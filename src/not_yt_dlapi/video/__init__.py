"""Video API endpoint."""

from __future__ import annotations

from copy import deepcopy
from logging import NullHandler, getLogger
from typing import Any, override

from good_ass_pydantic_integrator import CustomSerializer, ReplacementType

from not_yt_dlapi.base_api_endpoint import BaseEndpoint, generate_timestamp
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.exceptions import VideoNotFoundError
from not_yt_dlapi.video.models import VideoModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Videos(BaseEndpoint[VideoModel]):
    """Provides methods to download, parse, and retrieve video data."""

    _response_model = VideoModel

    @classmethod
    @override
    def _replacement_types(cls) -> list[ReplacementType]:
        return [
            ReplacementType(
                class_name="ContentDetails",
                field_name="dimension",
                new_type="str",
            ),
        ]

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="ContentDetails",
                field_name="duration",
                serializer_code="if value == timedelta(days=0):\n"
                '    return "P0D"\n'
                "return value",
                output_type="timedelta",
            ),
        ]

    def download(self, video_id: str) -> dict[str, Any]:
        """Downloads video data for a given video ID.

        Args:
            video_id: The ID of the video to download.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        part = (
            "contentDetails,"
            "id,"
            "liveStreamingDetails,"
            "localizations,"
            "paidProductPlacementDetails,"
            "player,"
            "recordingDetails,"
            "snippet,"
            "statistics,"
            "status,"
            "topicDetails"
        )

        logger.info("Downloading Video: %s ", video_id)
        output = self._client.get_around.get(
            f"{BASE_URL}/videos",
            params={"part": part, "id": video_id, "key": self._client.api_key},
        ).json()
        output["not_yt_dlapi"] = {
            "video_id": video_id,
            "part": part,
            "timestamp": generate_timestamp(),
        }
        return output

    def get(self, video_id: str) -> VideoModel:
        """Downloads and parses video data for a given video ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            video_id: The ID of the video to get.

        Returns:
            A Video model containing the parsed data.
        """
        response = self.download(video_id)
        if not response["items"]:
            msg = f"Video with ID '{video_id}' not found."
            raise VideoNotFoundError(msg)

        return self.parse(response)

    def download_multiple(self, video_ids: list[str]) -> list[dict[str, Any]]:
        """Downloads video data for multiple video IDs, split into individual responses.

        Automatically batches into groups of 50 (the API maximum per request).

        Args:
            video_ids: The IDs of the videos to download.

        Returns:
            A list of raw JSON responses, one per video.
        """
        results: list[dict[str, Any]] = []
        for i in range(0, len(video_ids), 50):
            batch = video_ids[i : i + 50]
            response = self.download(",".join(batch))
            base = {k: v for k, v in response.items() if k != "items"}
            for item in response["items"]:
                single = deepcopy(base)
                single["items"] = [item]
                results.append(single)
        return results

    def get_multiple(self, video_ids: list[str]) -> list[VideoModel]:
        """Downloads and parses video data for multiple video IDs.

        Each video is returned as its own model with a single item.

        Args:
            video_ids: The IDs of the videos to get.

        Returns:
            A list of VideoModel instances, one per video.
        """
        return [self.parse(response) for response in self.download_multiple(video_ids)]

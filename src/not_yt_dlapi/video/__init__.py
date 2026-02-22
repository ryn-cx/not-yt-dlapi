"""Video API endpoint."""

from __future__ import annotations

from datetime import datetime
from logging import NullHandler, getLogger
from typing import Any, override

from good_ass_pydantic_integrator import CustomSerializer, ReplacementType

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.exceptions import VideoNotFoundError
from not_yt_dlapi.video.models import VideoModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Video(BaseEndpoint[VideoModel]):
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
                input_type="timedelta",
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
        resource = self._client.youtube.videos()
        method = resource.list
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
        request = method(part=part, id=video_id)

        logger.info("Downloading Video: %s ", video_id)
        output = request.execute()
        output["not_yt_dlapi"] = {}
        output["not_yt_dlapi"]["video_id"] = video_id
        output["not_yt_dlapi"]["part"] = part
        timestamp = datetime.now().astimezone().isoformat().replace("+00:00", "Z")
        output["not_yt_dlapi"]["timestamp"] = timestamp

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

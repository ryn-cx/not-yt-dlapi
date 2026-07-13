# TODO: Validate
"""Contains the Videos class."""

from __future__ import annotations

from copy import deepcopy
from logging import NullHandler, getLogger
from typing import Any, override

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.exceptions import (
    HTTP_NOT_FOUND,
    NotYTDLAPIError,
    VideoNotFoundError,
)
from not_yt_dlapi.video.models import VideosModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Videos(BaseEndpoint[VideosModel]):
    """Manage the videos file."""

    _response_model = VideosModel

    def download(self, video_id: str) -> dict[str, Any]:
        """Downloads the videos file."""
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

        logger.info("Downloading: %s", f"{self.__class__.__name__} {video_id}")
        output = self._client.authenticated_get(
            f"{BASE_URL}/videos",
            params={"part": part, "id": video_id},
        ).json()
        if "error" in output:
            msg = output["error"]["message"]
            if output["error"]["code"] == HTTP_NOT_FOUND:
                raise VideoNotFoundError(msg)
            raise NotYTDLAPIError(msg)

        return output

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response.get("items"))

    def get(self, video_id: str) -> VideosModel:
        """Downloads and parses the videos file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        data = self.download(video_id)
        return self._parse_or_raise(data, f"{self.__class__.__name__} {video_id}")

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

    def get_multiple(self, video_ids: list[str]) -> list[VideosModel]:
        """Downloads and parses video data for multiple video IDs.

        Each video is returned as its own model with a single item.

        Args:
            video_ids: The IDs of the videos to get.

        Returns:
            A list of VideosModel instances, one per video.
        """
        return [self.parse(response) for response in self.download_multiple(video_ids)]

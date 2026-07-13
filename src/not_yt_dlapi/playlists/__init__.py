# TODO: Validate
"""Contains the Playlists class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from not_yt_dlapi.base_api_endpoint import (
    BaseEndpoint,
    fetch_all_pages,
)
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.exceptions import (
    HTTP_NOT_FOUND,
    NotYTDLAPIError,
    PlaylistNotFoundError,
)
from not_yt_dlapi.playlists.models import PlaylistsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,localizations,player,snippet,status"


class Playlists(BaseEndpoint[PlaylistsModel]):
    """Manage the playlists file."""

    _response_model = PlaylistsModel

    def download(self, channel_id: str) -> dict[str, Any]:
        """Downloads the playlists file."""
        logger.info("Downloading: %s", f"{self.__class__.__name__} {channel_id}")
        output = self._client.authenticated_get(
            f"{BASE_URL}/playlists",
            params={
                "part": PART,
                "channelId": channel_id,
                "maxResults": 50,
            },
        ).json()
        if "error" in output:
            msg = output["error"]["message"]
            if output["error"]["code"] == HTTP_NOT_FOUND:
                raise PlaylistNotFoundError(msg)
            raise NotYTDLAPIError(msg)

        return output

    def download_all(self, channel_id: str) -> dict[str, Any]:
        """Downloads all playlists for a channel with automatic pagination.

        Args:
            channel_id: The ID of the channel.

        Returns:
            A combined response dict with all playlists from every page.
        """
        logger.info("Downloading: %s", f"{self.__class__.__name__} {channel_id}")
        output = fetch_all_pages(
            self._client,
            f"{BASE_URL}/playlists",
            {"part": PART, "channelId": channel_id},
        )
        if "error" in output:
            msg = output["error"]["message"]
            if output["error"]["code"] == HTTP_NOT_FOUND:
                raise PlaylistNotFoundError(msg)
            raise NotYTDLAPIError(msg)

        return output

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response.get("items"))

    def get(self, channel_id: str) -> PlaylistsModel:
        """Downloads and parses the playlists file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        data = self.download(channel_id)
        return self._parse_or_raise(data, f"{self.__class__.__name__} {channel_id}")

    def get_all(self, channel_id: str) -> PlaylistsModel:
        """Downloads and parses all playlists for a channel.

        Args:
            channel_id: The ID of the channel.

        Returns:
            A PlaylistsModel containing all parsed playlists.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        data = self.download_all(channel_id)
        return self._parse_or_raise(data, f"{self.__class__.__name__} {channel_id}")

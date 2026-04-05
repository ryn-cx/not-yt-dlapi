"""Playlist Item API endpoint."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from not_yt_dlapi.base_api_endpoint import (
    BaseEndpoint,
    fetch_all_pages,
    generate_timestamp,
)
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.exceptions import (
    HTTP_NOT_FOUND,
    NotYTDLAPIError,
    PlaylistItemsNotFoundError,
)
from not_yt_dlapi.playlist_item.models import PlaylistItemModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,snippet,status"


class PlaylistItems(BaseEndpoint[PlaylistItemModel]):
    """Provides methods to download, parse, and retrieve playlist item data."""

    _response_model = PlaylistItemModel

    def download(self, playlist_id: str) -> dict[str, Any]:
        """Downloads a single page of items from a playlist.

        Args:
            playlist_id: The ID of the playlist.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        logger.info("Downloading PlaylistItems for Playlist: %s", playlist_id)
        output = self._client.get_around.get(
            f"{BASE_URL}/playlistItems",
            params={
                "part": PART,
                "playlistId": playlist_id,
                "maxResults": 50,
                "key": self._client.api_key,
            },
        ).json()
        output["not_yt_dlapi"] = {
            "playlist_id": playlist_id,
            "part": PART,
            "timestamp": generate_timestamp(),
        }

        if "error" in output:
            msg = output["error"]["message"]
            if output["error"]["code"] == HTTP_NOT_FOUND:
                raise PlaylistItemsNotFoundError(msg)
            raise NotYTDLAPIError(msg)

        return output

    def download_all(self, playlist_id: str) -> dict[str, Any]:
        """Downloads all items from a playlist with automatic pagination.

        Args:
            playlist_id: The ID of the playlist.

        Returns:
            A combined response dict with all items from every page.
        """
        logger.info("Downloading all PlaylistItems for Playlist: %s", playlist_id)
        output = fetch_all_pages(
            self._client,
            f"{BASE_URL}/playlistItems",
            {"part": PART, "playlistId": playlist_id, "key": self._client.api_key},
        )
        output["not_yt_dlapi"] = {
            "playlist_id": playlist_id,
            "part": PART,
            "timestamp": generate_timestamp(),
        }

        if "error" in output:
            msg = output["error"]["message"]
            if output["error"]["code"] == HTTP_NOT_FOUND:
                raise PlaylistItemsNotFoundError(msg)
            raise NotYTDLAPIError(msg)

        return output

    def get(self, playlist_id: str) -> PlaylistItemModel:
        """Downloads and parses a single page of items from a playlist.

        Args:
            playlist_id: The ID of the playlist.

        Returns:
            A PlaylistItemModel containing the parsed data.
        """
        return self.parse(self.download(playlist_id))

    def get_all(self, playlist_id: str) -> PlaylistItemModel:
        """Downloads and parses all items from a playlist.

        Args:
            playlist_id: The ID of the playlist.

        Returns:
            A PlaylistItemModel containing all parsed items.
        """
        return self.parse(self.download_all(playlist_id))

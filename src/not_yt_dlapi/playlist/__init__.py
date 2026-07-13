# TODO: Validate
"""Contains the Playlist class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.exceptions import (
    HTTP_NOT_FOUND,
    NotYTDLAPIError,
    PlaylistNotFoundError,
)
from not_yt_dlapi.playlist.models import PlaylistModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,localizations,player,snippet,status"


class Playlist(BaseEndpoint[PlaylistModel]):
    """Manage the playlist file."""

    _response_model = PlaylistModel

    def download(self, playlist_id: str) -> dict[str, Any]:
        """Downloads the playlist file."""
        logger.info("Downloading: %s", f"{self.__class__.__name__} {playlist_id}")
        output = self._client.authenticated_get(
            f"{BASE_URL}/playlists",
            params={
                "part": PART,
                "id": playlist_id,
                "maxResults": 50,
            },
        ).json()

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

    def get(self, playlist_id: str) -> PlaylistModel:
        """Downloads and parses the playlist file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        data = self.download(playlist_id)
        return self._parse_or_raise(data, f"{self.__class__.__name__} {playlist_id}")

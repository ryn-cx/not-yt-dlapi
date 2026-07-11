# TODO: Validate
"""Playlist API endpoint."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from good_ass_pydantic_integrator import ReplacementType

from not_yt_dlapi.base_api_endpoint import (
    BaseEndpoint,
    generate_timestamp,
)
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
    """Provides methods to download, parse, and retrieve a single playlist."""

    _response_model = PlaylistModel

    @classmethod
    @override
    def _replacement_types(cls) -> list[ReplacementType]:
        return [
            ReplacementType(
                class_name="Snippet",
                field_name="published_at",
                new_type="str",
            ),
        ]

    def download(self, playlist_id: str) -> dict[str, Any]:
        """Downloads playlist metadata by playlist ID.

        Unlike ``Playlists.download`` (which filters by channel), this fetches
        playlists by their own IDs. This is the only official way to retrieve
        auto-generated playlists, such as a Topic channel's album playlists,
        which are not returned when filtering by ``channelId``.

        Args:
            playlist_id: A playlist ID, or a comma-separated list of playlist IDs
                (up to 50).

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        logger.info("Downloading Playlist by ID: %s", playlist_id)
        output = self._client.authenticated_get(
            f"{BASE_URL}/playlists",
            params={
                "part": PART,
                "id": playlist_id,
                "maxResults": 50,
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
                raise PlaylistNotFoundError(msg)
            raise NotYTDLAPIError(msg)

        return output

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response.get("items"))

    def get(self, playlist_id: str) -> PlaylistModel:
        """Downloads and parses playlist metadata by playlist ID.

        Args:
            playlist_id: A playlist ID, or a comma-separated list of playlist IDs
                (up to 50).

        Returns:
            A PlaylistModel containing the parsed data.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        data = self.download(playlist_id)
        return self._parse_or_raise(data, has_content=self.has_content(data))

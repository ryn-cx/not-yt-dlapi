"""Playlist API endpoint."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from good_ass_pydantic_integrator import ReplacementType

from not_yt_dlapi.base_api_endpoint import (
    BaseEndpoint,
    fetch_all_pages,
    generate_timestamp,
)
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.playlist.models import PlaylistModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,localizations,player,snippet,status"


class Playlists(BaseEndpoint[PlaylistModel]):
    """Provides methods to download, parse, and retrieve playlist data."""

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

    def download(self, channel_id: str) -> dict[str, Any]:
        """Downloads a single page of playlists for a channel.

        Args:
            channel_id: The ID of the channel.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        logger.info("Downloading Playlists for Channel: %s", channel_id)
        output = self._client.get_around.get(
            f"{BASE_URL}/playlists",
            params={
                "part": PART,
                "channelId": channel_id,
                "maxResults": 50,
                "key": self._client.api_key,
            },
        ).json()
        output["not_yt_dlapi"] = {
            "channel_id": channel_id,
            "part": PART,
            "timestamp": generate_timestamp(),
        }
        return output

    def download_all(self, channel_id: str) -> dict[str, Any]:
        """Downloads all playlists for a channel with automatic pagination.

        Args:
            channel_id: The ID of the channel.

        Returns:
            A combined response dict with all playlists from every page.
        """
        logger.info("Downloading all Playlists for Channel: %s", channel_id)
        output = fetch_all_pages(
            self._client,
            f"{BASE_URL}/playlists",
            {"part": PART, "channelId": channel_id, "key": self._client.api_key},
        )
        output["not_yt_dlapi"] = {
            "channel_id": channel_id,
            "part": PART,
            "timestamp": generate_timestamp(),
        }
        return output

    def get(self, channel_id: str) -> PlaylistModel:
        """Downloads and parses a single page of playlists for a channel.

        Args:
            channel_id: The ID of the channel.

        Returns:
            A PlaylistModel containing the parsed data.
        """
        response = self.download(channel_id)
        return self.parse(response)

    def get_all(self, channel_id: str) -> PlaylistModel:
        """Downloads and parses all playlists for a channel.

        Args:
            channel_id: The ID of the channel.

        Returns:
            A PlaylistModel containing all parsed playlists.
        """
        response = self.download_all(channel_id)
        return self.parse(response)

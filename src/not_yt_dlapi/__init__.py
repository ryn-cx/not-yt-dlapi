# TODO: Validate
"""Contains the NotYTDLAPI class."""

from __future__ import annotations

import time
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from get_around import GetAround
from google.auth.transport.requests import Request

from not_yt_dlapi.channel import Channels
from not_yt_dlapi.playlist import Playlist
from not_yt_dlapi.playlist_item import PlaylistItems
from not_yt_dlapi.playlists import Playlists
from not_yt_dlapi.video import Videos

if TYPE_CHECKING:
    import httpx
    from google.oauth2.credentials import Credentials

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class NotYTDLAPI:
    """YouTube Data API wrapper."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        credentials: Credentials | None = None,
        get_around_client: GetAround | None = None,
    ) -> None:
        """Initialize the NotYTDLAPI client."""
        if api_key is None and credentials is None:
            msg = "Either api_key or credentials must be provided."
            raise ValueError(msg)

        self.api_key = api_key
        self.credentials = credentials
        self.get_around_client = get_around_client or GetAround()

        self.videos = Videos(self)
        self.playlists = Playlists(self)
        self.playlist = Playlist(self)
        self.playlist_items = PlaylistItems(self)
        self.channels = Channels(self)

    def authenticated_get(
        self,
        url: str,
        params: dict[str, Any],
    ) -> httpx.Response:
        """Perform a GET request authenticated with OAuth or an API key."""
        request_params = dict(params)
        headers: dict[str, str] = {}
        if self.credentials is not None:
            if not self.credentials.valid:
                self.credentials.refresh(Request())
            headers["Authorization"] = f"Bearer {self.credentials.token}"
        else:
            request_params["key"] = self.api_key

        # Log the caller-supplied params rather than request_params so the API key
        # is never written to the logs.
        operation = f"{url} params={params}"
        logger.debug("Downloading: %s", operation)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=request_params,
            headers=headers,
        )
        logger.debug("Downloaded %s (%.4f s)", operation, time.monotonic() - start)
        return response

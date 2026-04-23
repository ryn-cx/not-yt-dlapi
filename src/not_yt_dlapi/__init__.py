"""NotYTDLAPI is a companion for yt-dlapi."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from get_around import GetAround
from google.auth.transport.requests import Request

from not_yt_dlapi.channel import Channels
from not_yt_dlapi.playlist import Playlists
from not_yt_dlapi.playlist_item import PlaylistItems
from not_yt_dlapi.video import Videos

if TYPE_CHECKING:
    import httpx
    from google.oauth2.credentials import Credentials


class NotYTDLAPI:
    """Interface for downloading and parsing data from the YouTube Data API."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        credentials: Credentials | None = None,
        get_around_server: str | None = None,
        get_around_password: str | None = None,
    ) -> None:
        """Initialize the NotYTDLAPI client.

        Provide either ``api_key`` for public data access or ``credentials`` for
        OAuth-authenticated access. When ``credentials`` is supplied and the
        access token has expired, it is refreshed automatically before each
        request (the credentials object must have a refresh token, client id,
        client secret, and token URI for refresh to succeed).
        """
        if api_key is None and credentials is None:
            msg = "Either api_key or credentials must be provided."
            raise ValueError(msg)

        self.api_key = api_key
        self.credentials = credentials
        self.get_around = GetAround(
            server=get_around_server,
            password=get_around_password,
        )

        self.videos = Videos(self)
        self.playlists = Playlists(self)
        self.playlist_items = PlaylistItems(self)
        self.channels = Channels(self)

    def authenticated_get(
        self,
        url: str,
        params: dict[str, Any],
    ) -> httpx.Response:
        """Perform a GET request authenticated with OAuth or an API key.

        When OAuth ``credentials`` are configured, the access token is refreshed
        if expired and passed as a Bearer token in the ``Authorization`` header.
        Otherwise the ``api_key`` is injected as a ``key`` query parameter.
        """
        request_params = dict(params)
        headers: dict[str, str] = {}
        if self.credentials is not None:
            if not self.credentials.valid:
                self.credentials.refresh(Request())
            headers["Authorization"] = f"Bearer {self.credentials.token}"
        else:
            request_params["key"] = self.api_key
        return self.get_around.get(url, params=request_params, headers=headers)

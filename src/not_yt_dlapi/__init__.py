# TODO: Validate
from __future__ import annotations

import time
from itertools import count
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, overload

from get_around import GetAround
from google.auth.transport.requests import Request

from not_yt_dlapi.channel import Channel
from not_yt_dlapi.channel_section import ChannelSections
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.exceptions import HTTP_NOT_FOUND, NotYTDLAPIError
from not_yt_dlapi.playlist_item import PlaylistItems
from not_yt_dlapi.playlists import Playlists
from not_yt_dlapi.video import Videos

if TYPE_CHECKING:
    from google.oauth2.credentials import Credentials

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class NotYTDLAPI:
    @overload
    def __init__(
        self,
        *,
        api_key: str,
        credentials: Credentials | None = None,
        get_around_client: GetAround | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        api_key: str | None = None,
        credentials: Credentials,
        get_around_client: GetAround | None = None,
    ) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = None,
        credentials: Credentials | None = None,
        get_around_client: GetAround | None = None,
    ) -> None:
        if api_key is None and credentials is None:
            msg = "Either api_key or credentials must be provided."
            raise ValueError(msg)

        self.api_key = api_key
        self.credentials = credentials
        self.get_around_client = get_around_client or GetAround()

        self.videos = Videos(self)
        self.playlists = Playlists(self)
        self.playlist_items = PlaylistItems(self)
        self.channel = Channel(self)
        self.channel_sections = ChannelSections(self)

    def download(
        self,
        path: str,
        params: dict[str, Any],
        log_id: str,
        not_found_error: type[NotYTDLAPIError] = NotYTDLAPIError,
    ) -> dict[str, Any]:
        headers: dict[str, str] = {}
        if self.credentials:
            if not self.credentials.valid:
                self.credentials.refresh(Request())
            headers["Authorization"] = f"Bearer {self.credentials.token}"
        else:
            params["key"] = self.api_key

        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            f"{BASE_URL}/{path}",
            params=params,
            headers=headers,
        )
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)

        response_json: dict[str, Any] = response.json()
        if "error" in response_json:
            msg = response_json["error"]["message"]
            if response_json["error"]["code"] == HTTP_NOT_FOUND:
                raise not_found_error(msg, response_json)
            raise NotYTDLAPIError(msg, response_json)
        return response_json

    def download_all_pages(
        self,
        path: str,
        params: dict[str, Any],
        log_id: str,
        *,
        not_found_error: type[NotYTDLAPIError] = NotYTDLAPIError,
    ) -> list[dict[str, Any]]:
        pages: list[dict[str, Any]] = []
        for page in count(start=1, step=1):
            response = self.download(
                path,
                params,
                f"{log_id} {page=}",
                not_found_error,
            )
            pages.append(response)

            params["pageToken"] = response.get("nextPageToken")
            if not params["pageToken"]:
                break

        return pages

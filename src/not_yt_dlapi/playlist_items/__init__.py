# TODO: Validate
"""Contains the PlaylistItems class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.exceptions import PlaylistNotFoundError, ResourceNotFoundError
from not_yt_dlapi.playlist_items.models import (
    PlaylistItemsModel,
    model_validate_json,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from not_yt_dlapi.playlist_items.models import Item

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,snippet,status"
"""Every part a key can ask for, which is what is always asked for."""

DEFAULT_MAX_RESULTS = 50
"""The most the API will put on one page, which is what it is always asked for."""


# TODO: Validate
class PlaylistItems(BaseEndpoint):
    """The videos a playlist holds, as the playlist holds them.

    Source: https://developers.google.com/youtube/v3/docs/playlistItems

    Example request:
        - GET /youtube/v3/playlistItems?
            - part={part}&
            - playlistId={playlist_id}&
            - maxResults=50&
            - key=__REDACTED__
            - HTTP/2
        - Host: www.googleapis.com
    """

    # TODO: Validate
    def __call__(
        self,
        playlist_id: str,
        *,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistItemsModel:
        """Download and parse the playlist items file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                playlist_id,
                max_results=max_results,
                page_token=page_token,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        playlist_id: str,
        *,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> str:
        """Download one page of the playlist items file.

        A playlist YouTube generated for a show is answered with an empty page
        rather than refused, and no part or parameter makes it hold anything.
        `shows` is what lists one of those.

        Raises:
            PlaylistNotFoundError: If there is no playlist with that id.
        """
        log_id = self.get_log_id(self.download, locals())
        params: dict[str, Any] = {
            "part": PART,
            "playlistId": playlist_id,
            "maxResults": max_results,
        }
        if page_token is not None:
            params["pageToken"] = page_token

        try:
            return self._client.download(
                endpoint="playlistItems",
                params=params,
                headers={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise PlaylistNotFoundError(
                playlist_id,
                err.error,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def download_all(self, playlist_id: str) -> list[str]:
        """Download every page of a playlist's items, first to last.

        There is no limit on how long the playlist may be beyond how long a
        caller is willing to wait.

        Raises:
            PlaylistNotFoundError: If there is no playlist with that id.
        """
        pages: list[str] = []
        page_token: str | None = None
        while True:
            page = self.download(playlist_id, page_token=page_token)
            pages.append(page)
            page_token = self.load(page).next_page_token
            if page_token is None:
                return pages

    # TODO: Validate
    def download_merged(self, playlist_id: str) -> str:
        """Download every page of a playlist's items as a single file.

        The pages are put together into one file holding every item, which is
        the whole playlist written the way one page of it is, rather than the
        pages themselves.

        Raises:
            PlaylistNotFoundError: If there is no playlist with that id.
        """
        return self.merge_pages(self.download_all(playlist_id))

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> PlaylistItemsModel:
        """Load a playlist items file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[PlaylistItemsModel]:
        """Read the pages `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    # TODO: Validate
    def extract_items(self, datas: Sequence[PlaylistItemsModel | str]) -> list[Item]:
        """Extract the items from one or more files."""
        return [
            item
            for entry in datas
            for item in (
                entry if isinstance(entry, PlaylistItemsModel) else self.load(entry)
            ).items
        ]

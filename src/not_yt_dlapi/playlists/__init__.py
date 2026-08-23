# TODO: Validate
"""Contains the Playlists class."""

from __future__ import annotations

from itertools import batched
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.exceptions import ChannelNotFoundError, ResourceNotFoundError
from not_yt_dlapi.playlists.models import PlaylistsModel, model_validate_json

if TYPE_CHECKING:
    from collections.abc import Sequence

    from not_yt_dlapi.playlists.models import Item

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,localizations,player,snippet,status"
"""Every part a key can ask for, which is what is always asked for."""

DEFAULT_MAX_RESULTS = 50
"""The most the API will put on one page, which is what it is always asked for."""

MAX_IDS = 50
"""The most ids one request takes. Past this the API refuses rather than cuts."""


# TODO: Validate
class Playlists(BaseEndpoint):
    """A `playlist` resource represents a YouTube playlist.

    Source: https://developers.google.com/youtube/v3/docs/playlists

    Example request:
        - GET /youtube/v3/playlists?
            - part={part}&
            - id={playlist_ids}&
            - maxResults=50&
            - key=__REDACTED__
            - HTTP/2
        - Host: www.googleapis.com
    """

    # TODO: Validate
    @overload
    def __call__(
        self,
        *,
        playlist_ids: str | Sequence[str],
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistsModel: ...

    # TODO: Validate
    @overload
    def __call__(
        self,
        *,
        channel_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistsModel: ...

    # TODO: Validate
    def __call__(
        self,
        *,
        playlist_ids: str | Sequence[str] | None = None,
        channel_id: str | None = None,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistsModel:
        """Look the playlists up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                playlist_ids=playlist_ids,
                channel_id=channel_id,
                max_results=max_results,
                page_token=page_token,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        *,
        playlist_ids: str | Sequence[str] | None = None,
        channel_id: str | None = None,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> str:
        """Download one page of the playlists file.

        Up to fifty playlists can be asked for by id at once. An id nothing is
        under is not an error to the API: it answers with the playlists it did
        find and says nothing about the rest.

        Raises:
            ValueError: If the playlists are not named by exactly one of the
                two things they can be named by, which is all the API accepts.
            ChannelNotFoundError: If there is no channel with that id.
        """
        log_id = self.get_log_id(self.download, locals())
        ids = [playlist_ids] if isinstance(playlist_ids, str) else playlist_ids
        given = {
            name: value
            for name, value in (
                ("id", ",".join(ids) if ids is not None else None),
                ("channelId", channel_id),
            )
            if value is not None
        }
        if len(given) != 1:
            msg = "Invalid number of arguments."
            raise ValueError(msg)

        params: dict[str, Any] = {**given, "part": PART, "maxResults": max_results}
        if page_token is not None:
            params["pageToken"] = page_token

        try:
            return self._client.download(
                endpoint="playlists",
                params=params,
                headers={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ChannelNotFoundError(
                channel_id or "",
                err.error,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    @overload
    def download_all(self, *, playlist_ids: Sequence[str]) -> list[str]: ...

    # TODO: Validate
    @overload
    def download_all(self, *, channel_id: str) -> list[str]: ...

    # TODO: Validate
    def download_all(
        self,
        *,
        playlist_ids: Sequence[str] | None = None,
        channel_id: str | None = None,
    ) -> list[str]:
        """Download every playlist asked for, one file per request made.

        Asked for by id, the API takes fifty ids at a time and refuses more, so
        the ids are asked about fifty at a time. Asked for by channel, the
        playlists come back a page at a time, so the pages are walked to the
        end. There is no limit beyond how long a caller is willing to wait.

        Raises:
            ValueError: If the playlists are not named by exactly one of the
                two things they can be named by, which is all the API accepts.
            ChannelNotFoundError: If there is no channel with that id.
        """
        if playlist_ids is not None and channel_id is None:
            # The last batch is however many are left over, not a whole fifty.
            return [
                self.download(playlist_ids=batch)
                for batch in batched(playlist_ids, MAX_IDS, strict=False)
            ]
        if channel_id is not None and playlist_ids is None:
            return self._channel_pages(channel_id)
        msg = "Invalid number of arguments."
        raise ValueError(msg)

    # TODO: Validate
    def _channel_pages(self, channel_id: str) -> list[str]:
        """Download every page of the playlists a channel made, first to last."""
        pages: list[str] = []
        page_token: str | None = None
        while True:
            page = self.download(channel_id=channel_id, page_token=page_token)
            pages.append(page)
            page_token = self.load(page).next_page_token
            if page_token is None:
                return pages

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> PlaylistsModel:
        """Read a downloaded playlists file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[PlaylistsModel]:
        """Read the files `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    # TODO: Validate
    def extract_items(self, datas: Sequence[PlaylistsModel | str]) -> list[Item]:
        """Extract the items from one or more files."""
        return [
            item
            for entry in datas
            for item in (
                entry if isinstance(entry, PlaylistsModel) else self.load(entry)
            ).items
        ]

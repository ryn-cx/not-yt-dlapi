# TODO: Validate
"""Contains the Playlists class.

Playlists are asked for either by their own ids or by the channel they belong
to, and the API takes exactly one of the two, so the endpoint does too. A page
of them comes back at a time; `next_page_token` on the result is what asks for
the page after it.

Every part the API will hand out is always asked for, so what a request answers
with is decided only by the playlist rather than by the caller. That is what
lets `models` say which properties a playlist always carries.

`feed` is not the API. It is the Atom feed of the playlist's fifteen most recent
videos, which is served from youtube.com, takes no key and costs no quota.
YouTube is currently refusing every playlist feed it is asked for, so it raises
rather than answering until that is fixed.
"""

from __future__ import annotations

from itertools import batched
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, overload

if TYPE_CHECKING:
    import builtins
    from collections.abc import Iterator, Sequence

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.playlists.models import PlaylistFeedResponse, PlaylistListResponse

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
    """Playlists, by their own ids or by the channel that owns them."""

    # TODO: Validate
    @overload
    def list(
        self,
        *,
        playlist_ids: str | Sequence[str],
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistListResponse: ...

    # TODO: Validate
    @overload
    def list(
        self,
        *,
        channel_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistListResponse: ...

    # TODO: Validate
    def list(
        self,
        *,
        playlist_ids: str | Sequence[str] | None = None,
        channel_id: str | None = None,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistListResponse:
        """Download a page of playlists and read it.

        Up to 50 playlists can be asked for by id at once. An id nothing is
        under is not an error to the API: it answers with the playlists it did
        find and says nothing about the rest, so a request for an unknown id
        comes back empty rather than raising. A channel id nothing is under is
        refused.

        Raises:
            ValueError: If the playlists are not named by exactly one of the
                two things they can be named by, which is all the API accepts.
            NotFoundError: If there is no channel with that id.
        """
        log_id = self.get_log_id(self.list, locals())
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

        data = self._client.download("playlists", params, log_id)
        return PlaylistListResponse.from_response(data)

    # TODO: Validate
    def feed(self, *, playlist_id: str) -> PlaylistFeedResponse:
        """Download the playlist's feed and read it.

        The feed is the fifteen most recent videos and nothing else: there is no
        paging and no way to ask for more, so a playlist's whole contents are
        still only `playlist_items.list`.

        YouTube is currently refusing every playlist feed it is asked for, so at
        the moment this always raises. Nothing here has been checked against a
        downloaded feed for that reason; it is written on the understanding that
        a playlist feed is the same document a channel feed is but for saying
        which playlist it is of.

        Raises:
            HTTPError: If the feed is refused, which is every playlist feed
                while they are down, and otherwise if there is no playlist with
                that id.
        """
        log_id = self.get_log_id(self.feed, locals())
        data = self._client.download_feed({"playlist_id": playlist_id}, log_id)
        return PlaylistFeedResponse.from_response(data)

    # TODO: Validate
    def _channel_pages(self, channel_id: str) -> Iterator[PlaylistListResponse]:
        """Yield every page of the playlists a channel made, first to last."""
        page_token: str | None = None
        while True:
            page = self.list(channel_id=channel_id, page_token=page_token)
            yield page
            if page.next_page_token is None:
                return
            page_token = page.next_page_token

    # TODO: Validate
    @overload
    def list_all(
        self,
        *,
        playlist_ids: Sequence[str],
    ) -> builtins.list[PlaylistListResponse]: ...

    # TODO: Validate
    @overload
    def list_all(self, *, channel_id: str) -> builtins.list[PlaylistListResponse]: ...

    # TODO: Validate
    def list_all(
        self,
        *,
        playlist_ids: Sequence[str] | None = None,
        channel_id: str | None = None,
    ) -> builtins.list[PlaylistListResponse]:
        """Download every playlist asked for and read them one to a response.

        Asked for by id, the API takes fifty ids at a time and refuses more, so
        the ids are asked about fifty at a time. Asked for by channel, the
        playlists come back a page at a time, so the pages are walked to the
        end. Either way what comes back is put together, and there is no limit
        beyond how long a caller is willing to wait.

        Every playlist comes back in a response of its own, carrying whatever
        the response it arrived in said around it. That leaves `etag`,
        `page_info`, `raw` and the paging tokens describing a request that was
        never made, since no one request answered with exactly that one
        playlist. `kind` is right anyway.

        An id nothing is under is not answered for at all, so asking about a
        hundred ids does not mean a hundred playlists come back.

        Args:
            playlist_ids: The ids of the playlists to download.
            channel_id: The channel whose playlists to download, instead.

        Raises:
            ValueError: If the playlists are not named by exactly one of the
                two things they can be named by, which is all the API accepts.
            NotFoundError: If there is no channel with that id.
        """
        if playlist_ids is not None and channel_id is None:
            # The last batch is however many are left over, not a whole fifty.
            pages: Iterator[PlaylistListResponse] = (
                self.list(playlist_ids=batch)
                for batch in batched(playlist_ids, MAX_IDS, strict=False)
            )
        elif channel_id is not None and playlist_ids is None:
            pages = self._channel_pages(channel_id)
        else:
            msg = "Invalid number of arguments."
            raise ValueError(msg)

        return self.split(
            PlaylistListResponse.from_response,
            (page.raw for page in pages),
        )

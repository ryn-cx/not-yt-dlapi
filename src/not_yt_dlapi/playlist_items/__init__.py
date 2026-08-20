# TODO: Validate
"""Contains the PlaylistItems class.

A page of a playlist comes back at a time; `next_page_token` on the result is
what asks for the page after it.
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import builtins
    from collections.abc import Iterator

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.playlist_items.models import PlaylistItemListResponse

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,snippet,status"
"""Every part a key can ask for, which is what is always asked for."""

DEFAULT_MAX_RESULTS = 50
"""The most the API will put on one page, which is what it is always asked for."""


# TODO: Validate
class PlaylistItems(BaseEndpoint):
    """The videos in a playlist."""

    # TODO: Validate
    def list(
        self,
        playlist_id: str,
        *,
        max_results: int = DEFAULT_MAX_RESULTS,
        page_token: str | None = None,
    ) -> PlaylistItemListResponse:
        """Download a page of a playlist's items and read it.

        Raises:
            NotFoundError: If there is no playlist with that id.
        """
        log_id = self.get_log_id(self.list, locals())
        params: dict[str, Any] = {
            "part": PART,
            "playlistId": playlist_id,
            "maxResults": max_results,
        }
        if page_token is not None:
            params["pageToken"] = page_token

        data = self._client.download("playlistItems", params, log_id)
        return PlaylistItemListResponse.from_response(data)

    # TODO: Validate
    def _pages(self, playlist_id: str) -> Iterator[PlaylistItemListResponse]:
        """Yield every page of a playlist's items, first to last."""
        page_token: str | None = None
        while True:
            page = self.list(playlist_id, page_token=page_token)
            yield page
            if page.next_page_token is None:
                return
            page_token = page.next_page_token

    # TODO: Validate
    def list_all(
        self,
        playlist_id: str,
    ) -> builtins.list[PlaylistItemListResponse]:
        """Download every item in a playlist and read them one to a response.

        A playlist comes back a page at a time, so the pages are walked to the
        end and what comes back is put together. There is no limit on how long
        the playlist may be beyond how long a caller is willing to wait.

        Every item comes back in a response of its own, carrying whatever the
        page it arrived on said around it. That leaves `etag`, `page_info` and
        the paging tokens describing a request that was never made, since no one
        request answered with exactly that one item. `kind` is right anyway.

        Raises:
            NotFoundError: If there is no playlist with that id.
        """
        pages = (page.raw for page in self._pages(playlist_id))
        return self.split(PlaylistItemListResponse.from_response, pages)

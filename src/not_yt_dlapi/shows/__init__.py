# TODO: Validate
"""Contains the Shows class.

A show is a playlist the API will not hand out, so this goes to browse for it
and reads the page the site draws instead.

A `list` is one request and answers with one stretch of one season. A show of
more than one season is one playlist with a menu over it, and asking for the
playlist gives whichever season the menu starts on, so the seasons after it are
each their own thing to ask for; a season longer than one stretch carries the
token the next is asked for by. `list_all` is what asks for all of them.
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, overload

if TYPE_CHECKING:
    import builtins

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.shows.models import Show, ShowSeasonLink

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def show_browse_id(playlist_id: str) -> str:
    """Return what browse calls a show opened by the given id.

    A show has two ids. The `SC` one its page is at is already what browse
    calls it, and the `TVSH` playlist id is turned into one by putting `VL` in
    front of it. Sending either the wrong way answers with no episodes rather
    than a refusal.
    """
    return playlist_id if playlist_id.startswith("SC") else f"VL{playlist_id}"


# TODO: Validate
class Shows(BaseEndpoint):
    """Shows, which are the playlists the site draws a season menu over."""

    # TODO: Validate
    @overload
    def list(self, playlist_id: str) -> Show: ...

    # TODO: Validate
    @overload
    def list(self, *, season: ShowSeasonLink) -> Show: ...

    # TODO: Validate
    @overload
    def list(self, *, continuation: str) -> Show: ...

    # TODO: Validate
    def list(
        self,
        playlist_id: str | None = None,
        *,
        season: ShowSeasonLink | None = None,
        continuation: str | None = None,
    ) -> Show:
        """Download one stretch of a show and read it.

        A show is opened by either of its ids, a season of it is asked for by
        the entry the menu of them carries, and a stretch is carried on by the
        token the one before it ended with. Browse takes exactly one of the
        three, so this does too.

        Raises:
            ValueError: If the request is not named by exactly one of the three
                things it can be named by, which is all browse accepts.
        """
        log_id = self.get_log_id(self.list, locals())
        given: list[dict[str, Any]] = [
            asked
            for asked in (
                None
                if playlist_id is None
                else {"browseId": show_browse_id(playlist_id)},
                None
                if season is None
                else {"browseId": season.browse_id, "params": season.params},
                None if continuation is None else {"continuation": continuation},
            )
            if asked is not None
        ]
        if len(given) != 1:
            msg = "Invalid number of arguments."
            raise ValueError(msg)

        return Show.from_response(self._client.browse(given[0], log_id))

    # TODO: Validate
    def _season_pages(self, opened: Show) -> builtins.list[Show]:
        """Download every season of a show but the one already downloaded."""
        return [
            page
            for link in opened.seasons
            if not link.selected
            for page in self._pages_to_the_end(self.list(season=link))
        ]

    # TODO: Validate
    def _pages_to_the_end(self, opened: Show) -> builtins.list[Show]:
        """Download the rest of a listing already begun, first stretch to last."""
        pages = [opened]
        while pages[-1].continuation is not None:
            pages.append(self.list(continuation=pages[-1].continuation))
        return pages

    # TODO: Validate
    def list_all(self, playlist_id: str) -> builtins.list[Show]:
        """Download every season of a show, and every stretch of each of them.

        The show is opened, which answers with whichever season its menu starts
        on, and then each of the other seasons is asked for in the order the
        menu lists them. Every one of them is followed to the end of its
        listing, so what comes back is each season's stretches together and the
        seasons in the order they are numbered.

        Only a stretch that begins a season says which season it is: the ones
        carrying it on are the rest of a season already named, so a page saying
        nothing belongs to the last one that said.
        """
        opened = self.list(playlist_id)
        return self._pages_to_the_end(opened) + self._season_pages(opened)

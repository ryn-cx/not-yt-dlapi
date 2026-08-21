# TODO: Validate
"""Contains the Music class.

A music playlist is an album, single or EP that YouTube generated from a
release, and the API will hand one out but says nothing about whose music it
is: it answers that every one of them belongs to the YouTube channel. So this
goes to browse for it, the way `shows` does, and reads the release out of the
page the site draws rather than out of the resource the API documents.

Browse hands out a long listing a stretch at a time, so a `list` is one request
and answers with one stretch of the release. What comes back carries the token
the next stretch is asked for by, and `list_all` is what asks with it until
there is none left.
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, overload

if TYPE_CHECKING:
    import builtins

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.music.models import MusicPlaylist

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Music(BaseEndpoint):
    """Music playlists, which are the releases YouTube generated a playlist of."""

    # TODO: Validate
    @overload
    def list(self, playlist_id: str) -> MusicPlaylist: ...

    # TODO: Validate
    @overload
    def list(self, *, continuation: str) -> MusicPlaylist: ...

    # TODO: Validate
    def list(
        self,
        playlist_id: str | None = None,
        *,
        continuation: str | None = None,
    ) -> MusicPlaylist:
        """Download one stretch of a music playlist and read it.

        A playlist is opened by its id and carried on by the token the stretch
        before it ended with, and browse takes exactly one of the two, so this
        does too.

        Raises:
            ValueError: If the request is not named by exactly one of the two
                things it can be named by, which is all browse accepts.
        """
        log_id = self.get_log_id(self.list, locals())
        given: dict[str, Any] = {
            name: value
            for name, value in (
                ("browseId", None if playlist_id is None else f"VL{playlist_id}"),
                ("continuation", continuation),
            )
            if value is not None
        }
        if len(given) != 1:
            msg = "Invalid number of arguments."
            raise ValueError(msg)

        return MusicPlaylist.from_response(self._client.browse(given, log_id))

    # TODO: Validate
    def list_all(self, playlist_id: str) -> builtins.list[MusicPlaylist]:
        """Download every stretch of a music playlist, first to last.

        Only the first stretch carries the header, because the ones after it are
        the rest of a listing already asked for rather than the playlist again.
        So what says the release's name and who it is by is the first of what
        comes back, and the tracks are all of them run together.

        There is no limit beyond how long a caller is willing to wait: the
        listing is followed to its end however long it is.
        """
        pages = [self.list(playlist_id)]
        while pages[-1].continuation is not None:
            pages.append(self.list(continuation=pages[-1].continuation))
        return pages

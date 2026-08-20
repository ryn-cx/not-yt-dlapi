# TODO: Validate
"""Contains the Music class.

A music playlist is an album, single or EP that YouTube generated from a
release, and the API will hand one out but says nothing about whose music it
is: it answers that every one of them belongs to the YouTube channel. So this
goes to browse for it, the way `shows` does, and reads the release out of the
page the site draws rather than out of the resource the API documents.
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.music.models import MusicPlaylist

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Music(BaseEndpoint):
    """Music playlists, which are the releases YouTube generated a playlist of."""

    # TODO: Validate
    def list(self, playlist_id: str) -> MusicPlaylist:
        """Download a music playlist and read it.

        The whole listing is asked for however long it is, so what comes back is
        every track rather than a page of them.
        """
        log_id = self.get_log_id(self.list, locals())
        response = self._client.download_music(playlist_id, log_id)
        return MusicPlaylist.from_response(response)

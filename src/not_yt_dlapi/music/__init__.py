# TODO: Validate
"""Contains the Music class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.music.models import MusicModel, model_validate_json
from not_yt_dlapi.utils import find, read_continuation, read_text

logger = getLogger(__name__)
logger.addHandler(NullHandler())

VIDEO_LOCKUP = "LOCKUP_CONTENT_TYPE_VIDEO"
"""What browse marks the lockup of a track with, as against any other lockup."""


# TODO: Validate
class Music(BaseEndpoint):
    """A music playlist, which is the album, single or EP YouTube made of a release.

    The API hands one out but says every one of them belongs to the YouTube
    channel, so this asks browse for the page the site draws. One download is
    one stretch of the listing; `download_all` follows it to the end.

    Source: https://www.youtube.com/playlist?list={playlist_id}

    Example request:
        - POST /youtubei/v1/browse HTTP/2
        - Host: www.youtube.com
        - Content-Type: application/json
        - Body: {"browseId": "VL{playlist_id}", "context": {"client": ...}}
    """

    # TODO: Validate
    @overload
    def __call__(self, playlist_id: str) -> MusicModel: ...

    # TODO: Validate
    @overload
    def __call__(self, *, continuation: str) -> MusicModel: ...

    # TODO: Validate
    def __call__(
        self,
        playlist_id: str | None = None,
        *,
        continuation: str | None = None,
    ) -> MusicModel:
        """Look one stretch of a release up and return the model it reads into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(playlist_id, continuation=continuation),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        playlist_id: str | None = None,
        *,
        continuation: str | None = None,
    ) -> str:
        """Download one stretch of a music playlist.

        A playlist is opened by its id and carried on by the token the stretch
        before it ended with.

        Raises:
            ValueError: If the request is not named by exactly one of the two
                things it can be named by, which is all browse accepts.
        """
        log_id = self.get_log_id(self.download, locals())
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

        return self._client.browse(given, log_id)

    # TODO: Validate
    def download_all(self, playlist_id: str) -> list[str]:
        """Download every stretch of a music playlist, first to last.

        Only the first stretch carries the header, because the ones after it are
        the rest of a listing already asked for rather than the playlist again.
        """
        pages = [self.download(playlist_id)]
        continuation = self.extract_continuation(self.load(pages[0]))
        while continuation is not None:
            page = self.download(continuation=continuation)
            pages.append(page)
            continuation = self.extract_continuation(self.load(page))
        return pages

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MusicModel:
        """Read a downloaded music playlist file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[MusicModel]:
        """Read the stretches `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    # TODO: Validate
    @staticmethod
    def _header(data: MusicModel) -> dict[str, Any]:
        """Return what the release says about itself.

        Only the first stretch of a listing carries it.
        """
        return next(find(data.raw_input, "playlistHeaderRenderer"), {})

    # TODO: Validate
    @classmethod
    def extract_playlist_id(cls, data: MusicModel) -> str | None:
        """Extract the id of the release the stretch is of."""
        playlist_id: str | None = cls._header(data).get("playlistId")
        return playlist_id

    # TODO: Validate
    @classmethod
    def extract_title(cls, data: MusicModel) -> str | None:
        """Extract the release's name."""
        title = cls._header(data).get("title")
        return None if title is None else read_text(title)

    # TODO: Validate
    @classmethod
    def extract_artists(cls, data: MusicModel) -> list[str]:
        """Extract everyone the release is credited to, in the order it credits them.

        The subtitle reads "Future, Metro Boomin • Album", so the names are what
        comes before the bullet the release type is written after. The names are
        separated by commas and nothing marks where one ends, so an artist whose
        own name has a comma in it comes back as two.

        This is the only thing in an answer that names more than one musician,
        since every track is published by whichever single channel uploaded it.
        """
        credit, _, _ = cls._subtitle(data).rpartition(" • ")
        return [name.strip() for name in credit.split(",")] if credit else []

    # TODO: Validate
    @classmethod
    def extract_release_type(cls, data: MusicModel) -> str | None:
        """Extract what kind of release it is, such as "Album" or "Single"."""
        _, _, release_type = cls._subtitle(data).rpartition(" • ")
        return release_type or None

    # TODO: Validate
    @classmethod
    def _subtitle(cls, data: MusicModel) -> str:
        """Return the line crediting the release, as the text it spells."""
        subtitle = cls._header(data).get("subtitle")
        return "" if subtitle is None else read_text(subtitle)

    # TODO: Validate
    @staticmethod
    def extract_track_ids(data: MusicModel) -> list[str]:
        """Extract the id of every track the stretch listed, in the album's order.

        A music playlist has been seen listing nothing but videos, so a lockup
        written for anything else is not a track and is left out.
        """
        return [
            lockup["contentId"]
            for lockup in find(data.raw_input, "lockupViewModel")
            if lockup.get("contentType") == VIDEO_LOCKUP and "contentId" in lockup
        ]

    # TODO: Validate
    @staticmethod
    def extract_continuation(data: MusicModel) -> str | None:
        """Extract what the stretch after this one is asked for by."""
        return read_continuation(data.raw_input)

# TODO: Validate
"""Contains the Shows class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.shows.models import ShowsModel, model_validate_json
from not_yt_dlapi.utils import find, read_continuation, read_seasons

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
    """A show, which is the playlist the site draws a season menu over.

    The API will not hand a show out, so this asks browse for the page the site
    draws. One download is one stretch of one season; `download_all` walks every
    season to its end.

    Source: https://www.youtube.com/playlist?list={playlist_id}

    Example request:
        - POST /youtubei/v1/browse HTTP/2
        - Host: www.youtube.com
        - Content-Type: application/json
        - Body: {"browseId": "VL{playlist_id}", "context": {"client": ...}}
    """

    # TODO: Validate
    @overload
    def __call__(self, playlist_id: str) -> ShowsModel: ...

    # TODO: Validate
    @overload
    def __call__(self, *, season: dict[str, Any]) -> ShowsModel: ...

    # TODO: Validate
    @overload
    def __call__(self, *, continuation: str) -> ShowsModel: ...

    # TODO: Validate
    def __call__(
        self,
        playlist_id: str | None = None,
        *,
        season: dict[str, Any] | None = None,
        continuation: str | None = None,
    ) -> ShowsModel:
        """Look one stretch of a show up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(playlist_id, season=season, continuation=continuation),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        playlist_id: str | None = None,
        *,
        season: dict[str, Any] | None = None,
        continuation: str | None = None,
    ) -> str:
        """Download one stretch of a show.

        A show is opened by either of its ids, a season of it is asked for by
        the browse endpoint `extract_season_endpoints` returns for it, and a
        stretch is carried on by the token the one before it ended with.

        Raises:
            ValueError: If the request is not named by exactly one of the three
                things it can be named by, which is all browse accepts.
        """
        log_id = self.get_log_id(self.download, locals())
        given: list[dict[str, Any]] = [
            asked
            for asked in (
                None
                if playlist_id is None
                else {"browseId": show_browse_id(playlist_id)},
                season,
                None if continuation is None else {"continuation": continuation},
            )
            if asked is not None
        ]
        if len(given) != 1:
            msg = "Invalid number of arguments."
            raise ValueError(msg)

        return self._client.browse(given[0], log_id)

    # TODO: Validate
    def download_all(self, playlist_id: str) -> list[str]:
        """Download every season of a show, and every stretch of each of them.

        The show is opened, which answers with whichever season its menu starts
        on, and then each of the other seasons is asked for in the order the
        menu lists them. Every one of them is followed to the end of its
        listing.
        """
        opened = self.download(playlist_id)
        pages = self._stretches_to_the_end(opened)
        for season in self.extract_season_endpoints(self.load(opened)):
            pages.extend(self._stretches_to_the_end(self.download(season=season)))
        return pages

    # TODO: Validate
    def _stretches_to_the_end(self, opened: str) -> list[str]:
        """Download the rest of a listing already begun, first stretch to last."""
        pages = [opened]
        continuation = self.extract_continuation(self.load(opened))
        while continuation is not None:
            page = self.download(continuation=continuation)
            pages.append(page)
            continuation = self.extract_continuation(self.load(page))
        return pages

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ShowsModel:
        """Read a downloaded show file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[ShowsModel]:
        """Read the stretches `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    # TODO: Validate
    @staticmethod
    def extract_season(data: ShowsModel) -> int | None:
        """Extract which season the stretch is of, if its menu says."""
        return read_seasons(data.raw_input)[1]

    # TODO: Validate
    @staticmethod
    def extract_season_endpoints(data: ShowsModel) -> list[dict[str, Any]]:
        """Extract what each season but the open one is asked for by.

        A show of more than one season is one playlist with a menu over it, and
        opening it answers with whichever season the menu starts on, so the rest
        are each their own thing to ask browse for.
        """
        menu, open_season = read_seasons(data.raw_input)
        return [
            endpoint
            for number, endpoint in sorted(menu.items())
            if number != open_season
        ]

    # TODO: Validate
    @staticmethod
    def extract_episode_ids(data: ShowsModel) -> list[str]:
        """Extract the id of every episode the stretch listed, in its order."""
        return [
            entry["videoId"]
            for entry in find(data.raw_input, "playlistVideoRenderer")
            if "videoId" in entry
        ]

    # TODO: Validate
    @staticmethod
    def extract_continuation(data: ShowsModel) -> str | None:
        """Extract what the stretch after this one is asked for by."""
        return read_continuation(data.raw_input)

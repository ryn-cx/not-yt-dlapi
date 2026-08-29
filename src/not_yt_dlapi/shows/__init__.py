# TODO: Validate
"""Contains the Shows class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, overload
from urllib.parse import parse_qs, urlsplit

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.shows.models import ShowsModel, SubMenuItem, model_validate_json
from not_yt_dlapi.utils import find, read_continuation

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
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[ShowsModel]:
        """Read the stretches `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    # TODO: Validate
    @classmethod
    def extract_season(cls, data: ShowsModel) -> int | None:
        """Extract which season the stretch is of, if its menu says."""
        return next(
            (
                number
                for menu_item in cls._season_menu_items(data)
                if menu_item.selected
                for number in [cls._season_number(menu_item)]
                if number is not None
            ),
            None,
        )

    # TODO: Validate
    @classmethod
    def extract_season_endpoints(cls, data: ShowsModel) -> list[dict[str, Any]]:
        """Extract what each season but the open one is asked for by.

        A show of more than one season is one playlist with a menu over it, and
        opening it answers with whichever season the menu starts on, so the rest
        are each their own thing to ask browse for.
        """
        seasons = {
            number: menu_item
            for menu_item in cls._season_menu_items(data)
            for number in [cls._season_number(menu_item)]
            if number is not None
        }
        open_season = cls.extract_season(data)
        return [
            {"browseId": endpoint.browse_id}
            if endpoint.params is None
            else {"browseId": endpoint.browse_id, "params": endpoint.params}
            for number, menu_item in sorted(seasons.items())
            if number != open_season
            for endpoint in [menu_item.navigation_endpoint.browse_endpoint]
        ]

    # A season is chosen from the same menu a playlist is sorted from, so what
    # tells the two apart is that a season says which season it is, and it says so
    # in the address a person would read it at rather than in the endpoint browse
    # is asked by.
    # TODO: Validate
    @staticmethod
    def _season_number(menu_item: SubMenuItem) -> int | None:
        address = menu_item.navigation_endpoint.command_metadata.web_command_metadata
        numbers = parse_qs(urlsplit(address.url).query).get("season", ())
        if not numbers or not numbers[0].isdigit():
            return None
        return int(numbers[0])

    # TODO: Validate
    @staticmethod
    def _season_menu_items(data: ShowsModel) -> list[SubMenuItem]:
        if data.contents is None:
            return []
        return [
            menu_item
            for tab in data.contents.two_column_browse_results_renderer.tabs
            for section in tab.tab_renderer.content.section_list_renderer.contents
            for item in section.item_section_renderer.contents
            if item.playlist_show_metadata_renderer is not None
            for menu_item in (
                item.playlist_show_metadata_renderer.collection.sort_filter_sub_menu_renderer.sub_menu_items
            )
        ]

    # TODO: Validate
    @staticmethod
    def extract_episode_ids(data: ShowsModel) -> list[str]:
        """Extract the id of every episode the stretch listed, in its order.

        A stretch that carries a season on is answered in a shape no recorded
        response holds, so the episodes are read out of the answer itself rather
        than off the model until one is recorded.
        """
        return [
            entry["videoId"]
            for entry in find(data.raw_input, "playlistVideoRenderer")
            if "videoId" in entry
        ]

    # TODO: Validate
    @staticmethod
    def extract_continuation(data: ShowsModel) -> str | None:
        """Extract what the stretch after this one is asked for by.

        No recorded response holds a token, so it is read out of the answer
        itself rather than off the model until one is recorded.
        """
        return read_continuation(data.raw_input)

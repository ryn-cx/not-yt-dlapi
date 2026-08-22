# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.shows import Shows
from not_yt_dlapi.shows.models import Show
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

SHOW_ID = "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw"
"""Every season of a show, each holding the episodes listed under it."""


# TODO: Validate
class TestList(RecordedEndpoint):
    ENDPOINT = Shows
    MODEL = Show
    PLAYLIST_IDS = (
        pytest.param(SHOW_ID, id="show"),
        # Hell's Kitchen has run for over twenty years and YouTube carries three
        # of them, numbered the way the show numbers them, so the first season
        # of what comes back is season twenty-one.
        # https://www.youtube.com/show/SC76ETXKYZoiPWiG6TLxkBLA
        pytest.param(
            "TVSHI1FGTrUgFn4lRj_kLDPqR3ZC_PDpPGEPg",
            id="seasons not from one",
        ),
        # Every episode of Jimmy Neutron has to be bought, so none of them is
        # watched from the listing and none says which playlist it was listed
        # under.
        # https://www.youtube.com/show/SC9aXZwJfzfg0g7pZ6ird15g
        pytest.param(
            "TVSHCFpW6hsYe_06P5Sd9mkBTxy6rln4_No8A",
            id="bought show",
        ),
        # The same show opened by the id its page is at rather than by its
        # playlist id, which browse takes as it stands.
        pytest.param("SC9aXZwJfzfg0g7pZ6ird15g", id="bought show by page id"),
    )

    SECOND_SEASON = f"{SHOW_ID}_season_2"
    """The season after the one the show's menu opens on."""

    # TODO: Validate
    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_download(self, client: NotYTDLAPI, playlist_id: str) -> None:
        self.download_test(playlist_id, lambda: client.shows.list(playlist_id))

    # TODO: Validate
    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_parse(self, playlist_id: str) -> None:
        self.parse_test(playlist_id)

    # TODO: Validate
    def test_download_second_season(self, client: NotYTDLAPI) -> None:
        # A season is asked for by the entry the menu carries for it rather than
        # by its number, so the entry is read out of the show's own recording
        # and there is nothing to ask with until that download has been made.
        opened = Show.from_response(self.dumped_file_content(SHOW_ID))
        season = next(link for link in opened.seasons if not link.selected)
        self.download_test(
            self.SECOND_SEASON,
            lambda: client.shows.list(season=season),
        )

    # TODO: Validate
    def test_parse_second_season(self) -> None:
        self.parse_test(self.SECOND_SEASON)

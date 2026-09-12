# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

SHOW_ID = "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw"
"""Every season of a show, each holding the episodes listed under it."""

SECOND_SEASON = 2
"""The season after the one the show's menu opens on."""

PLAYLIST_IDS = [
    pytest.param(SHOW_ID, id="show"),
    # Hell's Kitchen has run for over twenty years and YouTube carries three of
    # them, numbered the way the show numbers them, so the first season of what
    # comes back is season twenty-one.
    # https://www.youtube.com/show/SC76ETXKYZoiPWiG6TLxkBLA
    pytest.param("TVSHI1FGTrUgFn4lRj_kLDPqR3ZC_PDpPGEPg", id="seasons not from one"),
    # Every episode of Jimmy Neutron has to be bought, so none of them is
    # watched from the listing and none says which playlist it was listed under.
    # https://www.youtube.com/show/SC9aXZwJfzfg0g7pZ6ird15g
    pytest.param("TVSHCFpW6hsYe_06P5Sd9mkBTxy6rln4_No8A", id="bought show"),
    # The same show opened by the id its page is at rather than by its playlist
    # id, which browse takes as it stands.
    pytest.param("SC9aXZwJfzfg0g7pZ6ird15g", id="bought show by page id"),
]


# TODO: Validate
@pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
def test_download(client: NotYTDLAPI, playlist_id: str) -> None:
    show = client.shows(playlist_id)
    assert client.shows.extract_episode_ids(show)


# TODO: Validate
def test_download_second_season(client: NotYTDLAPI) -> None:
    # A season is asked for by the browse endpoint the menu carries for it
    # rather than by its number.
    endpoint = client.shows.extract_season_endpoints(client.shows(SHOW_ID))[0]
    season = client.shows(season=endpoint)
    assert client.shows.extract_season(season) == SECOND_SEASON

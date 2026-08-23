# TODO: Validate
"""Rebuilds ShowsModel."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI as Client

PLAYLIST_IDS = [
    "SC9aXZwJfzfg0g7pZ6ird15g",
    "TVSHCFpW6hsYe_06P5Sd9mkBTxy6rln4_No8A",
    "TVSHI1FGTrUgFn4lRj_kLDPqR3ZC_PDpPGEPg",
    "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw",
]

MENU_SHOW_ID = "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw"
"""The show whose menu holds more than one season."""

SECOND_SEASON = f"{MENU_SHOW_ID}_season_2"
"""The season after the one that show's menu opens on."""


# TODO: Validate
def second_season_endpoint(client: Client) -> dict[str, Any]:
    """Return what browse asks the season after the open one for."""
    return client.shows.extract_season_endpoints(client.shows(MENU_SHOW_ID))[0]


# TODO: Validate
def generate_shows(client: NotYTDLAPI) -> None:
    """Rebuild ShowsModel."""
    for playlist_id in PLAYLIST_IDS:
        download_if_missing(
            FILES_PATH,
            "ShowsModel",
            playlist_id,
            lambda playlist_id=playlist_id: client.shows.download(playlist_id),
        )
    download_if_missing(
        FILES_PATH,
        "ShowsModel",
        SECOND_SEASON,
        lambda: client.shows.download(season=second_season_endpoint(client)),
    )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "ShowsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_shows(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

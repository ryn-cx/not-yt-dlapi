# TODO: Validate
"""Rebuilds ShowsModel."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from get_around import build_client_automatically, get_credential

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from not_yt_dlapi import NotYTDLAPI

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI as Client

SHOW_REQUESTS = load_ids("ShowsModel")
"""What each recording of a shows response was downloaded with.

`season_index` asks for a season the show's menu lists rather than the one
opening it answers with.
"""


# TODO: Validate
def download_show(client: Client, playlist_id: str, season_index: int | None) -> str:
    """Download the show, or the season its menu lists at that index."""
    if season_index is None:
        return client.shows.download(playlist_id)
    seasons = client.shows.extract_season_endpoints(client.shows(playlist_id))
    return client.shows.download(season=seasons[season_index])


# TODO: Validate
def generate_shows(client: NotYTDLAPI) -> None:
    """Rebuild ShowsModel."""
    for name, arguments in SHOW_REQUESTS.items():
        download_if_missing(
            FILES_PATH,
            "ShowsModel",
            name,
            lambda arguments=arguments: download_show(
                client,
                arguments["playlist_id"],
                arguments.get("season_index"),
            ),
        )
    rebuild_model(FILES_PATH, NOT_YT_DLAPI_PATH, "ShowsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_shows(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

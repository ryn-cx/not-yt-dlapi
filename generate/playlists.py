# TODO: Validate
"""Rebuilds PlaylistsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from not_yt_dlapi import NotYTDLAPI

PLAYLIST_REQUESTS = load_ids("PlaylistsModel")
"""What each recording of a playlists response was downloaded with."""


# TODO: Validate
def generate_playlists(client: NotYTDLAPI) -> None:
    """Rebuild PlaylistsModel."""
    for name, arguments in PLAYLIST_REQUESTS.items():
        download_if_missing(
            FILES_PATH,
            "PlaylistsModel",
            name,
            lambda arguments=arguments: client.playlists.download(**arguments),
        )
    rebuild_model(FILES_PATH, NOT_YT_DLAPI_PATH, "PlaylistsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_playlists(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

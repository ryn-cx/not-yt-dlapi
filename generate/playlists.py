# TODO: Validate
"""Rebuilds PlaylistsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI

PLAYLIST_IDS = [
    "OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8",
    "PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
    "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh",
    "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw",
    "UU4QobU6STFB0P71PMvOGN5A",
]

CHANNEL_IDS = [
    "UC-9-kyTW8ZkZNDHQJ6FgpwQ",
    "UC4QobU6STFB0P71PMvOGN5A",
    "UCYoEbMFACdvkquYH5h31RNA",
    "UClgRkhTL3_hImCAmdLfDE4g",
    "UCtFRv9O2AHqOZjjynzrv-xg",
]

WALKED_PLAYLIST_PAGES = {
    "OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8": 1,
    "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh": 1,
    "UU4QobU6STFB0P71PMvOGN5A": 1,
}
"""How many pages each recorded walk of a set of playlist ids was served."""

WALKED_CHANNEL_PAGES = {"UC4QobU6STFB0P71PMvOGN5A": 1}
"""How many pages each recorded walk of a channel's playlists was served.

A page past the first is asked for by the token the one before it ended with, so
a missing one is taken out of the walk it sits in.
"""


# TODO: Validate
def generate_playlists(client: NotYTDLAPI) -> None:
    """Rebuild PlaylistsModel."""
    for playlist_id in PLAYLIST_IDS:
        download_if_missing(
            FILES_PATH,
            "PlaylistsModel",
            playlist_id,
            lambda playlist_id=playlist_id: client.playlists.download(
                playlist_ids=playlist_id,
            ),
        )
    for channel_id in CHANNEL_IDS:
        download_if_missing(
            FILES_PATH,
            "PlaylistsModel",
            channel_id,
            lambda channel_id=channel_id: client.playlists.download(
                channel_id=channel_id,
            ),
        )
    for playlist_id, page_count in WALKED_PLAYLIST_PAGES.items():
        for page in range(page_count):
            download_if_missing(
                FILES_PATH,
                "PlaylistsModel",
                f"{playlist_id}-page-{page}",
                lambda playlist_id=playlist_id, page=page: (
                    client.playlists.download_all(playlist_ids=[playlist_id])[page]
                ),
            )
    for channel_id, page_count in WALKED_CHANNEL_PAGES.items():
        for page in range(page_count):
            download_if_missing(
                FILES_PATH,
                "PlaylistsModel",
                f"{channel_id}-page-{page}",
                lambda channel_id=channel_id, page=page: client.playlists.download_all(
                    channel_id=channel_id,
                )[page],
            )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "PlaylistsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_playlists(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

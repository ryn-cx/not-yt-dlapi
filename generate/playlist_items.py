# TODO: Validate
"""Rebuilds PlaylistItemsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI

PLAYLIST_IDS = [
    "OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8",
    "PLFgquLnL59alvrcyyOWR6zy-De3GUo-B_",
    "PLHPTxTxtC0iZUB6K7RWdvB7bimNTqbL-O",
    "PLbpi6ZahtOH4kNyb9pjnMYg4PB7qiljiH",
    "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh",
    "PLydZ2Hrp_gPQmh4MSMoUK4H5QPr7AM4bT",
    "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw",
    "UU4QobU6STFB0P71PMvOGN5A",
]

WALKED_PLAYLIST_PAGES = {
    "OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8": 19,
    "PLbpi6ZahtOH4kNyb9pjnMYg4PB7qiljiH": 76,
    "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh": 4,
    "UU4QobU6STFB0P71PMvOGN5A": 1,
}
"""How many pages each recorded walk of a playlist's items was served.

A page past the first is asked for by the token the one before it ended with, so
a missing one is taken out of the walk it sits in.
"""


# TODO: Validate
def generate_playlist_items(client: NotYTDLAPI) -> None:
    """Rebuild PlaylistItemsModel."""
    for playlist_id in PLAYLIST_IDS:
        download_if_missing(
            FILES_PATH,
            "PlaylistItemsModel",
            playlist_id,
            lambda playlist_id=playlist_id: client.playlist_items.download(playlist_id),
        )
    for playlist_id, page_count in WALKED_PLAYLIST_PAGES.items():
        for page in range(page_count):
            download_if_missing(
                FILES_PATH,
                "PlaylistItemsModel",
                f"{playlist_id}-page-{page}",
                lambda playlist_id=playlist_id, page=page: (
                    client.playlist_items.download_all(playlist_id)[page]
                ),
            )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "PlaylistItemsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_playlist_items(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

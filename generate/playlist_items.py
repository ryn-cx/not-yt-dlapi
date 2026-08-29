# TODO: Validate
"""Rebuilds PlaylistItemsModel."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from get_around import build_client_automatically, get_credential

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from not_yt_dlapi import NotYTDLAPI

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI as Client

PLAYLIST_IDS = load_ids("PlaylistItemsModel")


# TODO: Validate
def download_second_page(client: Client, playlist_id: str) -> None:
    """Record the page after the first of a playlist's items.

    The page after the first is the only one holding a previous page token, and
    that token is read off the recorded first page.

    Raises:
        ValueError: If the playlist fits on one page.
    """
    first_page_path = FILES_PATH / "PlaylistItemsModel" / f"{playlist_id}.json"

    def download() -> str:
        page_token = client.playlist_items.load(
            first_page_path.read_text(encoding="utf-8"),
        ).next_page_token
        if page_token is None:
            msg = f"{playlist_id} holds every item on one page."
            raise ValueError(msg)
        return client.playlist_items.download(playlist_id, page_token=page_token)

    download_if_missing(
        FILES_PATH,
        "PlaylistItemsModel",
        f"{playlist_id}-page-2",
        download,
    )


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
    download_second_page(client, PLAYLIST_IDS[0])
    rebuild_model(FILES_PATH, NOT_YT_DLAPI_PATH, "PlaylistItemsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_playlist_items(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

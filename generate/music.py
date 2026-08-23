# TODO: Validate
"""Rebuilds MusicModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI

PLAYLIST_IDS = [
    "OLAK5uy_kiAyq0iiYYIPvqybBkpxFvNai3lAw3fyU",
    "OLAK5uy_lVxq_QCXDlleCnpsszQyiFextilkX12_w",
    "OLAK5uy_mYS5efFtXpNEV9MDDZsGt3LkFJNR02GzY",
]


# TODO: Validate
def generate_music(client: NotYTDLAPI) -> None:
    """Rebuild MusicModel."""
    for playlist_id in PLAYLIST_IDS:
        download_if_missing(
            FILES_PATH,
            "MusicModel",
            playlist_id,
            lambda playlist_id=playlist_id: client.music.download(playlist_id),
        )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "MusicModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_music(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

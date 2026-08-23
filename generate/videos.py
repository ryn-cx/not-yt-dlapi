# TODO: Validate
"""Rebuilds VideosModel."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.videos import MAX_IDS

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI as Client

VIDEO_IDS = [
    "00000000000",
    "6JTFYuloLFM",
    "g1eZjGhN8oo",
    "jNQXAC9IVRw",
    "zKQGAv8gtBA",
]

SEVERAL_VIDEO_IDS = ["jNQXAC9IVRw", "LY8Wi7XRXCA"]
"""The videos asked about in one request, recorded under their ids joined by a plus."""

LONG_PLAYLIST_ID = "PLbpi6ZahtOH4kNyb9pjnMYg4PB7qiljiH"
"""A playlist of more videos than one request takes."""

WALKED_PLAYLIST_PAGES = 72
"""How many pages the recorded walk of that playlist's videos was served.

A page past the first is the next batch of ids rather than a request of its own,
so a missing one is taken out of the walk it sits in.
"""


# TODO: Validate
def long_playlist_video_ids(client: Client) -> list[str]:
    """Return the id of every video in the long playlist."""
    pages = client.playlist_items.download_all(LONG_PLAYLIST_ID)
    return [
        item.content_details.video_id
        for item in client.playlist_items.extract_items(pages)
    ]


# TODO: Validate
def generate_videos(client: NotYTDLAPI) -> None:
    """Rebuild VideosModel."""
    for video_id in VIDEO_IDS:
        download_if_missing(
            FILES_PATH,
            "VideosModel",
            video_id,
            lambda video_id=video_id: client.videos.download(video_id),
        )
    download_if_missing(
        FILES_PATH,
        "VideosModel",
        "+".join(SEVERAL_VIDEO_IDS),
        lambda: client.videos.download(SEVERAL_VIDEO_IDS),
    )
    download_if_missing(
        FILES_PATH,
        "VideosModel",
        f"{LONG_PLAYLIST_ID}-{MAX_IDS}",
        lambda: client.videos.download(long_playlist_video_ids(client)[:MAX_IDS]),
    )
    for page in range(WALKED_PLAYLIST_PAGES):
        download_if_missing(
            FILES_PATH,
            "VideosModel",
            f"{LONG_PLAYLIST_ID}-page-{page}",
            lambda page=page: client.videos.download_all(
                long_playlist_video_ids(client),
            )[page],
        )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "VideosModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_videos(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

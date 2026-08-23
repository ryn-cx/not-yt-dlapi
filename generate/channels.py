# TODO: Validate
"""Rebuilds ChannelsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI

CHANNEL_IDS = [
    "UC4QobU6STFB0P71PMvOGN5A",
    "UCCCCCCCCCCCCCCCCCCCCCCC",
    "UCYoEbMFACdvkquYH5h31RNA",
    "UCooTDYkIERWBwDC1JKyoElQ",
]

CHANNEL_HANDLES = ["@jawed"]

CHANNEL_USERNAMES = ["jawed"]


# TODO: Validate
def generate_channels(client: NotYTDLAPI) -> None:
    """Rebuild ChannelsModel."""
    for channel_id in CHANNEL_IDS:
        download_if_missing(
            FILES_PATH,
            "ChannelsModel",
            channel_id,
            lambda channel_id=channel_id: client.channels.download(
                channel_id=channel_id,
            ),
        )
    for channel_handle in CHANNEL_HANDLES:
        download_if_missing(
            FILES_PATH,
            "ChannelsModel",
            channel_handle,
            lambda channel_handle=channel_handle: client.channels.download(
                channel_handle=channel_handle,
            ),
        )
    for channel_username in CHANNEL_USERNAMES:
        download_if_missing(
            FILES_PATH,
            "ChannelsModel",
            channel_username,
            lambda channel_username=channel_username: client.channels.download(
                channel_username=channel_username,
            ),
        )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "ChannelsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_channels(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

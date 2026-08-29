# TODO: Validate
"""Rebuilds ChannelsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from not_yt_dlapi import NotYTDLAPI

CHANNEL_REQUESTS = load_ids("ChannelsModel")
"""What each recording of a channels response was downloaded with."""


# TODO: Validate
def generate_channels(client: NotYTDLAPI) -> None:
    """Rebuild ChannelsModel."""
    for name, arguments in CHANNEL_REQUESTS.items():
        download_if_missing(
            FILES_PATH,
            "ChannelsModel",
            name,
            lambda arguments=arguments: client.channels.download(**arguments),
        )
    rebuild_model(FILES_PATH, NOT_YT_DLAPI_PATH, "ChannelsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_channels(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

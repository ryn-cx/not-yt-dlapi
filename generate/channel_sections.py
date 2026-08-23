# TODO: Validate
"""Rebuilds ChannelSectionsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI

CHANNEL_IDS = ["UC4QobU6STFB0P71PMvOGN5A", "UCooTDYkIERWBwDC1JKyoElQ"]


# TODO: Validate
def generate_channel_sections(client: NotYTDLAPI) -> None:
    """Rebuild ChannelSectionsModel."""
    for channel_id in CHANNEL_IDS:
        download_if_missing(
            FILES_PATH,
            "ChannelSectionsModel",
            channel_id,
            lambda channel_id=channel_id: client.channel_sections.download(channel_id),
        )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "ChannelSectionsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_channel_sections(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

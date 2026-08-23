# TODO: Validate
"""Rebuilds TopicModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing
from not_yt_dlapi import NotYTDLAPI

CHANNEL_IDS = ["UCooTDYkIERWBwDC1JKyoElQ"]

WALKED_CHANNEL_PAGES = {"UCooTDYkIERWBwDC1JKyoElQ": 3}
"""How many stretches the recorded walk of each channel's releases was served.

A stretch past the first is asked for by the token the one before it ended with,
so a missing one is taken out of the walk it sits in.
"""


# TODO: Validate
def generate_topic(client: NotYTDLAPI) -> None:
    """Rebuild TopicModel."""
    for channel_id in CHANNEL_IDS:
        download_if_missing(
            FILES_PATH,
            "TopicModel",
            channel_id,
            lambda channel_id=channel_id: client.topic.download(channel_id),
        )
    for channel_id, page_count in WALKED_CHANNEL_PAGES.items():
        for page in range(page_count):
            download_if_missing(
                FILES_PATH,
                "TopicModel",
                f"{channel_id}-page-{page}",
                lambda channel_id=channel_id, page=page: client.topic.download_all(
                    channel_id,
                )[page],
            )
    generate_model(FILES_PATH, NOT_YT_DLAPI_PATH, "TopicModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_topic(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

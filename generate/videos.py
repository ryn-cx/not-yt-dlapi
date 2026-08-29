# TODO: Validate
"""Rebuilds VideosModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from not_yt_dlapi import NotYTDLAPI

VIDEO_REQUESTS = load_ids("VideosModel")
"""The ids each recording of a videos response was downloaded with."""


# TODO: Validate
def generate_videos(client: NotYTDLAPI) -> None:
    """Rebuild VideosModel."""
    for name, arguments in VIDEO_REQUESTS.items():
        download_if_missing(
            FILES_PATH,
            "VideosModel",
            name,
            lambda arguments=arguments: client.videos.download(**arguments),
        )
    rebuild_model(FILES_PATH, NOT_YT_DLAPI_PATH, "VideosModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_videos(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

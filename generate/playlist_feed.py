# TODO: Validate
"""Rebuilds PlaylistFeedModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.feed import read_feed

PLAYLIST_IDS = load_ids("PlaylistFeedModel")

FEED_SUFFIX = ".xml"
"""A feed is served as XML and recorded as it was served."""


# TODO: Validate
def generate_playlist_feed(client: NotYTDLAPI) -> None:
    """Rebuild PlaylistFeedModel."""
    for playlist_id in PLAYLIST_IDS:
        download_if_missing(
            FILES_PATH,
            "PlaylistFeedModel",
            playlist_id,
            lambda playlist_id=playlist_id: client.playlist_feed.download(playlist_id),
            FEED_SUFFIX,
        )
    rebuild_model(FILES_PATH, NOT_YT_DLAPI_PATH, "PlaylistFeedModel", read_feed)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_playlist_feed(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

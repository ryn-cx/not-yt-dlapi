# TODO: Validate
"""Rebuilds TopicModel."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from get_around import build_client_automatically, get_credential

from generate.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from not_yt_dlapi import NotYTDLAPI

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI as Client

CHANNEL_IDS = load_ids("TopicModel")


# TODO: Validate
def download_second_stretch(client: Client, channel_id: str) -> None:
    """Record the stretch after the one opening the channel answers with.

    A token is minted per response, so it is read off the recorded first stretch
    rather than written down in the ids file.

    Raises:
        ValueError: If the channel lists everything in one stretch.
    """
    opened_path = FILES_PATH / "TopicModel" / f"{channel_id}.json"

    def download() -> str:
        continuation = client.topic.extract_continuation(
            client.topic.load(opened_path.read_text(encoding="utf-8")),
        )
        if continuation is None:
            msg = f"{channel_id} lists every release in one stretch."
            raise ValueError(msg)
        return client.topic.download(continuation=continuation)

    download_if_missing(FILES_PATH, "TopicModel", f"{channel_id}-page-2", download)


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
    download_second_stretch(client, CHANNEL_IDS[0])
    rebuild_model(FILES_PATH, NOT_YT_DLAPI_PATH, "TopicModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_topic(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

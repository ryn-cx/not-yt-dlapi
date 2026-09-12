from __future__ import annotations

import logging
from typing import override

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.feed import extract_feed

MODEL_NAME = "ChannelFeedModel"


# TODO: Validate
FEED_SUFFIX = ".xml"


# TODO: Validate
class ChannelFeedId(RecordingId[NotYTDLAPI]):
    channel_id: str

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        return client.channel_feed.download(self.channel_id)


CHANNEL_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ChannelFeedId)


# TODO: Validate
def generate_channel_feed(client: NotYTDLAPI) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CHANNEL_IDS, client, FEED_SUFFIX)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ChannelFeedId, extract_feed)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_channel_feed(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

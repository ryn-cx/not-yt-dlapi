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

MODEL_NAME = "ChannelsModel"


# TODO: Validate
class ChannelsId(RecordingId[NotYTDLAPI]):
    written_as_fields = True

    channel_id: str

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        return client.channels.download(**self.model_dump(exclude_unset=True))


CHANNEL_REQUESTS = load_ids(GENERATOR_PATHS, MODEL_NAME, ChannelsId)


# TODO: Validate
def generate_channels(client: NotYTDLAPI) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CHANNEL_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ChannelsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_channels(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

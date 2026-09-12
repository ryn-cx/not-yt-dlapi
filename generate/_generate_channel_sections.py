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

MODEL_NAME = "ChannelSectionsModel"


# TODO: Validate
class ChannelSectionsId(RecordingId[NotYTDLAPI]):
    channel_id: str

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        return client.channel_sections.download(self.channel_id)


CHANNEL_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ChannelSectionsId)


# TODO: Validate
def generate_channel_sections(client: NotYTDLAPI) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CHANNEL_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ChannelSectionsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_channel_sections(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

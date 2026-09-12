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

MODEL_NAME = "TopicModel"


# TODO: Validate
class TopicId(RecordingId[NotYTDLAPI]):
    channel_id: str
    page: int | None = None

    # TODO: Validate
    @override
    def recording_name(self) -> str:
        if self.page is None:
            return self.channel_id
        return f"{self.channel_id}-page-{self.page}"

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        if self.page is None:
            return client.topic.download(self.channel_id)
        opened_path = GENERATOR_PATHS.recorded_path(MODEL_NAME, self.channel_id)
        continuation = client.topic.extract_continuation(
            client.topic.load(opened_path.read_text(encoding="utf-8")),
        )
        if continuation is None:
            msg = f"{self.channel_id} lists every release in one stretch."
            raise ValueError(msg)
        return client.topic.download(continuation=continuation)


CHANNEL_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, TopicId)


# TODO: Validate
def generate_topic(client: NotYTDLAPI) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CHANNEL_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TopicId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_topic(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

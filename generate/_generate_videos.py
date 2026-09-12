from __future__ import annotations

import logging
from typing import override

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from not_yt_dlapi import NotYTDLAPI

MODEL_NAME = "VideosModel"


# TODO: Validate
class VideosId(RecordingId[NotYTDLAPI]):
    written_as_fields = True

    video_ids: list[str] | str

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        return client.videos.download(**self.model_dump(exclude_unset=True))


VIDEO_REQUESTS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, VideosId)


# TODO: Validate
def generate_videos(client: NotYTDLAPI) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, VIDEO_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, VideosId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_videos(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

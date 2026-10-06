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

MODEL_NAME = "VideosModel"


# TODO: Validate
class VideosId(RecordingId[NotYTDLAPI]):
    written_as_fields = True

    video_ids: list[str] | str

    # TODO: Validate
    @override
    def recording_name(self) -> str:
        """Name a batch of videos after its first video and the count."""
        if isinstance(self.video_ids, str):
            return self.video_ids
        return f"{self.video_ids[0]} +{len(self.video_ids) - 1}"

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        return client.videos.download(**self.model_dump(exclude_unset=True))


VIDEO_REQUESTS = load_ids(GENERATOR_PATHS, MODEL_NAME, VideosId)


# TODO: Validate
def generate_videos(client: NotYTDLAPI) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, VIDEO_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, VideosId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_videos(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

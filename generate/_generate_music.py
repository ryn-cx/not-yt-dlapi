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

MODEL_NAME = "MusicModel"


# TODO: Validate
class MusicId(RecordingId[NotYTDLAPI]):
    playlist_id: str

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        return client.music.download(self.playlist_id)


PLAYLIST_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, MusicId)


# TODO: Validate
def generate_music(client: NotYTDLAPI) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, PLAYLIST_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, MusicId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_music(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

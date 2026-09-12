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

MODEL_NAME = "PlaylistsModel"


# TODO: Validate
class PlaylistsId(RecordingId[NotYTDLAPI]):
    written_as_fields = True

    playlist_ids: str | None = None
    channel_id: str | None = None

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        return client.playlists.download(**self.model_dump(exclude_unset=True))


PLAYLIST_REQUESTS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, PlaylistsId)


# TODO: Validate
def generate_playlists(client: NotYTDLAPI) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, PLAYLIST_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, PlaylistsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_playlists(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

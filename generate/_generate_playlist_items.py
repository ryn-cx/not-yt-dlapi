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

MODEL_NAME = "PlaylistItemsModel"


# TODO: Validate
class PlaylistItemsId(RecordingId[NotYTDLAPI]):
    playlist_id: str
    page: int | None = None

    # TODO: Validate
    @override
    def recording_name(self) -> str:
        if self.page is None:
            return self.playlist_id
        return f"{self.playlist_id}-page-{self.page}"

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        if self.page is None:
            return client.playlist_items.download(self.playlist_id)
        first_page_path = GENERATOR_PATHS.recorded_path(MODEL_NAME, self.playlist_id)
        page_token = client.playlist_items.load(
            first_page_path.read_text(encoding="utf-8"),
        ).next_page_token
        if page_token is None:
            msg = f"{self.playlist_id} holds every item on one page."
            raise ValueError(msg)
        return client.playlist_items.download(self.playlist_id, page_token=page_token)


PLAYLIST_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, PlaylistItemsId)


# TODO: Validate
def generate_playlist_items(client: NotYTDLAPI) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, PLAYLIST_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, PlaylistItemsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_playlist_items(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

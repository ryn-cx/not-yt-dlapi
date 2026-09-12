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

MODEL_NAME = "ShowsModel"


# TODO: Validate
class ShowsId(RecordingId[NotYTDLAPI]):
    written_as_fields = True

    playlist_id: str
    season_index: int | None = None

    # TODO: Validate
    @override
    def download(self, client: NotYTDLAPI) -> str:
        if self.season_index is None:
            return client.shows.download(self.playlist_id)
        seasons = client.shows.extract_season_endpoints(client.shows(self.playlist_id))
        return client.shows.download(season=seasons[self.season_index])


SHOW_REQUESTS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, ShowsId)


# TODO: Validate
def generate_shows(client: NotYTDLAPI) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, SHOW_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ShowsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_shows(
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

# TODO: Validate
import json
import os

import pytest
from get_around import build_client_automatically

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import NoContentError

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

client = NotYTDLAPI(
    api_key=API_KEY,
    get_around_client=build_client_automatically(),
)

VIDEO_ID = "jNQXAC9IVRw"
"""video_id of "Me at the zoo"."""
AGE_RESTRICTED_VIDEO_ID = "l1ITP7m6R0Q"
"""video_id of an age-restricted video."""
SECOND_VIDEO_ID = "S-8U4lSEq8A"
"""video_id of a second video, used for multi-video requests."""
INVALID_VIDEO_ID = "12345678901"


class TestVideos:
    @pytest.mark.parametrize(
        "video_id",
        [VIDEO_ID, AGE_RESTRICTED_VIDEO_ID],
        ids=[f"{VIDEO_ID=}", f"{AGE_RESTRICTED_VIDEO_ID=}"],
    )
    def test_get(self, video_id: str) -> None:
        endpoint = client.videos
        model = endpoint.get(video_id)
        assert any(item.id == video_id for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_multiple(self) -> None:
        endpoint = client.videos
        models = endpoint.get_multiple([VIDEO_ID, SECOND_VIDEO_ID])
        returned_ids = {item.id for model in models for item in model.items}
        assert {VIDEO_ID, SECOND_VIDEO_ID} <= returned_ids
        for model in models:
            endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.videos.get(INVALID_VIDEO_ID)
        assert error.value.response

    def test_parse(self) -> None:
        endpoint = client.videos
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

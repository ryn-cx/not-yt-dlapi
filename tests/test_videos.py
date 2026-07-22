# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from not_yt_dlapi.exceptions import VideoNotFoundError
from tests.utils import (
    assert_error,
    download_and_save,
    page_dicts,
    page_models,
    parse_json,
    single_dict,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from not_yt_dlapi import NotYTDLAPI
    from not_yt_dlapi.video import Videos
    from not_yt_dlapi.video.models import VideosModel

# The input shapes extract_items accepts.
type ExtractInput = (
    VideosModel | dict[str, Any] | list[VideosModel] | list[dict[str, Any]]
)


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> Videos:
    return client.videos


# TODO: Find a private video for testing.
VIDEO_ID = "jNQXAC9IVRw"
VIDEO_ID_2 = "LY8Wi7XRXCA"
VIDEO_ID_3 = "5ahp-nKTM8w"
VIDEO_ID_4 = "h06djUQqIEA"
# This is probably the age restricted video with the most views on YouTube.
AGE_RESTRICTED_VIDEO_ID = "qpgTC9MDx1o"
INVALID_VIDEO_ID = "00000000000"

VIDEO_IDS: list[str] = [
    VIDEO_ID,
    AGE_RESTRICTED_VIDEO_ID,
    VIDEO_ID_2,
    VIDEO_ID_3,
    VIDEO_ID_4,
]


class TestVideoId:
    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_download(self, endpoint: Videos, video_id: str) -> None:
        download_and_save(
            endpoint,
            video_id,
            lambda: endpoint.download([video_id]),
        )

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_parse(self, endpoint: Videos, video_id: str) -> None:
        data = parse_json(endpoint, video_id)
        assert [item.id for item in data.items] == [video_id]

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    @pytest.mark.parametrize(
        "load",
        [single_dict, parse_json, page_dicts, page_models],
        ids=["dict", "model", "dicts", "models"],
    )
    def test_extract_items(
        self,
        endpoint: Videos,
        video_id: str,
        load: Callable[[Videos, str], ExtractInput],
    ) -> None:
        items = endpoint.extract_items(load(endpoint, video_id))
        assert [item.id for item in items] == [video_id]

    def test_invalid_download(self, endpoint: Videos) -> None:
        assert_error(
            endpoint,
            INVALID_VIDEO_ID,
            lambda: endpoint.download([INVALID_VIDEO_ID]),
            VideoNotFoundError,
        )

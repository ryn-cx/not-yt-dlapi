# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import (
    assert_no_content_error,
    data_path,
    download_if_missing,
)

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI
    from not_yt_dlapi.video import Videos

VIDEO_ID = "jNQXAC9IVRw"
"""video_id of "Me at the zoo"."""
AGE_RESTRICTED_VIDEO_ID = "l1ITP7m6R0Q"
"""video_id of an age-restricted video."""
SECOND_VIDEO_ID = "S-8U4lSEq8A"
"""video_id of a second video, used for multi-video requests."""
INVALID_VIDEO_ID = "12345678901"

VIDEO_IDS = [VIDEO_ID, AGE_RESTRICTED_VIDEO_ID, SECOND_VIDEO_ID]


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> Videos:
    return client.videos


class TestVideos:
    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_download(self, endpoint: Videos, video_id: str) -> None:
        download_if_missing(
            endpoint,
            video_id,
            lambda: endpoint.download(video_id),
        )

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_value(self, endpoint: Videos, video_id: str) -> None:
        data = endpoint.parse(json.loads(data_path(endpoint, video_id).read_text()))
        # TODO: assert expected value (needs live data)
        assert data is not None

    def test_invalid(self, endpoint: Videos) -> None:
        name = INVALID_VIDEO_ID
        assert_no_content_error(
            endpoint,
            name,
            lambda: endpoint.get(INVALID_VIDEO_ID),
        )

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
    from not_yt_dlapi.playlists import Playlists

CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"
"""channel_id of the YouTube channel that owns "Me at the zoo"."""
YOUTUBE_CHANNEL_ID = "UCBR8-60-B28hp2BmDPdntcQ"
"""channel_id of the official YouTube channel."""
INVALID_CHANNEL_ID = "UCinvalidchannelid123456"

CHANNEL_IDS = [CHANNEL_ID, YOUTUBE_CHANNEL_ID]


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> Playlists:
    return client.playlists


class TestPlaylists:
    @pytest.mark.parametrize("channel_id", CHANNEL_IDS)
    def test_download(self, endpoint: Playlists, channel_id: str) -> None:
        download_if_missing(
            endpoint,
            channel_id,
            lambda: endpoint.download(channel_id),
        )

    @pytest.mark.parametrize("channel_id", CHANNEL_IDS)
    def test_value(self, endpoint: Playlists, channel_id: str) -> None:
        data = endpoint.parse(json.loads(data_path(endpoint, channel_id).read_text()))
        # TODO: assert expected value (needs live data)
        assert data is not None

    def test_invalid(self, endpoint: Playlists) -> None:
        name = INVALID_CHANNEL_ID
        assert_no_content_error(
            endpoint,
            name,
            lambda: endpoint.get(INVALID_CHANNEL_ID),
        )

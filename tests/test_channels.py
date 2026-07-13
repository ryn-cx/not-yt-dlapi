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
    from not_yt_dlapi.channel import Channels

CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"
"""channel_id of the YouTube channel that owns "Me at the zoo"."""
CHANNEL_HANDLE = "@Google"
"""Handle of the Google channel."""
CHANNEL_USERNAME = "MrBeast"
"""Legacy username of the MrBeast channel."""
INVALID_CHANNEL_ID = "UCinvalidchannelid123456"

# Each lookup is (cache name, download kwargs) so a single id downloads via the
# matching channel_id/handle/username parameter.
LOOKUPS: list[tuple[str, dict[str, str]]] = [
    (CHANNEL_ID, {"channel_id": CHANNEL_ID}),
    (CHANNEL_HANDLE, {"handle": CHANNEL_HANDLE}),
    (CHANNEL_USERNAME, {"username": CHANNEL_USERNAME}),
]

LOOKUP_NAMES = [name for name, _ in LOOKUPS]


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> Channels:
    return client.channels


class TestChannels:
    @pytest.mark.parametrize(("name", "kwargs"), LOOKUPS)
    def test_download(
        self,
        endpoint: Channels,
        name: str,
        kwargs: dict[str, str],
    ) -> None:
        download_if_missing(endpoint, name, lambda: endpoint.download(**kwargs))

    @pytest.mark.parametrize("name", LOOKUP_NAMES)
    def test_value(self, endpoint: Channels, name: str) -> None:
        data = endpoint.parse(json.loads(data_path(endpoint, name).read_text()))
        # TODO: assert expected value (needs live data)
        assert data is not None

    def test_invalid(self, endpoint: Channels) -> None:
        name = INVALID_CHANNEL_ID
        assert_no_content_error(
            endpoint,
            name,
            lambda: endpoint.get(channel_id=INVALID_CHANNEL_ID),
        )

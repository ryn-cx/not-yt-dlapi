# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import ChannelNotFoundError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI
    from not_yt_dlapi.channel_section import ChannelSections


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> ChannelSections:
    return client.channel_sections


VALID_CHANNEL_IDS: list[str] = [
    # YouTube channel https://www.youtube.com/user/jawed
    "UC4QobU6STFB0P71PMvOGN5A",
    # Youtube topic https://www.youtube.com/channel/UCooTDYkIERWBwDC1JKyoElQ
    "UCooTDYkIERWBwDC1JKyoElQ",
]
INVALID_CHANNEL_ID = "UCCCCCCCCCCCCCCCCCCCCCCC"


@pytest.mark.parametrize("channel_id", VALID_CHANNEL_IDS, ids=lambda x: x)
def test_download(endpoint: ChannelSections, channel_id: str) -> None:
    download_and_save(
        endpoint,
        channel_id,
        lambda: endpoint.download(channel_id),
    )


@pytest.mark.parametrize("channel_id", VALID_CHANNEL_IDS, ids=lambda x: x)
def test_parse(endpoint: ChannelSections, channel_id: str) -> None:
    channel_sections = parse_json(endpoint, channel_id)
    assert channel_sections.items[0].snippet.channel_id == channel_id


def test_invalid_download(endpoint: ChannelSections) -> None:
    assert_error(
        endpoint,
        INVALID_CHANNEL_ID,
        lambda: endpoint.download(INVALID_CHANNEL_ID),
        ChannelNotFoundError,
    )

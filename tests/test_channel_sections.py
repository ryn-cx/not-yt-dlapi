# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import ChannelNotFoundError

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

CHANNEL_IDS = [
    pytest.param("UC4QobU6STFB0P71PMvOGN5A", id="regular channel"),
    # The current API returns basically nothing for a Topic channel.
    pytest.param("UCooTDYkIERWBwDC1JKyoElQ", id="topic channel"),
]


# TODO: Validate
@pytest.mark.parametrize("channel_id", CHANNEL_IDS)
def test_download(client: NotYTDLAPI, channel_id: str) -> None:
    sections = client.channel_sections(channel_id)
    assert sections.kind == "youtube#channelSectionListResponse"


# TODO: Validate
def test_download_invalid(client: NotYTDLAPI) -> None:
    with pytest.raises(ChannelNotFoundError):
        client.channel_sections.download("UCCCCCCCCCCCCCCCCCCCCCCC")

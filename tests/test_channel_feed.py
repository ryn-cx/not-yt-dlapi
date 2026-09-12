# TODO: Validate
from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import ChannelFeedNotFoundError

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"
"""https://www.youtube.com/@jawed"""


# TODO: Validate
def test_download(client: NotYTDLAPI) -> None:
    feed = client.channel_feed(CHANNEL_ID)
    # The feed writes a channel's id with the leading `UC` taken off.
    assert feed.channel_id == CHANNEL_ID.removeprefix("UC")
    assert feed.entry


# TODO: Validate
def test_download_invalid(client: NotYTDLAPI) -> None:
    with pytest.raises(ChannelFeedNotFoundError) as error:
        client.channel_feed.download("UCCCCCCCCCCCCCCCCCCCCCCC")
    assert error.value.status_code == HTTPStatus.NOT_FOUND

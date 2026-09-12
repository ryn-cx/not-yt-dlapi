# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

FILTERS = [
    pytest.param("channel_id", "UC4QobU6STFB0P71PMvOGN5A", id="regular channel"),
    # The current API returns basically nothing for a Topic channel.
    pytest.param("channel_id", "UCooTDYkIERWBwDC1JKyoElQ", id="topic channel"),
    pytest.param("channel_id", "UCCCCCCCCCCCCCCCCCCCCCCC", id="invalid channel"),
    pytest.param(
        "channel_id",
        "UCYoEbMFACdvkquYH5h31RNA",
        id="channel linked to movie",
    ),
    pytest.param("channel_handle", "@jawed", id="handle"),
    pytest.param("channel_username", "jawed", id="username"),
]


# TODO: Validate
@pytest.mark.parametrize(("filter_name", "filter_value"), FILTERS)
def test_download(client: NotYTDLAPI, filter_name: str, filter_value: str) -> None:
    channels = client.channels(**{filter_name: filter_value})
    assert channels.kind == "youtube#channelListResponse"


# TODO: Validate
def test_download_two_filters(client: NotYTDLAPI) -> None:
    with pytest.raises(ValueError, match="Invalid number of arguments"):
        client.channels.download(
            channel_id="UC4QobU6STFB0P71PMvOGN5A",
            channel_handle="@jawed",
        )


# TODO: Validate
def test_download_no_filters(client: NotYTDLAPI) -> None:
    with pytest.raises(ValueError, match="Invalid number of arguments"):
        client.channels.download()

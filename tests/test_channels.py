# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.channels.models import ChannelsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

FILTERS = [
    pytest.param(("channel_id", "UC4QobU6STFB0P71PMvOGN5A"), id="regular channel"),
    # The current API returns basically nothing for a Topic channel.
    pytest.param(("channel_id", "UCooTDYkIERWBwDC1JKyoElQ"), id="topic channel"),
    pytest.param(("channel_id", "UCCCCCCCCCCCCCCCCCCCCCCC"), id="invalid channel"),
    pytest.param(
        ("channel_id", "UCYoEbMFACdvkquYH5h31RNA"),
        id="channel linked to movie",
    ),
    pytest.param(("channel_handle", "@jawed"), id="handle"),
    pytest.param(("channel_username", "jawed"), id="username"),
]


# TODO: Validate
class ChannelsTest(RecordedEndpoint):
    MODEL = ChannelsModel
    IGNORED = ("ChannelsModel.etag", "Channel.etag")
    SORTED = (
        "ChannelTopicDetails.topic_ids",
        "ChannelTopicDetails.topic_categories",
    )
    SAME_TYPE = (
        "ChannelStatistics.view_count",
        "ChannelStatistics.subscriber_count",
        "ChannelStatistics.video_count",
    )


# TODO: Validate
@pytest.mark.parametrize("channel_filter", FILTERS)
def test_download(client: NotYTDLAPI, channel_filter: tuple[str, str]) -> None:
    filter_name, filter_value = channel_filter
    ChannelsTest.download_test(
        filter_value,
        lambda: client.channels.download(**{filter_name: filter_value}),
    )


# TODO: Validate
@pytest.mark.parametrize("channel_filter", FILTERS)
def test_parse(client: NotYTDLAPI, channel_filter: tuple[str, str]) -> None:
    channel_id = channel_filter[1]
    channels = client.channels.load(ChannelsTest.recorded_content(channel_id))
    assert channels.kind == "youtube#channelListResponse"
    ChannelsTest.parse_test(channel_id)


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

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.channels import Channels
from not_yt_dlapi.channels.models import ChannelFeedResponse, ChannelListResponse
from not_yt_dlapi.exceptions import HTTPError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


class ChannelTest(RecordedEndpoint):
    ENDPOINT = Channels
    IGNORED = ("ChannelListResponse.etag", "Channel.etag")
    SORTED = (
        "ChannelTopicDetails.topic_ids",
        "ChannelTopicDetails.topic_categories",
    )
    SAME_TYPE = (
        "ChannelStatistics.view_count",
        "ChannelStatistics.subscriber_count",
        "ChannelStatistics.video_count",
    )


class TestList(ChannelTest):
    MODEL = ChannelListResponse
    FILTERS = (
        pytest.param(("channel_id", "UC4QobU6STFB0P71PMvOGN5A"), id="regular channel"),
        # The current API returns basically nothing for a Topic channel.
        pytest.param(("channel_id", "UCooTDYkIERWBwDC1JKyoElQ"), id="topic channel"),
        pytest.param(("channel_id", "UCCCCCCCCCCCCCCCCCCCCCCC"), id="invalid channel"),
        pytest.param(("channel_handle", "@jawed"), id="handle"),
        pytest.param(("channel_username", "jawed"), id="username"),
    )

    @pytest.mark.parametrize("channel_filter", FILTERS)
    def test_download(
        self,
        client: NotYTDLAPI,
        channel_filter: tuple[str, str],
    ) -> None:
        filter_name, filter_value = channel_filter
        self.download_test(
            filter_value,
            lambda: client.channels.list(**{filter_name: filter_value}),  # type: ignore[call-overload]
        )

    @pytest.mark.parametrize("channel_filter", FILTERS)
    def test_parse(self, channel_filter: tuple[str, str]) -> None:
        self.parse_test(channel_filter[1])

    def test_two_filters(self, client: NotYTDLAPI) -> None:
        with pytest.raises(ValueError, match="Invalid number of arguments"):
            client.channels.list(  # type: ignore[call-overload] # ty: ignore[no-matching-overload]
                channel_id="UC4QobU6STFB0P71PMvOGN5A",
                channel_handle="@jawed",
            )

    def test_no_filters(self, client: NotYTDLAPI) -> None:
        with pytest.raises(ValueError, match="Invalid number of arguments"):
            client.channels.list()  # type: ignore[call-overload] # ty: ignore[no-matching-overload]


class TestFeed(ChannelTest):
    MODEL = ChannelFeedResponse
    IGNORED = ("ChannelFeedResponse.entries", "ChannelFeedResponse.published")
    SUFFIX = ".xml"
    CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"

    def test_download(self, client: NotYTDLAPI) -> None:
        self.download_test(
            self.CHANNEL_ID,
            lambda: client.channels.feed(channel_id=self.CHANNEL_ID),
        )

    def test_parse(self) -> None:
        self.parse_test(self.CHANNEL_ID)

    def test_invalid_id(self, client: NotYTDLAPI) -> None:
        with pytest.raises(HTTPError) as error:
            client.channels.feed(channel_id="UCCCCCCCCCCCCCCCCCCCCCCC")
        assert error.value.status_code == HTTPStatus.NOT_FOUND

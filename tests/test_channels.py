# TODO: Validate
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


# TODO: Validate
class ChannelTest(RecordedEndpoint):
    ENDPOINT = Channels


# TODO: Validate
class TestList:
    """Test `channels.list`."""

    # TODO: Validate
    class TestChannelId(ChannelTest):
        CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.CHANNEL_ID,
                lambda: client.channels.list(channel_id=self.CHANNEL_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.CHANNEL_ID, ChannelListResponse)

    # TODO: Validate
    class TestChannelHandle(ChannelTest):
        """A handle names the same thing an id does, and answers with the channel."""

        HANDLE = "@Google"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.HANDLE,
                lambda: client.channels.list(channel_handle=self.HANDLE).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.HANDLE, ChannelListResponse)

    # TODO: Validate
    class TestChannelUsername(ChannelTest):
        """A username is what a channel was named before handles existed.

        It is not the handle: this is not the channel `@MrBeast` is.
        """

        USERNAME = "MrBeast"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.USERNAME,
                lambda: client.channels.list(channel_username=self.USERNAME).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.USERNAME, ChannelListResponse)

    # TODO: Validate
    class TestUnknownChannel(ChannelTest):
        """An id nothing is under answers with no items at all, rather than refused."""

        CHANNEL_ID = "UCCCCCCCCCCCCCCCCCCCCCCC"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.CHANNEL_ID,
                lambda: client.channels.list(channel_id=self.CHANNEL_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            assert "items" not in self.recorded_content(self.CHANNEL_ID)
            self.parse_test(self.CHANNEL_ID, ChannelListResponse)

    # TODO: Validate
    class TestTooManyFilters:
        """The API takes exactly one of the three ways of naming a channel."""

        # TODO: Validate
        def test_two_filters(self, client: NotYTDLAPI) -> None:
            with pytest.raises(ValueError, match="Invalid number of arguments"):
                client.channels.list(  # ty: ignore[no-matching-overload]
                    channel_id="UC4QobU6STFB0P71PMvOGN5A",
                    channel_handle="@jawed",
                )

        # TODO: Validate
        def test_no_filters(self, client: NotYTDLAPI) -> None:
            with pytest.raises(ValueError, match="Invalid number of arguments"):
                client.channels.list()  # ty: ignore[no-matching-overload]


# TODO: Validate
class TestFeed:
    """Test `channels.feed`."""

    # TODO: Validate
    class TestChannelId(ChannelTest):
        """The feed of a channel that is still uploading.

        A feed cannot be recorded the way a response can. It is the newest
        fifteen videos of a channel that keeps publishing, and every entry
        carries a view count that moves while it is being read, so no two
        downloads of one feed are ever the same document and comparing one
        against a recording would only ever fail.

        So the two tests ask different things of the feed than an API endpoint's
        do. The download test asks whether today's feed still reads into the
        models at all, which is the thing that breaks when YouTube changes the
        document. The recording under `_files` is a frozen sample kept by hand
        rather than written by the test, and the parse test is what holds the
        reading of it still.
        """

        SUFFIX = ".xml"
        """A feed is served as XML, and the recording is the document itself."""

        CHANNEL_ID = "UChqUTb7kYRX8-EiaN3XFrSQ"
        """Reuters https://www.youtube.com/channel/UChqUTb7kYRX8-EiaN3XFrSQ"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            feed = client.channels.feed(channel_id=self.CHANNEL_ID)

            # The feed writes the channel's id without the `UC` it starts with,
            # where every entry in it writes the same id in full.
            assert feed.channel_id == self.CHANNEL_ID.removeprefix("UC")
            assert feed.entries
            assert all(entry.channel_id == self.CHANNEL_ID for entry in feed.entries)

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.CHANNEL_ID, ChannelFeedResponse)

    # TODO: Validate
    class TestUnknownChannel:
        """An id nothing is under is refused, where `list` answers it empty."""

        CHANNEL_ID = "UCCCCCCCCCCCCCCCCCCCCCCC"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            with pytest.raises(HTTPError) as error:
                client.channels.feed(channel_id=self.CHANNEL_ID)
            assert error.value.status_code == HTTPStatus.NOT_FOUND

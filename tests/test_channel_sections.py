# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.channel_sections import ChannelSections
from not_yt_dlapi.channel_sections.models import ChannelSectionListResponse
from not_yt_dlapi.exceptions import NotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class ChannelSectionTest(RecordedEndpoint):
    ENDPOINT = ChannelSections


# TODO: Validate
class TestList:
    """Test `channel_sections.list`."""

    # TODO: Validate
    class TestChannel(ChannelSectionTest):
        """A shelf YouTube titles itself has no title of its own.

        Only a shelf holding something the channel chose has contents.
        """

        CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.CHANNEL_ID,
                lambda: client.channel_sections.list(self.CHANNEL_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.CHANNEL_ID, ChannelSectionListResponse)

    # TODO: Validate
    class TestTopicChannel(ChannelSectionTest):
        """A Topic channel is generated rather than arranged by anybody.

        Its one shelf is of a kind the API has no name for.
        """

        CHANNEL_ID = "UCooTDYkIERWBwDC1JKyoElQ"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.CHANNEL_ID,
                lambda: client.channel_sections.list(self.CHANNEL_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.CHANNEL_ID, ChannelSectionListResponse)

    # TODO: Validate
    class TestUnknownChannel:
        """Unlike the channels endpoint, this one refuses an id nothing is under.

        There is no response to record, only the refusal.
        """

        CHANNEL_ID = "UCCCCCCCCCCCCCCCCCCCCCCC"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            with pytest.raises(NotFoundError) as error:
                client.channel_sections.list(self.CHANNEL_ID)

            assert error.value.code == 404  # noqa: PLR2004 - The status code is the point.
            assert error.value.error["errors"][0]["reason"] == "channelNotFound"

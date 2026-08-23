# TODO: Validate
from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.channel_feed.models import ChannelFeedModel
from not_yt_dlapi.exceptions import ChannelFeedNotFoundError
from not_yt_dlapi.feed import read_feed
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from pydantic import BaseModel

    from not_yt_dlapi import NotYTDLAPI

CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"
"""https://www.youtube.com/@jawed"""


# TODO: Validate
class ChannelFeedTest(RecordedEndpoint):
    MODEL = ChannelFeedModel
    SUFFIX = ".xml"
    # A feed holds the newest fifteen videos, so its entries are replaced as the
    # channel grows.
    IGNORED = ("ChannelFeedModel.entry", "ChannelFeedModel.published")

    # TODO: Validate
    @classmethod
    def load_document(cls, document: str) -> BaseModel:
        """Read one recorded feed, which is XML rather than JSON."""
        return ChannelFeedModel.model_validate(read_feed(document))


# TODO: Validate
def test_download(client: NotYTDLAPI) -> None:
    ChannelFeedTest.download_test(
        CHANNEL_ID,
        lambda: client.channel_feed.download(CHANNEL_ID),
    )


# TODO: Validate
def test_parse(client: NotYTDLAPI) -> None:
    feed = client.channel_feed.load(ChannelFeedTest.recorded_content(CHANNEL_ID))
    # The feed writes a channel's id with the leading `UC` taken off.
    assert feed.channel_id == CHANNEL_ID.removeprefix("UC")
    ChannelFeedTest.parse_test(CHANNEL_ID)


# TODO: Validate
def test_download_invalid(client: NotYTDLAPI) -> None:
    with pytest.raises(ChannelFeedNotFoundError) as error:
        client.channel_feed.download("UCCCCCCCCCCCCCCCCCCCCCCC")
    assert error.value.status_code == HTTPStatus.NOT_FOUND

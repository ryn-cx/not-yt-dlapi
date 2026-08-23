# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.channel_sections.models import ChannelSectionsModel
from not_yt_dlapi.exceptions import ChannelNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

CHANNEL_IDS = [
    pytest.param("UC4QobU6STFB0P71PMvOGN5A", id="regular channel"),
    # The current API returns basically nothing for a Topic channel.
    pytest.param("UCooTDYkIERWBwDC1JKyoElQ", id="topic channel"),
]


# TODO: Validate
class ChannelSectionsTest(RecordedEndpoint):
    MODEL = ChannelSectionsModel
    IGNORED = ("ChannelSectionsModel.etag", "ChannelSection.etag")


# TODO: Validate
@pytest.mark.parametrize("channel_id", CHANNEL_IDS)
def test_download(client: NotYTDLAPI, channel_id: str) -> None:
    ChannelSectionsTest.download_test(
        channel_id,
        lambda: client.channel_sections.download(channel_id),
    )


# TODO: Validate
@pytest.mark.parametrize("channel_id", CHANNEL_IDS)
def test_parse(client: NotYTDLAPI, channel_id: str) -> None:
    sections = client.channel_sections.load(
        ChannelSectionsTest.recorded_content(channel_id),
    )
    assert sections.kind == "youtube#channelSectionListResponse"
    ChannelSectionsTest.parse_test(channel_id)


# TODO: Validate
@pytest.mark.parametrize(
    "channel_id",
    [pytest.param("UCCCCCCCCCCCCCCCCCCCCCCC", id="channel that does not exist")],
)
def test_download_invalid(client: NotYTDLAPI, channel_id: str) -> None:
    ChannelSectionsTest.error_test(
        channel_id,
        lambda: client.channel_sections.download(channel_id),
        ChannelNotFoundError,
    )

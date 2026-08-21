from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.channel_sections import ChannelSections
from not_yt_dlapi.channel_sections.models import ChannelSectionListResponse
from not_yt_dlapi.exceptions import NotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


class TestList(RecordedEndpoint):
    ENDPOINT = ChannelSections
    MODEL = ChannelSectionListResponse
    IGNORED = ("ChannelSectionListResponse.etag", "ChannelSection.etag")

    CHANNEL_IDS = (
        pytest.param("UC4QobU6STFB0P71PMvOGN5A", id="regular channel"),
        # The current API returns basically nothing for a Topic channel.
        pytest.param("UCooTDYkIERWBwDC1JKyoElQ", id="topic channel"),
    )

    @pytest.mark.parametrize("channel_id", CHANNEL_IDS)
    def test_download(self, client: NotYTDLAPI, channel_id: str) -> None:
        self.download_test(
            channel_id,
            lambda: client.channel_sections.list(channel_id),
        )

    @pytest.mark.parametrize("channel_id", CHANNEL_IDS)
    def test_parse(self, channel_id: str) -> None:
        self.parse_test(channel_id)

    def test_invalid_id(self, client: NotYTDLAPI) -> None:
        with pytest.raises(NotFoundError) as error:
            client.channel_sections.list("UCCCCCCCCCCCCCCCCCCCCCCC")

        assert error.value.code == 404  # noqa: PLR2004
        assert error.value.error["errors"][0]["reason"] == "channelNotFound"

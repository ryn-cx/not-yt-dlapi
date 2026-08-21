from __future__ import annotations

from typing import TYPE_CHECKING

from not_yt_dlapi.topic import Topic
from not_yt_dlapi.topic.models import TopicReleases
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


class TestTopic(RecordedEndpoint):
    ENDPOINT = Topic
    MODEL = TopicReleases
    IGNORED = ("TopicReleases.continuation",)
    CHANNEL_ID = "UCooTDYkIERWBwDC1JKyoElQ"

    ALL_RELEASES = f"{CHANNEL_ID}_all"

    def test_download(self, client: NotYTDLAPI) -> None:
        self.download_test(
            self.CHANNEL_ID,
            lambda: client.topic.list(self.CHANNEL_ID),
        )

    def test_parse(self) -> None:
        self.parse_test(self.CHANNEL_ID)

    def test_download_all(self, client: NotYTDLAPI) -> None:
        self.download_test(
            self.ALL_RELEASES,
            lambda: client.topic.list_all(self.CHANNEL_ID),
        )

    def test_parse_all(self) -> None:
        self.parse_test(self.ALL_RELEASES)

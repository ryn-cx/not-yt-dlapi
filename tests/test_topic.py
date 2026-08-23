# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from not_yt_dlapi.topic.models import TopicModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

CHANNEL_ID = "UCooTDYkIERWBwDC1JKyoElQ"
"""A Topic channel, which is the one YouTube generated for a musician."""

ALL_RELEASES = f"{CHANNEL_ID}_all"


# TODO: Validate
class TopicTest(RecordedEndpoint):
    MODEL = TopicModel


# TODO: Validate
def test_download(client: NotYTDLAPI) -> None:
    TopicTest.download_test(CHANNEL_ID, lambda: client.topic.download(CHANNEL_ID))


# TODO: Validate
def test_parse(client: NotYTDLAPI) -> None:
    releases = client.topic.load(TopicTest.recorded_content(CHANNEL_ID))
    assert client.topic.extract_channel_id(releases) == CHANNEL_ID
    assert client.topic.extract_release_ids(releases)
    TopicTest.parse_test(CHANNEL_ID)


# TODO: Validate
def test_download_all(client: NotYTDLAPI) -> None:
    TopicTest.download_test(
        ALL_RELEASES,
        lambda: client.topic.download_all(CHANNEL_ID),
        "Multipage",
    )


# TODO: Validate
def test_parse_all(client: NotYTDLAPI) -> None:
    pages = TopicTest.recorded_documents(ALL_RELEASES, "Multipage")
    stretches = client.topic.load_pages(pages)
    assert client.topic.extract_channel_id(stretches[0]) == CHANNEL_ID
    TopicTest.parse_test(ALL_RELEASES, "Multipage")

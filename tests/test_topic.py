# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

CHANNEL_ID = "UCooTDYkIERWBwDC1JKyoElQ"
"""A Topic channel, which is the one YouTube generated for a musician."""


# TODO: Validate
def test_download(client: NotYTDLAPI) -> None:
    releases = client.topic(CHANNEL_ID)
    assert client.topic.extract_channel_id(releases) == CHANNEL_ID
    assert client.topic.extract_release_ids(releases)


# TODO: Validate
def test_download_all(client: NotYTDLAPI) -> None:
    stretches = client.topic.load_pages(client.topic.download_all(CHANNEL_ID))
    assert client.topic.extract_channel_id(stretches[0]) == CHANNEL_ID

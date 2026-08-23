# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from not_yt_dlapi.feed import read_feed
from not_yt_dlapi.playlist_feed.models import PlaylistFeedModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from pydantic import BaseModel

    from not_yt_dlapi import NotYTDLAPI

PLAYLIST_ID = "UUEIwxahdLz7bap-VDs9h35A"
"""The uploads playlist of https://www.youtube.com/@SteveMould"""


# TODO: Validate
class PlaylistFeedTest(RecordedEndpoint):
    MODEL = PlaylistFeedModel
    SUFFIX = ".xml"
    # A feed holds the newest fifteen videos, so its entries are replaced as the
    # playlist grows.
    IGNORED = ("PlaylistFeedModel.entry", "PlaylistFeedModel.published")

    # TODO: Validate
    @classmethod
    def load_document(cls, document: str) -> BaseModel:
        """Read one recorded feed, which is XML rather than JSON."""
        return PlaylistFeedModel.model_validate(read_feed(document))


# TODO: Validate
def test_download(client: NotYTDLAPI) -> None:
    # YouTube is currently refusing every playlist feed it is asked for, so this
    # raises rather than recording anything until that is fixed.
    PlaylistFeedTest.download_test(
        PLAYLIST_ID,
        lambda: client.playlist_feed.download(PLAYLIST_ID),
    )


# TODO: Validate
def test_parse(client: NotYTDLAPI) -> None:
    feed = client.playlist_feed.load(PlaylistFeedTest.recorded_content(PLAYLIST_ID))
    # A playlist feed keeps every character of the id it was asked for.
    assert feed.playlist_id == PLAYLIST_ID
    PlaylistFeedTest.parse_test(PLAYLIST_ID)

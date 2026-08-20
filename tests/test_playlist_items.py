# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import NotFoundError
from not_yt_dlapi.playlist_items import PlaylistItems
from not_yt_dlapi.playlist_items.models import PlaylistItemListResponse
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

JAWED_PLAYLIST_ID = "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh"
"""A playlist of four items, which one page holds and two pages split up."""


# TODO: Validate
class PlaylistItemTest(RecordedEndpoint):
    ENDPOINT = PlaylistItems


# TODO: Validate
class TestList:
    """Test `playlist_items.list`."""

    # TODO: Validate
    class TestPlaylist(PlaylistItemTest):
        PLAYLIST_ID = JAWED_PLAYLIST_ID

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.playlist_items.list(self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistItemListResponse)

    # TODO: Validate
    class TestFirstPage(PlaylistItemTest):
        """A playlist longer than one page comes back a page at a time.

        The page carries the token the page after it is asked for by.
        """

        PLAYLIST_ID = JAWED_PLAYLIST_ID
        MAX_RESULTS = 2
        NAME = f"{JAWED_PLAYLIST_ID}-{MAX_RESULTS}"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.NAME,
                lambda: (
                    client.playlist_items.list(
                        self.PLAYLIST_ID,
                        max_results=self.MAX_RESULTS,
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.NAME, PlaylistItemListResponse)

    # TODO: Validate
    class TestUploadsPlaylist(PlaylistItemTest):
        """A channel's uploads are a playlist like any other.

        The one difference is that an item was added to it when the video went up.
        """

        PLAYLIST_ID = "UU4QobU6STFB0P71PMvOGN5A"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.playlist_items.list(self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistItemListResponse)

    # TODO: Validate
    class TestUnknownPlaylist:
        """Unlike the playlists endpoint, this one refuses an id nothing is under.

        There is no response to record, only the refusal.
        """

        PLAYLIST_ID = "PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            with pytest.raises(NotFoundError) as error:
                client.playlist_items.list(self.PLAYLIST_ID)

            assert error.value.code == 404  # noqa: PLR2004 - The status code is the point.
            assert error.value.error["errors"][0]["reason"] == "playlistNotFound"

    # TODO: Validate
    class TestMusicPlaylist(PlaylistItemTest):
        """An auto-generated music playlist is refused, though it plays on the site."""

        PLAYLIST_ID = "OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.playlist_items.list(self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistItemListResponse)

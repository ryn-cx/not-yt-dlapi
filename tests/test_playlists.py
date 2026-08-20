# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import HTTPError
from not_yt_dlapi.playlists import DEFAULT_MAX_RESULTS, Playlists
from not_yt_dlapi.playlists.models import PlaylistListResponse
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class PlaylistTest(RecordedEndpoint):
    ENDPOINT = Playlists


# TODO: Validate
class TestList:
    """Test `playlists.list`."""

    class TestPlaylist(PlaylistTest):
        PLAYLIST_ID = "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh"
        """jawed's playlist
        https://www.youtube.com/playlist?list=PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh"""

        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.playlists.list(playlist_ids=self.PLAYLIST_ID).raw,
            )

        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistListResponse)

    # TODO: Validate
    class TestChannel(PlaylistTest):
        CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"
        """jawed's channel https://www.youtube.com/channel/UC4QobU6STFB0P71PMvOGN5A"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.CHANNEL_ID,
                lambda: client.playlists.list(channel_id=self.CHANNEL_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.CHANNEL_ID, PlaylistListResponse)

    # TODO: Validate
    class TestUploadsPlaylist(PlaylistTest):
        PLAYLIST_ID = "UU4QobU6STFB0P71PMvOGN5A"
        """jawed's channel https://www.youtube.com/playlist?list=UU4QobU6STFB0P71PMvOGN5A"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.playlists.list(playlist_ids=self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistListResponse)

    # TODO: Validate
    class TestMusicPlaylist(PlaylistTest):
        PLAYLIST_ID = "OLAK5uy_kgvDzTzHW2NHKXbZ6kzcoCY-XfVE0c-Sc"
        """Despacito is the most popular music video on all of YouTube and it comes from
        this album. https://www.youtube.com/playlist?list=OLAK5uy_kgvDzTzHW2NHKXbZ6kzcoCY

        Source: https://www.youtube.com/playlist?list=PLbpi6ZahtOH6rCGVbivmx20zx88ZKtUXl
        """

        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.playlists.list(playlist_ids=self.PLAYLIST_ID).raw,
            )

        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistListResponse)

    # TODO: Validate
    class TestInvalidPlaylist(PlaylistTest):
        PLAYLIST_ID = "PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.playlists.list(playlist_ids=self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistListResponse)


# TODO: Validate
class TestListAll:
    """Test `playlists.list_all`."""

    # TODO: Validate
    class TestAllOfAChannelsPlaylists:
        """Every playlist a channel made, which is far more than one page holds.

        The channel has thousands of them, so walking to the end takes tens of
        requests and the count moves as YouTube makes more. What is checked is the
        shape rather than the number: that more came back than one page holds, that
        each playlist arrived in a response of its own, and that none arrived twice,
        which is what a page walked wrongly would give.

        There is no response to record, only what walking them all gives.
        """

        CHANNEL_ID = "UCBR8-60-B28hp2BmDPdntcQ"
        """YouTube's own channel https://www.youtube.com/@YouTube/playlists"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            responses = client.playlists.list_all(channel_id=self.CHANNEL_ID)
            playlist_ids = [response.items[0].id for response in responses]

            assert all(len(response.items) == 1 for response in responses)
            assert len(playlist_ids) > DEFAULT_MAX_RESULTS
            assert len(set(playlist_ids)) == len(playlist_ids)


# TODO: Validate
class TestFeed:
    """Test `playlists.feed`."""

    # TODO: Validate
    class TestPlaylistIsDown:
        """YouTube refuses every playlist feed it is asked for at the moment.

        There is nothing to record and nothing to parse while that is true, so
        what is checked is only that the refusal comes back as a refusal. Which
        refusal it is is not checked, because it is not always the same one: the
        same request is answered `404` most times and `500` some of them, which
        is what being broken looks like rather than what being asked about
        something that does not exist looks like.

        When playlist feeds answer again this test is the one that fails, and
        what replaces it is a download and a parse test like the channel feed
        has.
        """

        PLAYLIST_ID = "UUEIwxahdLz7bap-VDs9h35A"
        """The uploads playlist of https://www.youtube.com/@veritasium"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            with pytest.raises(HTTPError):
                client.playlists.feed(playlist_id=self.PLAYLIST_ID)

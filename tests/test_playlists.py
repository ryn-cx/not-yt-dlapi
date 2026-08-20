# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from not_yt_dlapi.playlists import DEFAULT_MAX_RESULTS, Playlists
from not_yt_dlapi.playlists.models import PlaylistFeedResponse, PlaylistListResponse
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
    class TestTVShowPlaylistId(PlaylistTest):
        """A playlist whose id is in none of the shapes the cases above cover.

        `PL`, `UU` and `OLAK5uy_` are what an id normally starts with, and this
        is none of them, so what the API answers a request for it with is worth
        holding on to whether that is a playlist or nothing at all.
        """

        PLAYLIST_ID = "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw"
        """https://www.youtube.com/playlist?list=TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw"""

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
    class TestAllOfAChannelsPlaylists(PlaylistTest):
        """Every playlist a channel made, which is far more than one page holds.

        The channel has thousands of them, so walking to the end takes tens of
        requests and the count moves as YouTube makes more. What is checked is the
        shape rather than the number: that more came back than one page holds, that
        each playlist arrived in a response of its own, and that none arrived twice,
        which is what a page walked wrongly would give.

        What is recorded is what walking them all gave, so the walk happens once
        rather than on every run.
        """

        CHANNEL_ID = "UCBR8-60-B28hp2BmDPdntcQ"
        """YouTube's own channel https://www.youtube.com/@YouTube/playlists"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.CHANNEL_ID,
                lambda: [
                    response.raw
                    for response in client.playlists.list_all(
                        channel_id=self.CHANNEL_ID,
                    )
                ],
            )

        # TODO: Validate
        def test_each_playlist_arrived_once(self) -> None:
            """Every playlist came back in a response of its own, and only once."""
            responses = self.recorded_content(self.CHANNEL_ID)
            playlist_ids = [response["items"][0]["id"] for response in responses]

            assert all(len(response["items"]) == 1 for response in responses)
            assert len(playlist_ids) > DEFAULT_MAX_RESULTS
            assert len(set(playlist_ids)) == len(playlist_ids)


# TODO: Validate
class TestFeed:
    """Test `playlists.feed`."""

    # TODO: Validate
    class TestUploadsPlaylist(PlaylistTest):
        """The feed of a playlist that is still being added to.

        A feed cannot be recorded the way a response can. It is the newest
        fifteen videos of a playlist that keeps growing, and every entry carries
        a view count that moves while it is being read, so no two downloads of
        one feed are ever the same document and comparing one against a
        recording would only ever fail.

        So the two tests ask different things of the feed than an API endpoint's
        do. The download test asks whether today's feed still reads into the
        models at all, which is the thing that breaks when YouTube changes the
        document. The recording under `_files` is a frozen sample kept by hand
        rather than written by the test, and the parse test is what holds the
        reading of it still.
        """

        SUFFIX = ".xml"
        """A feed is served as XML, and the recording is the document itself."""

        PLAYLIST_ID = "UUEIwxahdLz7bap-VDs9h35A"
        """The uploads playlist of https://www.youtube.com/@SteveMould"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            feed = client.playlists.feed(playlist_id=self.PLAYLIST_ID)

            # A playlist feed writes the id it was asked for in full, where a
            # channel feed writes its channel id with the leading `UC` off. An
            # uploads playlist is that channel's id under `UU`, so the entries
            # are the same id again under `UC`.
            assert feed.playlist_id == self.PLAYLIST_ID
            assert feed.entries
            assert all(
                entry.channel_id == self.PLAYLIST_ID.replace("UU", "UC", 1)
                for entry in feed.entries
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, PlaylistFeedResponse)

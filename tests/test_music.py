# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from not_yt_dlapi.music import Music
from not_yt_dlapi.music.models import MusicPlaylist
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class MusicTest(RecordedEndpoint):
    ENDPOINT = Music


# TODO: Validate
class TestList:
    """Test `music.list`."""

    # TODO: Validate
    class TestOneArtist(MusicTest):
        """An album by one musician, put out on that musician's own channel."""

        PLAYLIST_ID = "OLAK5uy_mYS5efFtXpNEV9MDDZsGt3LkFJNR02GzY"
        """clipping. - Dead Channel Sky."""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.music.list(self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, MusicPlaylist)

        # TODO: Validate
        def test_the_one_musician_is_credited(self) -> None:
            """The one name credited is the channel the tracks went up on."""
            playlist = MusicPlaylist.from_response(
                self.recorded_content(self.PLAYLIST_ID),
            )

            assert playlist.artists == ["clipping."]
            assert playlist.release_type == "Album"
            assert playlist.artist_channel_id == "UCGEkvEO_z3ncFPOeTIIf-TQ"

    # TODO: Validate
    class TestTwoArtists(MusicTest):
        """An album credited to two musicians, which one of them put out.

        The credit is the only thing that names both: every track was published
        by Future's channel and says nothing of Metro Boomin, so a release read
        from its tracks alone would lose half of who made it.
        """

        PLAYLIST_ID = "OLAK5uy_lVxq_QCXDlleCnpsszQyiFextilkX12_w"
        """Future, Metro Boomin - WE DON'T TRUST YOU."""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.music.list(self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, MusicPlaylist)

        # TODO: Validate
        def test_both_musicians_are_credited(self) -> None:
            """Both names are read, and the channel is the one that put it out."""
            playlist = MusicPlaylist.from_response(
                self.recorded_content(self.PLAYLIST_ID),
            )

            assert playlist.artists == ["Future", "Metro Boomin"]
            assert playlist.artist_channel_id == "UCSDvKdIQOwTfcyOimSi9oYA"
            assert {track.channel_title for track in playlist.tracks} == {"Future"}

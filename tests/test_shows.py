# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from not_yt_dlapi.shows import Shows
from not_yt_dlapi.shows.models import Show
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class ShowTest(RecordedEndpoint):
    ENDPOINT = Shows


# TODO: Validate
class TestList:
    """Test `shows.list`."""

    # TODO: Validate
    class TestShow(ShowTest):
        """Every season of a show, each holding the episodes listed under it."""

        PLAYLIST_ID = "TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.shows.list(self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, Show)

    # TODO: Validate
    class TestFirstSeasonIsNotSeasonOne(ShowTest):
        """A show whose seasons are numbered from where the show is up to.

        Hell's Kitchen has run for over twenty years and YouTube carries three
        of them, numbered the way the show numbers them rather than from one.
        So the first season of what comes back is season twenty-one, which is
        what nothing here may assume otherwise.
        """

        PLAYLIST_ID = "TVSHI1FGTrUgFn4lRj_kLDPqR3ZC_PDpPGEPg"
        """https://www.youtube.com/show/SC76ETXKYZoiPWiG6TLxkBLA"""

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.PLAYLIST_ID,
                lambda: client.shows.list(self.PLAYLIST_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.PLAYLIST_ID, Show)

        # TODO: Validate
        def test_seasons_are_numbered_as_the_show_numbers_them(self) -> None:
            """The seasons are the numbers the show gives them, not one upwards."""
            show = Show.from_response(self.recorded_content(self.PLAYLIST_ID))
            numbers = [season.number for season in show.seasons]

            assert numbers
            assert numbers[0] != 1
            assert numbers == sorted(numbers)

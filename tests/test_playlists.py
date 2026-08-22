# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.playlists import Playlists
from not_yt_dlapi.playlists.models import PlaylistFeedResponse, PlaylistListResponse
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class TestPlaylists(RecordedEndpoint):
    ENDPOINT = Playlists
    MODEL = PlaylistListResponse
    IGNORED = ("PlaylistListResponse.etag", "Playlist.etag")
    # A playlist gains and loses videos, so only the type is held against the
    # recording.
    SAME_TYPE = ("PlaylistContentDetails.item_count",)

    # `PL`, `UU` and `OLAK5uy_` are what an id normally starts with and a show's
    # is none of them, so each shape of id is asked for.
    PLAYLIST_IDS = (
        pytest.param("PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh", id="regular playlist"),
        pytest.param("UU4QobU6STFB0P71PMvOGN5A", id="channel uploads"),
        pytest.param("OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8", id="music playlist"),
        pytest.param("TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw", id="show"),
        pytest.param("PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", id="invalid playlist"),
    )

    # A channel answers with every playlist it made rather than one asked for.
    # The hub channels are YouTube's own and hold no videos, only playlists.
    CHANNEL_IDS = (
        pytest.param("UC4QobU6STFB0P71PMvOGN5A", id="channel"),
        pytest.param("UCYoEbMFACdvkquYH5h31RNA", id="channel linked to movie"),
        pytest.param("UClgRkhTL3_hImCAmdLfDE4g", id="movies and shows hub"),
        pytest.param("UC-9-kyTW8ZkZNDHQJ6FgpwQ", id="music hub"),
        pytest.param("UCtFRv9O2AHqOZjjynzrv-xg", id="learning hub"),
    )

    # Only the first channel is walked, since walking one is enough to say the
    # walk works and every extra one is another run of requests.
    WALKED_CHANNEL_IDS = CHANNEL_IDS[:1]

    # TODO: Validate
    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_download(self, client: NotYTDLAPI, playlist_id: str) -> None:
        self.download_test(
            playlist_id,
            lambda: client.playlists.list(playlist_ids=playlist_id),
        )

    # TODO: Validate
    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_parse(self, playlist_id: str) -> None:
        self.parse_test(playlist_id)

    # TODO: Validate
    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_download_all(self, client: NotYTDLAPI, playlist_id: str) -> None:
        self.download_test(
            f"{playlist_id}_all",
            lambda: client.playlists.list_all(playlist_ids=[playlist_id]),
        )

    # TODO: Validate
    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_parse_all(self, playlist_id: str) -> None:
        self.parse_test(f"{playlist_id}_all")

    # TODO: Validate
    @pytest.mark.parametrize("channel_id", CHANNEL_IDS)
    def test_download_channel(self, client: NotYTDLAPI, channel_id: str) -> None:
        self.download_test(
            channel_id,
            lambda: client.playlists.list(channel_id=channel_id),
        )

    # TODO: Validate
    @pytest.mark.parametrize("channel_id", CHANNEL_IDS)
    def test_parse_channel(self, channel_id: str) -> None:
        self.parse_test(channel_id)

    # TODO: Validate
    @pytest.mark.parametrize("channel_id", WALKED_CHANNEL_IDS)
    def test_download_channel_all(self, client: NotYTDLAPI, channel_id: str) -> None:
        # Every response the walk was served is recorded, so the walk happens
        # once rather than on every run.
        self.download_test(
            f"{channel_id}_all",
            lambda: client.playlists.list_all(channel_id=channel_id),
        )

    # TODO: Validate
    @pytest.mark.parametrize("channel_id", WALKED_CHANNEL_IDS)
    def test_parse_channel_all(self, channel_id: str) -> None:
        self.parse_test(f"{channel_id}_all")


# TODO: Validate
class TestFeed(RecordedEndpoint):
    ENDPOINT = Playlists
    MODEL = PlaylistFeedResponse
    # A feed holds the newest fifteen videos, so its entries are replaced as the
    # playlist grows.
    IGNORED = ("PlaylistFeedResponse.entries", "PlaylistFeedResponse.published")
    SUFFIX = ".xml"
    PLAYLIST_ID = "UUEIwxahdLz7bap-VDs9h35A"
    """The uploads playlist of https://www.youtube.com/@SteveMould"""

    # TODO: Validate
    def test_download(self, client: NotYTDLAPI) -> None:
        # YouTube is currently refusing every playlist feed it is asked for, so
        # this raises rather than recording anything until that is fixed.
        self.download_test(
            self.PLAYLIST_ID,
            lambda: client.playlists.feed(playlist_id=self.PLAYLIST_ID),
        )

    # TODO: Validate
    def test_parse(self) -> None:
        self.parse_test(self.PLAYLIST_ID)

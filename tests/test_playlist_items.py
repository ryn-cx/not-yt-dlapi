from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import NotFoundError
from not_yt_dlapi.playlist_items import PlaylistItems
from not_yt_dlapi.playlist_items.models import PlaylistItemListResponse
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class TestPlaylistItems(RecordedEndpoint):
    ENDPOINT = PlaylistItems
    MODEL = PlaylistItemListResponse
    IGNORED = ("PlaylistItemListResponse.etag", "PlaylistItem.etag")

    PLAYLIST_IDS = (
        pytest.param("PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh", id="regular playlist"),
        pytest.param("UU4QobU6STFB0P71PMvOGN5A", id="channel uploads"),
        pytest.param("OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8", id="music playlist"),
        pytest.param("PLbpi6ZahtOH4kNyb9pjnMYg4PB7qiljiH", id="multipage playlist"),
        pytest.param("TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw", id="show"),
        # The hub channels are YouTube's own and hold no videos, only
        # playlists, so one playlist of each is asked for.
        pytest.param("PLHPTxTxtC0iZUB6K7RWdvB7bimNTqbL-O", id="movies hub playlist"),
        pytest.param("PLFgquLnL59alvrcyyOWR6zy-De3GUo-B_", id="music hub playlist"),
        pytest.param("PLydZ2Hrp_gPQmh4MSMoUK4H5QPr7AM4bT", id="learning hub playlist"),
    )

    # Only the playlists that were already walked are walked, since the hub
    # playlists are there to be read rather than to say the walk works.
    WALKED_PLAYLIST_IDS = PLAYLIST_IDS[:5]

    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_download(self, client: NotYTDLAPI, playlist_id: str) -> None:
        self.download_test(
            playlist_id,
            lambda: client.playlist_items.list(playlist_id),
        )

    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_parse(self, playlist_id: str) -> None:
        self.parse_test(playlist_id)

    @pytest.mark.parametrize("playlist_id", WALKED_PLAYLIST_IDS)
    def test_download_all(self, client: NotYTDLAPI, playlist_id: str) -> None:
        self.download_test(
            f"{playlist_id}_all",
            lambda: client.playlist_items.list_all(playlist_id),
        )

    @pytest.mark.parametrize("playlist_id", WALKED_PLAYLIST_IDS)
    def test_parse_all(self, playlist_id: str) -> None:
        self.parse_test(f"{playlist_id}_all")

    def test_invalid_id(self, client: NotYTDLAPI) -> None:
        with pytest.raises(NotFoundError) as error:
            client.playlist_items.list("PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

        assert error.value.code == 404  # noqa: PLR2004 - The status code is the point.
        assert error.value.error["errors"][0]["reason"] == "playlistNotFound"

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import PlaylistNotFoundError
from not_yt_dlapi.playlist_items.models import PlaylistItemsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

PLAYLIST_IDS = [
    pytest.param("PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh", id="regular playlist"),
    pytest.param("UU4QobU6STFB0P71PMvOGN5A", id="channel uploads"),
    pytest.param("OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8", id="music playlist"),
    pytest.param("PLbpi6ZahtOH4kNyb9pjnMYg4PB7qiljiH", id="multipage playlist"),
    pytest.param("TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw", id="show"),
    # The hub channels are YouTube's own and hold no videos, only playlists, so
    # one playlist of each is asked for.
    pytest.param("PLHPTxTxtC0iZUB6K7RWdvB7bimNTqbL-O", id="movies hub playlist"),
    pytest.param("PLFgquLnL59alvrcyyOWR6zy-De3GUo-B_", id="music hub playlist"),
    pytest.param("PLydZ2Hrp_gPQmh4MSMoUK4H5QPr7AM4bT", id="learning hub playlist"),
]

# Only the playlists that were already walked are walked, since the hub
# playlists are there to be read rather than to say the walk works.
WALKED_PLAYLIST_IDS = PLAYLIST_IDS[:5]


# TODO: Validate
class PlaylistItemsTest(RecordedEndpoint):
    MODEL = PlaylistItemsModel
    IGNORED = ("PlaylistItemsModel.etag", "PlaylistItem.etag")


# TODO: Validate
@pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
def test_download(client: NotYTDLAPI, playlist_id: str) -> None:
    PlaylistItemsTest.download_test(
        playlist_id,
        lambda: client.playlist_items.download(playlist_id),
    )


# TODO: Validate
@pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
def test_parse(client: NotYTDLAPI, playlist_id: str) -> None:
    items = client.playlist_items.load(
        PlaylistItemsTest.recorded_content(playlist_id),
    )
    assert items.kind == "youtube#playlistItemListResponse"
    PlaylistItemsTest.parse_test(playlist_id)


# TODO: Validate
@pytest.mark.parametrize("playlist_id", WALKED_PLAYLIST_IDS)
def test_download_all(client: NotYTDLAPI, playlist_id: str) -> None:
    PlaylistItemsTest.download_test(
        f"{playlist_id}_all",
        lambda: client.playlist_items.download_all(playlist_id),
        "Multipage",
    )


# TODO: Validate
@pytest.mark.parametrize("playlist_id", WALKED_PLAYLIST_IDS)
def test_parse_all(playlist_id: str) -> None:
    PlaylistItemsTest.parse_test(f"{playlist_id}_all", "Multipage")


# TODO: Validate
@pytest.mark.parametrize(
    "playlist_id",
    [
        pytest.param(
            "PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
            id="playlist that does not exist",
        ),
    ],
)
def test_download_invalid(client: NotYTDLAPI, playlist_id: str) -> None:
    PlaylistItemsTest.error_test(
        playlist_id,
        lambda: client.playlist_items.download(playlist_id),
        PlaylistNotFoundError,
    )

# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import (
    assert_no_content_error,
    data_path,
    download_if_missing,
)

if TYPE_CHECKING:
    from pathlib import Path

    from not_yt_dlapi import NotYTDLAPI
    from not_yt_dlapi.playlist import Playlist
    from not_yt_dlapi.playlist.models import PlaylistModel

ALBUM_PLAYLIST_ID = "OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q"
"""playlist_id of an auto-generated album playlist."""
INVALID_PLAYLIST_ID = "PL0123456789ABCDEF"


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> Playlist:
    return client.playlist


@pytest.fixture(scope="session")
def json_file(endpoint: Playlist) -> Path:
    return data_path(endpoint, ALBUM_PLAYLIST_ID)


@pytest.fixture(scope="session")
def data(endpoint: Playlist, json_file: Path) -> PlaylistModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestPlaylist:
    def test_download(self, endpoint: Playlist) -> None:
        download_if_missing(
            endpoint,
            ALBUM_PLAYLIST_ID,
            lambda: endpoint.download(ALBUM_PLAYLIST_ID),
        )

    def test_value(self, data: PlaylistModel) -> None:
        # TODO: assert expected value (needs live data)
        assert data is not None

    def test_invalid(self, endpoint: Playlist) -> None:
        name = INVALID_PLAYLIST_ID
        assert_no_content_error(
            endpoint,
            name,
            lambda: endpoint.get(INVALID_PLAYLIST_ID),
        )

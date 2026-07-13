# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import (
    assert_playlist_items_not_found_error,
    data_path,
    download_if_missing,
)

if TYPE_CHECKING:
    from pathlib import Path

    from not_yt_dlapi import NotYTDLAPI
    from not_yt_dlapi.playlist_item import PlaylistItems
    from not_yt_dlapi.playlist_item.models import PlaylistItemsModel

UPLOADS_PLAYLIST_ID = "UU4QobU6STFB0P71PMvOGN5A"
"""playlist_id of the uploads playlist for CHANNEL_ID."""
INVALID_PLAYLIST_ID = "PL0123456789ABCDEF"


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> PlaylistItems:
    return client.playlist_items


@pytest.fixture(scope="session")
def json_file(endpoint: PlaylistItems) -> Path:
    return data_path(endpoint, UPLOADS_PLAYLIST_ID)


@pytest.fixture(scope="session")
def data(endpoint: PlaylistItems, json_file: Path) -> PlaylistItemsModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestPlaylistItems:
    def test_download(self, endpoint: PlaylistItems) -> None:
        download_if_missing(
            endpoint,
            UPLOADS_PLAYLIST_ID,
            lambda: endpoint.download(UPLOADS_PLAYLIST_ID),
        )

    def test_value(self, data: PlaylistItemsModel) -> None:
        # TODO: assert expected value (needs live data)
        assert data is not None

    def test_invalid(self, endpoint: PlaylistItems) -> None:
        name = INVALID_PLAYLIST_ID
        assert_playlist_items_not_found_error(
            endpoint,
            name,
            lambda: endpoint.download(INVALID_PLAYLIST_ID),
        )

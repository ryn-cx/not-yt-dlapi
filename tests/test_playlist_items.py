# TODO: Validate
import json
import os

import pytest
from get_around import build_client_automatically

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import PlaylistItemsNotFoundError

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

client = NotYTDLAPI(
    api_key=API_KEY,
    get_around_client=build_client_automatically(),
)

UPLOADS_PLAYLIST_ID = "UU4QobU6STFB0P71PMvOGN5A"
"""playlist_id of the uploads playlist for CHANNEL_ID."""
INVALID_PLAYLIST_ID = "PL0123456789ABCDEF"


class TestPlaylistItems:
    def test_get(self) -> None:
        endpoint = client.playlist_items
        model = endpoint.get(UPLOADS_PLAYLIST_ID)
        assert all(
            item.snippet.playlist_id == UPLOADS_PLAYLIST_ID for item in model.items
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_all(self) -> None:
        endpoint = client.playlist_items
        model = endpoint.get_all(UPLOADS_PLAYLIST_ID)
        assert all(
            item.snippet.playlist_id == UPLOADS_PLAYLIST_ID for item in model.items
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(PlaylistItemsNotFoundError):
            client.playlist_items.get(INVALID_PLAYLIST_ID)

    def test_parse(self) -> None:
        endpoint = client.playlist_items
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

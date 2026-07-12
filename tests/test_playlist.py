# TODO: Validate
import json
import os

import pytest
from get_around import build_client_automatically

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import NoContentError

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

client = NotYTDLAPI(
    api_key=API_KEY,
    get_around_client=build_client_automatically(),
)

ALBUM_PLAYLIST_ID = "OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q"
"""playlist_id of an auto-generated album playlist."""
INVALID_PLAYLIST_ID = "PL0123456789ABCDEF"


class TestPlaylist:
    def test_get(self) -> None:
        endpoint = client.playlist
        model = endpoint.get(ALBUM_PLAYLIST_ID)
        assert any(item.id == ALBUM_PLAYLIST_ID for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.playlist.get(INVALID_PLAYLIST_ID)
        assert error.value.response

    def test_parse(self) -> None:
        endpoint = client.playlist
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

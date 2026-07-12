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

CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"
"""channel_id of the YouTube channel that owns "Me at the zoo"."""
CHANNEL_HANDLE = "@Google"
"""Handle of the Google channel."""
CHANNEL_USERNAME = "MrBeast"
"""Legacy username of the MrBeast channel."""
INVALID_CHANNEL_ID = "UCinvalidchannelid123456"


class TestChannels:
    def test_get(self) -> None:
        endpoint = client.channels
        model = endpoint.get(channel_id=CHANNEL_ID)
        assert any(item.id == CHANNEL_ID for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_by_handle(self) -> None:
        endpoint = client.channels
        model = endpoint.get(handle=CHANNEL_HANDLE)
        assert any(
            item.snippet.custom_url.lower() == CHANNEL_HANDLE.lower()
            for item in model.items
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_by_username(self) -> None:
        endpoint = client.channels
        model = endpoint.get(username=CHANNEL_USERNAME)
        assert model.items
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.channels.get(channel_id=INVALID_CHANNEL_ID)
        assert error.value.response

    def test_parse(self) -> None:
        endpoint = client.channels
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

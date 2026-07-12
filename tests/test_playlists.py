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
YOUTUBE_CHANNEL_ID = "UCBR8-60-B28hp2BmDPdntcQ"
"""channel_id of the official YouTube channel."""
INVALID_CHANNEL_ID = "UCinvalidchannelid123456"


class TestPlaylists:
    def test_get(self) -> None:
        endpoint = client.playlists
        model = endpoint.get(CHANNEL_ID)
        assert all(item.snippet.channel_id == CHANNEL_ID for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    @pytest.mark.parametrize(
        "channel_id",
        [CHANNEL_ID, YOUTUBE_CHANNEL_ID],
        ids=[f"{CHANNEL_ID=}", f"{YOUTUBE_CHANNEL_ID=}"],
    )
    def test_get_all(self, channel_id: str) -> None:
        endpoint = client.playlists
        model = endpoint.get_all(channel_id)
        assert all(item.snippet.channel_id == channel_id for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.playlists.get(INVALID_CHANNEL_ID)
        assert error.value.response

    def test_parse(self) -> None:
        endpoint = client.playlists
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

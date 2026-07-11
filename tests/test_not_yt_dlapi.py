# TODO: Validate
from __future__ import annotations

import json
import os

import pytest
from get_around import build_client_automatically

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import (
    NoContentError,
    PlaylistItemsNotFoundError,
)

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

client = NotYTDLAPI(
    api_key=API_KEY,
    get_around_client=build_client_automatically(),
)

VIDEO_ID = "jNQXAC9IVRw"
"""video_id of "Me at the zoo"."""
AGE_RESTRICTED_VIDEO_ID = "l1ITP7m6R0Q"
"""video_id of an age-restricted video."""
SECOND_VIDEO_ID = "S-8U4lSEq8A"
"""video_id of a second video, used for multi-video requests."""
CHANNEL_ID = "UC4QobU6STFB0P71PMvOGN5A"
"""channel_id of the YouTube channel that owns "Me at the zoo"."""
YOUTUBE_CHANNEL_ID = "UCBR8-60-B28hp2BmDPdntcQ"
"""channel_id of the official YouTube channel."""
CHANNEL_HANDLE = "@Google"
"""Handle of the Google channel."""
CHANNEL_USERNAME = "MrBeast"
"""Legacy username of the MrBeast channel."""
ALBUM_PLAYLIST_ID = "OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q"
"""playlist_id of an auto-generated album playlist."""
UPLOADS_PLAYLIST_ID = "UU4QobU6STFB0P71PMvOGN5A"
"""playlist_id of the uploads playlist for CHANNEL_ID."""
INVALID_VIDEO_ID = "12345678901"
INVALID_CHANNEL_ID = "UCinvalidchannelid123456"
INVALID_PLAYLIST_ID = "PL0123456789ABCDEF"


class TestGet:
    @pytest.mark.parametrize(
        "video_id",
        [VIDEO_ID, AGE_RESTRICTED_VIDEO_ID],
        ids=[f"{VIDEO_ID=}", f"{AGE_RESTRICTED_VIDEO_ID=}"],
    )
    def test_get_videos(self, video_id: str) -> None:
        endpoint = client.videos
        model = endpoint.get(video_id)
        assert any(item.id == video_id for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_videos_multiple(self) -> None:
        endpoint = client.videos
        models = endpoint.get_multiple([VIDEO_ID, SECOND_VIDEO_ID])
        returned_ids = {item.id for model in models for item in model.items}
        assert {VIDEO_ID, SECOND_VIDEO_ID} <= returned_ids
        for model in models:
            endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_playlists(self) -> None:
        endpoint = client.playlists
        model = endpoint.get(CHANNEL_ID)
        assert all(item.snippet.channel_id == CHANNEL_ID for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    @pytest.mark.parametrize(
        "channel_id",
        [CHANNEL_ID, YOUTUBE_CHANNEL_ID],
        ids=[f"{CHANNEL_ID=}", f"{YOUTUBE_CHANNEL_ID=}"],
    )
    def test_get_playlists_all(self, channel_id: str) -> None:
        endpoint = client.playlists
        model = endpoint.get_all(channel_id)
        assert all(item.snippet.channel_id == channel_id for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_playlist(self) -> None:
        endpoint = client.playlist
        model = endpoint.get(ALBUM_PLAYLIST_ID)
        assert any(item.id == ALBUM_PLAYLIST_ID for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_playlist_items(self) -> None:
        endpoint = client.playlist_items
        model = endpoint.get(UPLOADS_PLAYLIST_ID)
        assert all(
            item.snippet.playlist_id == UPLOADS_PLAYLIST_ID for item in model.items
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_playlist_items_all(self) -> None:
        endpoint = client.playlist_items
        model = endpoint.get_all(UPLOADS_PLAYLIST_ID)
        assert all(
            item.snippet.playlist_id == UPLOADS_PLAYLIST_ID for item in model.items
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_channel(self) -> None:
        endpoint = client.channels
        model = endpoint.get(channel_id=CHANNEL_ID)
        assert any(item.id == CHANNEL_ID for item in model.items)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_channel_by_handle(self) -> None:
        endpoint = client.channels
        model = endpoint.get(handle=CHANNEL_HANDLE)
        assert any(
            item.snippet.custom_url.lower() == CHANNEL_HANDLE.lower()
            for item in model.items
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_channel_by_username(self) -> None:
        endpoint = client.channels
        model = endpoint.get(username=CHANNEL_USERNAME)
        assert model.items
        endpoint.save_new_json_file(endpoint.original_input(model))


class TestInvalidGet:
    def test_invalid_get_videos(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.videos.get(INVALID_VIDEO_ID)
        assert error.value.response

    def test_invalid_get_playlists(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.playlists.get(INVALID_CHANNEL_ID)
        assert error.value.response

    def test_invalid_get_playlist(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.playlist.get(INVALID_PLAYLIST_ID)
        assert error.value.response

    def test_invalid_get_playlist_items(self) -> None:
        with pytest.raises(PlaylistItemsNotFoundError):
            client.playlist_items.get(INVALID_PLAYLIST_ID)

    def test_invalid_get_channel(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.channels.get(channel_id=INVALID_CHANNEL_ID)
        assert error.value.response


class TestParse:
    @pytest.mark.parametrize(
        "endpoint_name",
        ["videos", "playlists", "playlist", "playlist_items", "channels"],
    )
    def test_parse(self, endpoint_name: str) -> None:
        endpoint = getattr(client, endpoint_name)
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

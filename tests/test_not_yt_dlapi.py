# TODO: Validate
"""Tests for not_yt_dlapi."""

import json
import os

import pytest

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import (
    ChannelNotFoundError,
    PlaylistItemsNotFoundError,
    PlaylistNotFoundError,
    VideoNotFoundError,
)

API_KEY = os.getenv("YOUTUBE_API_KEY", "")
GET_AROUND_SERVER = os.getenv("GET_AROUND_SERVER")
GET_AROUND_PASSWORD = os.getenv("GET_AROUND_PASSWORD")

client = NotYTDLAPI(
    api_key=API_KEY,
    get_around_server=GET_AROUND_SERVER,
    get_around_password=GET_AROUND_PASSWORD,
)


@pytest.mark.skipif(not API_KEY, reason="YOUTUBE_API_KEY environment variable not set")
class TestGet:
    """Test live get requests across every endpoint.

    Every request saves its response back into the model's ``_files/`` corpus so
    real responses feed future rebuilds.
    """

    def test_get_video(self) -> None:
        """Test getting a video."""
        model = client.videos.get("jNQXAC9IVRw")
        client.videos.save_new_json_file(client.videos.original_input(model))

    def test_get_video_age_restricted(self) -> None:
        """Test getting an age-restricted video."""
        model = client.videos.get("l1ITP7m6R0Q")
        client.videos.save_new_json_file(client.videos.original_input(model))

    def test_get_video_multiple(self) -> None:
        """Test getting multiple videos at once."""
        models = client.videos.get_multiple(["jNQXAC9IVRw", "S-8U4lSEq8A"])
        expected = 2
        assert len(models) == expected
        for model in models:
            client.videos.save_new_json_file(client.videos.original_input(model))

    def test_get_playlists(self) -> None:
        """Test getting playlists for a channel."""
        model = client.playlists.get("UC4QobU6STFB0P71PMvOGN5A")
        client.playlists.save_new_json_file(client.playlists.original_input(model))

    def test_get_playlists_all(self) -> None:
        """Test getting all playlists for a channel with pagination."""
        model = client.playlists.get_all("UC4QobU6STFB0P71PMvOGN5A")
        client.playlists.save_new_json_file(client.playlists.original_input(model))

    def test_get_playlists_youtube(self) -> None:
        """Test getting all playlists for the YouTube channel."""
        model = client.playlists.get_all("UCBR8-60-B28hp2BmDPdntcQ")
        client.playlists.save_new_json_file(client.playlists.original_input(model))

    def test_get_playlist(self) -> None:
        """Test getting an auto-generated album playlist by its ID.

        Auto-generated playlists (such as a Topic channel's albums) are not
        returned when filtering by channel, but can be fetched by ID.
        """
        model = client.playlist.get("OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q")
        expected = 1
        assert len(model.items) == expected
        client.playlist.save_new_json_file(client.playlist.original_input(model))

    def test_get_playlist_item(self) -> None:
        """Test getting items from a playlist."""
        model = client.playlist_items.get("UU4QobU6STFB0P71PMvOGN5A")
        client.playlist_items.save_new_json_file(
            client.playlist_items.original_input(model)
        )

    def test_get_playlist_item_all(self) -> None:
        """Test getting all items from a playlist with pagination."""
        model = client.playlist_items.get_all("UU4QobU6STFB0P71PMvOGN5A")
        client.playlist_items.save_new_json_file(
            client.playlist_items.original_input(model)
        )

    def test_get_channel(self) -> None:
        """Test getting a channel."""
        model = client.channels.get(channel_id="UC4QobU6STFB0P71PMvOGN5A")
        client.channels.save_new_json_file(client.channels.original_input(model))

    def test_get_channel_by_handle(self) -> None:
        """Test getting a channel by handle."""
        model = client.channels.get(handle="@Google")
        client.channels.save_new_json_file(client.channels.original_input(model))

    def test_get_channel_by_username(self) -> None:
        """Test getting a channel by username."""
        model = client.channels.get(username="MrBeast")
        client.channels.save_new_json_file(client.channels.original_input(model))


@pytest.mark.skipif(not API_KEY, reason="YOUTUBE_API_KEY environment variable not set")
class TestInvalidGet:
    """Test get requests for missing or invalid resources."""

    def test_invalid_get_video(self) -> None:
        """Test getting an invalid video."""
        with pytest.raises(VideoNotFoundError):
            client.videos.get("12345678901")

    def test_invalid_get_playlists(self) -> None:
        """Test getting playlists for an invalid channel."""
        with pytest.raises(PlaylistNotFoundError):
            client.playlists.get(channel_id="UCinvalidchannelid123456")

    def test_invalid_get_playlist_item(self) -> None:
        """Test getting items for an invalid playlist."""
        with pytest.raises(PlaylistItemsNotFoundError):
            client.playlist_items.get(playlist_id="PL0123456789ABCDEF")

    def test_invalid_get_channel(self) -> None:
        """Test getting an invalid channel."""
        with pytest.raises(ChannelNotFoundError):
            client.channels.get(channel_id="UCinvalidchannelid123456")


class TestParse:
    """Test parsing every saved file for each endpoint."""

    def test_parse_video(self) -> None:
        """Test parsing every saved video file."""
        for json_file in client.videos.json_files():
            client.videos.parse(json.loads(json_file.read_text()))

    def test_parse_playlists(self) -> None:
        """Test parsing every saved playlists file."""
        for json_file in client.playlists.json_files():
            client.playlists.parse(json.loads(json_file.read_text()))

    def test_parse_playlist(self) -> None:
        """Test parsing every saved playlist file."""
        for json_file in client.playlist.json_files():
            client.playlist.parse(json.loads(json_file.read_text()))

    def test_parse_playlist_item(self) -> None:
        """Test parsing every saved playlist item file."""
        for json_file in client.playlist_items.json_files():
            client.playlist_items.parse(json.loads(json_file.read_text()))

    def test_parse_channel(self) -> None:
        """Test parsing every saved channel file."""
        for json_file in client.channels.json_files():
            client.channels.parse(json.loads(json_file.read_text()))

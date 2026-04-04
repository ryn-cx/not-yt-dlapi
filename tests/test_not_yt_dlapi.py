"""Tests for not_yt_dlapi."""

import json
import os

import pytest

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import ChannelNotFoundError, VideoNotFoundError

API_KEY = os.getenv("YOUTUBE_API_KEY", "")
GET_AROUND_SERVER = os.getenv("GET_AROUND_SERVER")
GET_AROUND_PASSWORD = os.getenv("GET_AROUND_PASSWORD")

client = NotYTDLAPI(
    api_key=API_KEY,
    get_around_server=GET_AROUND_SERVER,
    get_around_password=GET_AROUND_PASSWORD,
)


class TestParse:
    """Tests parsing files."""

    def test_parse_video(self) -> None:
        """Test parsing video files."""
        for json_file in client.video.json_files():
            file_content = json.loads(json_file.read_text())
            client.video.parse(file_content)

    def test_parse_playlist(self) -> None:
        """Test parsing playlist files."""
        for json_file in client.playlist.json_files():
            file_content = json.loads(json_file.read_text())
            client.playlist.parse(file_content)

    def test_parse_playlist_item(self) -> None:
        """Test parsing playlist item files."""
        for json_file in client.playlist_item.json_files():
            file_content = json.loads(json_file.read_text())
            client.playlist_item.parse(file_content)

    def test_parse_channel(self) -> None:
        """Test parsing channel files."""
        for json_file in client.channel.json_files():
            file_content = json.loads(json_file.read_text())
            client.channel.parse(file_content)


@pytest.mark.skipif(not API_KEY, reason="YOUTUBE_API_KEY environment variable not set")
class TestGet:
    """Tests getting data."""

    class TestValid:
        """Tests getting data with valid inputs."""

        def test_get_video(self) -> None:
            """Test getting a video."""
            client.video.get("jNQXAC9IVRw")

        def test_get_age_restricted_video(self) -> None:
            """Test getting an age-restricted video."""
            client.video.get("l1ITP7m6R0Q")

        def test_get_playlist(self) -> None:
            """Test getting playlists for a channel."""
            client.playlist.get("UC4QobU6STFB0P71PMvOGN5A")

        def test_get_all_playlists(self) -> None:
            """Test getting all playlists for a channel with pagination."""
            client.playlist.get_all("UC4QobU6STFB0P71PMvOGN5A")

        def test_get_playlist_item(self) -> None:
            """Test getting items from a playlist."""
            client.playlist_item.get("UU4QobU6STFB0P71PMvOGN5A")

        def test_get_all_playlist_items(self) -> None:
            """Test getting all items from a playlist with pagination."""
            client.playlist_item.get_all("UU4QobU6STFB0P71PMvOGN5A")

        def test_get_multiple_videos(self) -> None:
            """Test getting multiple videos at once."""
            results = client.video.get_multiple(["jNQXAC9IVRw", "S-8U4lSEq8A"])
            expected = 2
            assert len(results) == expected

        def test_get_channel(self) -> None:
            """Test getting a channel."""
            client.channel.get(channel_id="UC4QobU6STFB0P71PMvOGN5A")

        def test_get_channel_by_handle(self) -> None:
            """Test getting a channel by handle."""
            client.channel.get(handle="@Google")

    class TestInvalid:
        """Tests getting data with invalid inputs."""

        def test_get_invalid_video(self) -> None:
            """Test getting an invalid video."""
            with pytest.raises(VideoNotFoundError):
                client.video.get("12345678901")

        def test_get_invalid_channel(self) -> None:
            """Test getting an invalid channel."""
            with pytest.raises(ChannelNotFoundError):
                client.channel.get(channel_id="UCinvalidchannelid123456")

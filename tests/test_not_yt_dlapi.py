"""Tests for not_yt_dlapi."""

import json
import os

import pytest

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import VideoNotFoundError

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

client = NotYTDLAPI(api_key=API_KEY)


class TestParse:
    """Tests parsing files."""

    def test_parse_video(self) -> None:
        """Test parsing video files."""
        for json_file in client.video.json_files():
            file_content = json.loads(json_file.read_text())
            client.video.parse(file_content)


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

    class TestInvalid:
        """Tests getting data with invalid inputs."""

        def test_get_invalid_video(self) -> None:
            """Test getting an invalid video."""
            with pytest.raises(VideoNotFoundError):
                client.video.get("12345678901")

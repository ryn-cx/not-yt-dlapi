"""Tests for the not_yt_dlapi library."""

import json
import os

import pytest

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.exceptions import VideoNotFoundError

API_KEY = os.getenv("YOUTUBE_API_KEY", "")


class TestParsing:
    """Tests for parsing saved JSON files into Pydantic models."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        self.client = NotYTDLAPI(api_key=API_KEY)

    def test_parse_video(self) -> None:
        """Parse all saved video JSON files."""
        for json_file in self.client.video.json_files():
            file_content = json.loads(json_file.read_text())
            self.client.video.parse(file_content)


@pytest.mark.skipif(not API_KEY, reason="YOUTUBE_API_KEY environment variable not set")
class TestGet:
    """Tests for downloading and parsing live data from YouTube."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        self.client = NotYTDLAPI(api_key=API_KEY)

    def test_get_video(self) -> None:
        """Download and parse a public video."""
        self.client.video.get("jNQXAC9IVRw")

    def test_get_age_restricted_video(self) -> None:
        """Download and parse an age-restricted video."""
        self.client.video.get("l1ITP7m6R0Q")

    def test_get_invalid_video(self) -> None:
        """Verify that an invalid video ID raises VideoNotFoundError."""
        with pytest.raises(VideoNotFoundError):
            self.client.video.get("12345678901")

import json
import logging
import os
from collections.abc import Iterator
from pathlib import Path

import pytest

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.constants import FILES_PATH
from not_yt_dlapi.video import VideoNotFoundError

logger = logging.getLogger(__name__)


if not (API_KEY := os.getenv("YOUTUBE_API_KEY", "")):
    pytest.skip("YOUTUBE_API_KEY environment variable not set", allow_module_level=True)

client = NotYTDLAPI(api_key=API_KEY)


class TestParsing:
    def get_test_files(self, endpoint: str) -> Iterator[Path]:
        """Get all JSON test files for a given endpoint."""
        dir_path = FILES_PATH / endpoint
        if not dir_path.exists():
            pytest.skip(f"{dir_path} not found")
        return dir_path.glob("*.json")

    def test_parse_video(self) -> None:
        for json_file in self.get_test_files("video"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_video(file_content, update=True)
            assert file_content == client.dump_response(parsed)


class TestGet:
    def test_get_video(self) -> None:
        """Test getting a public video."""
        client.get_video("jNQXAC9IVRw")

    def test_get_age_restricted_video(self) -> None:
        """Test getting an age-restricted video."""
        client.get_video("l1ITP7m6R0Q")

    def test_get_invalid_video(self) -> None:
        """Test getting an age-restricted video."""
        with pytest.raises(VideoNotFoundError):
            client.get_video("invalid")

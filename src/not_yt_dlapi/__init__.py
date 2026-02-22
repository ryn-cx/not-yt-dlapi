"""NotYTDLAPI is a companion for yt-dlapi."""

from googleapiclient.discovery import build

from not_yt_dlapi.video import Video


class NotYTDLAPI:
    """Interface for downloading and parsing data from the YouTube Data API."""

    def __init__(self, api_key: str) -> None:
        """Initialize the NotYTDLAPI client."""
        self.api_key = api_key
        self.youtube = build("youtube", "v3", developerKey=api_key)

        self.video = Video(self)

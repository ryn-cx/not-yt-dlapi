"""NotYTDLAPI is a companion for yt-dlapi."""

from get_around import GetAround

from not_yt_dlapi.channel import Channels
from not_yt_dlapi.playlist import Playlists
from not_yt_dlapi.playlist_item import PlaylistItems
from not_yt_dlapi.video import Videos


class NotYTDLAPI:
    """Interface for downloading and parsing data from the YouTube Data API."""

    def __init__(
        self,
        api_key: str,
        *,
        get_around_server: str | None = None,
        get_around_password: str | None = None,
    ) -> None:
        """Initialize the NotYTDLAPI client."""
        self.api_key = api_key
        self.get_around = GetAround(
            server=get_around_server,
            password=get_around_password,
        )

        self.videos = Videos(self)
        self.playlists = Playlists(self)
        self.playlist_items = PlaylistItems(self)
        self.channels = Channels(self)

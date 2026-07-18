<!-- TODO: Validate -->
# not-yt-dlapi

Unofficial YouTube API wrapper.

`not-yt-dlapi` wraps a small subset of the official [YouTube Data
API](https://developers.google.com/youtube/v3) and parses its raw JSON into typed
[Pydantic](https://docs.pydantic.dev/) models, giving you a small, structured API for
reading data about YouTube videos, channels, and playlists.

## Installation

```bash
uv add git+https://github.com/ryn-cx/not-yt-dlapi
```

## Usage

Create a client with either an API key or OAuth credentials, then call `get(...)`
on an endpoint to download from YouTube and get back a parsed, typed model.

```python
from not_yt_dlapi import NotYTDLAPI

# Authenticate with an API key for public data...
client = NotYTDLAPI(api_key="YOUR_API_KEY")

# ...or with OAuth credentials (refreshed automatically when expired).
client = NotYTDLAPI(credentials=credentials)

# A single video, by video ID.
video = client.videos.download_and_parse(["jNQXAC9IVRw"])

# Multiple videos at once, by a list of video IDs (batched in groups of 50).
videos = client.videos.download_and_parse_all(["jNQXAC9IVRw", "9bZkp7q19f0"])

# A channel, by channel ID, handle, or legacy username.
channel = client.channel.download_and_parse(channel_id="UC4QobU6STFB0P71PMvOGN5A")
channel = client.channel.download_and_parse(channel_handle="jawed")
channel = client.channel.download_and_parse(channel_username="jawed")

# A channel's sections (the shelves on its channel page), by channel ID.
sections = client.channel_sections.download_and_parse("UC4QobU6STFB0P71PMvOGN5A")

# A single playlist, by playlist ID.
playlist = client.playlists.download_and_parse(
    playlist_id="PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh"
)

# A single page of a channel's playlists, by channel ID.
playlists = client.playlists.download_and_parse(channel_id="UC4QobU6STFB0P71PMvOGN5A")

# All of a channel's playlists, with automatic pagination.
playlists = client.playlists.download_and_parse_all("UC4QobU6STFB0P71PMvOGN5A")

# A single page of the items in a playlist, by playlist ID.
items = client.playlist_items.download_and_parse("PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh")

# All items in a playlist, with automatic pagination.
items = client.playlist_items.download_and_parse_all(
    "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh"
)
```

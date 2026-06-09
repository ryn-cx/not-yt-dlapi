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
video = client.videos.get("jNQXAC9IVRw")

# Multiple videos at once, by a list of video IDs (batched in groups of 50).
videos = client.videos.get_multiple(["jNQXAC9IVRw", "9bZkp7q19f0"])

# A channel, by channel ID, handle, or legacy username.
channel = client.channels.get(channel_id="UC4QobU6STFB0P71PMvOGN5A")
channel = client.channels.get(handle="jawed")
channel = client.channels.get(username="jawed")

# A single page of a channel's playlists, by channel ID.
playlists = client.playlists.get("UC4QobU6STFB0P71PMvOGN5A")

# All of a channel's playlists, with automatic pagination.
playlists = client.playlists.get_all("UC4QobU6STFB0P71PMvOGN5A")

# A single page of the items in a playlist, by playlist ID.
items = client.playlist_items.get("PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh")

# All items in a playlist, with automatic pagination.
items = client.playlist_items.get_all("PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh")
```

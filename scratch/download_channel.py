# TODO: Validate
"""Download one channel, its first page of playlists and of uploads, save each.

The channel is asked about by id and the playlists by the same id, which asks
for the playlists that channel owns rather than any it happens to be in. The
uploads are a playlist like any other, named by the id the channel itself gives
for them, so they are asked for as playlist items rather than as a channel.
Only the first page is asked for: what comes back carries a `next_page_token`
when there are more, and following it is deliberately not done here.

Each response is written next to this file as the raw JSON it was served as,
which is the same thing a recording under `tests/_files` holds.
"""

from __future__ import annotations

import json
from pathlib import Path

from get_around import build_client_automatically, get_credential

from not_yt_dlapi import NotYTDLAPI

CHANNEL_ID = "UCuVPpxrm2VAgpH3Ktln4HXg"
"""The channel to download."""

OUTPUT_DIRECTORY = Path(__file__).parent
"""Where the downloaded responses are written."""


# TODO: Validate
def save(name: str, raw: dict) -> Path:
    """Write a downloaded response out and return where it went."""
    path = OUTPUT_DIRECTORY / f"{name}.json"
    path.write_text(json.dumps(raw, indent=2), encoding="utf-8")
    return path


# TODO: Validate
def main() -> None:
    """Download the channel, a page of its playlists and of its uploads."""
    client = NotYTDLAPI(
        api_key=get_credential("YOUTUBE_API_KEY"),
        get_around_client=build_client_automatically(),
    )

    channel = client.channels.list(channel_id=CHANNEL_ID)
    path = save("channel", channel.raw)
    print(f"Channel: saved {len(channel.items)} item(s) to {path}")

    playlists = client.playlists.list(channel_id=CHANNEL_ID)
    path = save("playlists", playlists.raw)
    print(f"Playlists: saved {len(playlists.items)} item(s) to {path}")
    if playlists.next_page_token:
        print(f"More pages: next_page_token={playlists.next_page_token}")

    uploads_id = channel.items[0].content_details.related_playlists.uploads
    uploads = client.playlist_items.list(uploads_id)
    path = save("uploads", uploads.raw)
    print(f"Uploads: saved {len(uploads.items)} item(s) to {path}")
    if uploads.next_page_token:
        print(f"More pages: next_page_token={uploads.next_page_token}")


if __name__ == "__main__":
    main()

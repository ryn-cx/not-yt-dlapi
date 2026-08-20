# TODO: Validate
"""Download one playlist twice over, from browse and from the API, save both.

Browse is asked for the playlist page the way the site asks for it, by the
playlist id under a `VL` prefix, and is followed to the end: what comes back
carries a continuation while there are more videos, so each answer is saved as
its own file. That is the whole playlist, videos and all.

The API is asked the same playlist by id through `playlists.list`, which
answers with the playlist itself and nothing about what is in it. Its videos
would be `playlist_items.list`, which is deliberately not asked for here.

Each response is written next to this file as the raw JSON it was served as,
which is the same thing a recording under `tests/_files` holds.
"""

from __future__ import annotations

import json
from pathlib import Path

from get_around import build_client_automatically, get_credential

from not_yt_dlapi import NotYTDLAPI
from not_yt_dlapi.utils import read_continuation

PLAYLIST_ID = "OLAK5uy_lVxq_QCXDlleCnpsszQyiFextilkX12_w"
"""The playlist to download."""

OUTPUT_DIRECTORY = Path(__file__).parent
"""Where the downloaded responses are written."""


# TODO: Validate
def save(name: str, raw: dict) -> Path:
    """Write a downloaded response out and return where it went."""
    path = OUTPUT_DIRECTORY / f"{name}.json"
    path.write_text(json.dumps(raw, indent=2), encoding="utf-8")
    return path


# TODO: Validate
def download_browse(client: NotYTDLAPI) -> None:
    """Browse the playlist to the end, saving each answer as it arrives."""
    browsed = client.browse({"browseId": f"VL{PLAYLIST_ID}"}, "download_playlist")
    page = 0

    while True:
        path = save(f"playlist_browse_{page:02}", browsed)
        print(f"Browse: saved page {page} to {path}")

        token = read_continuation(browsed)
        if token is None:
            return

        page += 1
        browsed = client.browse({"continuation": token}, "download_playlist")


# TODO: Validate
def main() -> None:
    """Download the playlist from browse and from the playlists endpoint."""
    client = NotYTDLAPI(
        api_key=get_credential("YOUTUBE_API_KEY"),
        get_around_client=build_client_automatically(),
    )

    download_browse(client)

    playlist = client.playlists.list(playlist_ids=PLAYLIST_ID)
    path = save("playlist", playlist.raw)
    print(f"Playlist: saved {len(playlist.items)} item(s) to {path}")


if __name__ == "__main__":
    main()

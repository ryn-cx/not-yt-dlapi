# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

# `PL`, `UU` and `OLAK5uy_` are what an id normally starts with and a show's is
# none of them, so each shape of id is asked for.
PLAYLIST_IDS = [
    pytest.param("PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh", id="regular playlist"),
    pytest.param("UU4QobU6STFB0P71PMvOGN5A", id="channel uploads"),
    pytest.param("OLAK5uy_mKcftf5tOvVhq-CsutohYLKrB1l8PqCG8", id="music playlist"),
    pytest.param("TVSHX2-tv9KBHSAWLsDbH3h9vNzwxEAyyqXMw", id="show"),
    pytest.param("PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", id="invalid playlist"),
]

# A channel answers with every playlist it made rather than one asked for. The
# hub channels are YouTube's own and hold no videos, only playlists.
CHANNEL_IDS = [
    pytest.param("UC4QobU6STFB0P71PMvOGN5A", id="channel"),
    pytest.param("UCYoEbMFACdvkquYH5h31RNA", id="channel linked to movie"),
    pytest.param("UClgRkhTL3_hImCAmdLfDE4g", id="movies and shows hub"),
    pytest.param("UC-9-kyTW8ZkZNDHQJ6FgpwQ", id="music hub"),
    pytest.param("UCtFRv9O2AHqOZjjynzrv-xg", id="learning hub"),
]

# Only the first channel is walked, since walking one is enough to say the walk
# works and every extra one is another run of requests.
WALKED_CHANNEL_IDS = CHANNEL_IDS[:1]


# TODO: Validate
@pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
def test_download(client: NotYTDLAPI, playlist_id: str) -> None:
    playlists = client.playlists(playlist_ids=playlist_id)
    assert playlists.kind == "youtube#playlistListResponse"


# TODO: Validate
@pytest.mark.parametrize("channel_id", CHANNEL_IDS)
def test_download_channel(client: NotYTDLAPI, channel_id: str) -> None:
    playlists = client.playlists(channel_id=channel_id)
    assert playlists.kind == "youtube#playlistListResponse"


# TODO: Validate
@pytest.mark.parametrize("channel_id", WALKED_CHANNEL_IDS)
def test_download_channel_all(client: NotYTDLAPI, channel_id: str) -> None:
    pages = client.playlists.download_all(channel_id=channel_id)
    assert client.playlists.extract_items(pages)


# TODO: Validate
def test_download_no_filters(client: NotYTDLAPI) -> None:
    with pytest.raises(ValueError, match="Invalid number of arguments"):
        client.playlists.download()

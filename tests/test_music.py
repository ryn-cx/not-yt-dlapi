# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

PLAYLIST_IDS = [
    pytest.param("OLAK5uy_mYS5efFtXpNEV9MDDZsGt3LkFJNR02GzY", id="channel, one artist"),
    pytest.param(
        "OLAK5uy_lVxq_QCXDlleCnpsszQyiFextilkX12_w",
        id="channel, two artists",
    ),
    pytest.param(
        "OLAK5uy_kiAyq0iiYYIPvqybBkpxFvNai3lAw3fyU",
        id="topic, three artists",
    ),
]


# TODO: Validate
@pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
def test_download(client: NotYTDLAPI, playlist_id: str) -> None:
    release = client.music(playlist_id)
    assert client.music.extract_playlist_id(release) == playlist_id
    assert client.music.extract_artists(release)
    assert client.music.extract_track_ids(release)

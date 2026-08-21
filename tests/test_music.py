from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.music import Music
from not_yt_dlapi.music.models import MusicPlaylist
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


class TestList(RecordedEndpoint):
    ENDPOINT = Music
    MODEL = MusicPlaylist
    IGNORED = (
        "MusicTrack.view_count_text",
        "MusicTrack.published_text",
        "MusicPlaylist.thumbnails",
    )

    PLAYLIST_IDS = (
        pytest.param("OLAK5uy_mYS5efFtXpNEV9MDDZsGt3LkFJNR02GzY", id="one artist"),
        pytest.param("OLAK5uy_lVxq_QCXDlleCnpsszQyiFextilkX12_w", id="two artists"),
    )

    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_download(self, client: NotYTDLAPI, playlist_id: str) -> None:
        self.download_test(playlist_id, lambda: client.music.list(playlist_id))

    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_parse(self, playlist_id: str) -> None:
        self.parse_test(playlist_id)

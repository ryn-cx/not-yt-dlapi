from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Any

import pytest
from pydantic import BaseModel

from not_yt_dlapi.exceptions import ChannelNotFoundError, PlaylistNotFoundError
from tests.utils import (
    assert_error,
    download_and_save,
    page_dicts,
    page_models,
    parse_json,
    single_dict,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from not_yt_dlapi import NotYTDLAPI
    from not_yt_dlapi.playlists import Playlists
    from not_yt_dlapi.playlists.models import PlaylistsModel

# The input shapes extract_items accepts.
type ExtractInput = (
    PlaylistsModel | dict[str, Any] | list[PlaylistsModel] | list[dict[str, Any]]
)


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> Playlists:
    return client.playlists


PLAYLIST_IDS: list[str] = [
    # Album playlist.
    # https://www.youtube.com/playlist?list=OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q
    "OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q",
    # Regular playlist.
    # https://www.youtube.com/playlist?list=PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh
    "PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh",
    # Channel uploads playlist: https://www.youtube.com/channel/UC4QobU6STFB0P71PMvOGN5A
    "UU4QobU6STFB0P71PMvOGN5A",
]

INVALID_PLAYLIST_ID = "PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"


class TestPlaylistId:
    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_download(self, endpoint: Playlists, playlist_id: str) -> None:
        download_and_save(
            endpoint,
            playlist_id,
            lambda: endpoint.download(playlist_id=playlist_id),
        )

    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    def test_parse(self, endpoint: Playlists, playlist_id: str) -> None:
        playlists = parse_json(endpoint, playlist_id)
        assert [item.id for item in playlists.items] == [playlist_id]

    @pytest.mark.parametrize("playlist_id", PLAYLIST_IDS)
    @pytest.mark.parametrize(
        "load",
        [single_dict, parse_json, page_dicts, page_models],
        ids=["dict", "model", "dicts", "models"],
    )
    def test_extract_items(
        self,
        endpoint: Playlists,
        playlist_id: str,
        load: Callable[[Playlists, str], ExtractInput],
    ) -> None:
        items = endpoint.extract_items(load(endpoint, playlist_id))
        assert [item.id for item in items] == [playlist_id]

    def test_invalid_download(self, endpoint: Playlists) -> None:
        assert_error(
            endpoint,
            INVALID_PLAYLIST_ID,
            lambda: endpoint.download(playlist_id=INVALID_PLAYLIST_ID),
            PlaylistNotFoundError,
        )


class ChannelData(BaseModel):
    channel_id: str
    playlist_ids: set[str] = set()


CHANNELS: list[ChannelData] = [
    # Channel with a playlist. https://www.youtube.com/user/jawed
    ChannelData(
        channel_id="UC4QobU6STFB0P71PMvOGN5A",
        playlist_ids={"PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh"},
    ),
    # Channel with no playlists. https://www.youtube.com/@jawedNOW
    ChannelData(channel_id="UCPszuZ3hR89D4NqFd7g3mDQ"),
    # A "Topic" channel whose playlists are not returned by the API.
    # https://www.youtube.com/channel/UCo1DYcm1IZ9v3UPkpiAcgtg
    ChannelData(channel_id="UCo1DYcm1IZ9v3UPkpiAcgtg"),
]

INVALID_CHANNEL_ID = "UCCCCCCCCCCCCCCCCCCCCCCC"


class TestChannelId:
    @pytest.mark.parametrize("test_channel", CHANNELS)
    def test_download(
        self,
        endpoint: Playlists,
        test_channel: ChannelData,
    ) -> None:
        download_and_save(
            endpoint,
            test_channel.channel_id,
            lambda: endpoint.download(channel_id=test_channel.channel_id),
        )

    @pytest.mark.parametrize("test_channel", CHANNELS)
    def test_download_all(
        self,
        endpoint: Playlists,
        test_channel: ChannelData,
    ) -> None:
        download_and_save(
            endpoint,
            test_channel.channel_id,
            lambda: endpoint.download_all(channel_id=test_channel.channel_id),
            folder="PlaylistsAll",
        )

    @pytest.mark.parametrize("test_channel", CHANNELS)
    def test_parse(self, endpoint: Playlists, test_channel: ChannelData) -> None:
        playlists = parse_json(endpoint, test_channel.channel_id)
        assert test_channel.playlist_ids == {item.id for item in playlists.items}

    @pytest.mark.parametrize("test_channel", CHANNELS)
    @pytest.mark.parametrize(
        "load",
        [
            single_dict,
            parse_json,
            partial(page_dicts, folder="PlaylistsAll"),
            partial(page_models, folder="PlaylistsAll"),
        ],
        ids=["dict", "model", "dicts", "models"],
    )
    def test_extract_items(
        self,
        endpoint: Playlists,
        test_channel: ChannelData,
        load: Callable[[Playlists, str], ExtractInput],
    ) -> None:
        items = endpoint.extract_items(load(endpoint, test_channel.channel_id))
        assert test_channel.playlist_ids == {item.id for item in items}

    def test_invalid_download(self, endpoint: Playlists) -> None:
        assert_error(
            endpoint,
            INVALID_CHANNEL_ID,
            lambda: endpoint.download(channel_id=INVALID_CHANNEL_ID),
            ChannelNotFoundError,
        )

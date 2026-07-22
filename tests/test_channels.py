from __future__ import annotations

from itertools import combinations
from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from not_yt_dlapi.exceptions import ChannelNotFoundError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI
    from not_yt_dlapi.channel import Channel


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> Channel:
    return client.channel


class TestData(BaseModel):
    name: str
    kwargs: dict[str, str]
    channel_id: str | None = None


VALID_TEST_DATA = [
    # Every different parameter that can be used.
    TestData(
        name="UC4QobU6STFB0P71PMvOGN5A",
        kwargs={"channel_id": "UC4QobU6STFB0P71PMvOGN5A"},
        channel_id="UC4QobU6STFB0P71PMvOGN5A",
    ),
    TestData(
        name="@Google",
        kwargs={"channel_handle": "@Google"},
        channel_id="UCK8sQmJBp8GCxrOtXWBpyEA",
    ),
    TestData(
        name="MrBeast",
        kwargs={"channel_username": "MrBeast"},
        channel_id="UCgoFStVyEsm8tBZP5NC-aBQ",
    ),
]

INVALID_TEST_DATA = [
    # Every different parameter that can be used.
    TestData(
        name="UCCCCCCCCCCCCCCCCCCCCCCC",
        kwargs={"channel_id": "UCCCCCCCCCCCCCCCCCCCCCCC"},
    ),
    TestData(
        name="InvalidYouTubeHandleForTests",
        kwargs={"channel_handle": "InvalidYouTubeHandleForTests"},
    ),
    TestData(
        name="InvalidYouTubeUsernameFortests",
        kwargs={"channel_username": "InvalidYouTubeUsernameFortests"},
    ),
]

_ALL_PARAMS = {
    "channel_id": "UC4QobU6STFB0P71PMvOGN5A",
    "channel_handle": "@Google",
    "channel_username": "MrBeast",
}
INVALID_PARAM_COMBINATIONS = [
    dict(combo) for size in (2, 3) for combo in combinations(_ALL_PARAMS.items(), size)
]


@pytest.mark.parametrize("test_data", VALID_TEST_DATA, ids=lambda x: x.name)
def test_download(endpoint: Channel, test_data: TestData) -> None:
    download_and_save(
        endpoint,
        test_data.name,
        lambda: endpoint.download(**test_data.kwargs),
    )


@pytest.mark.parametrize("test_data", VALID_TEST_DATA, ids=lambda x: x.name)
def test_parse(endpoint: Channel, test_data: TestData) -> None:
    channels = parse_json(endpoint, test_data.name)
    assert len(channels.items) == 1
    assert channels.items[0].id == test_data.channel_id


@pytest.mark.parametrize("test_data", INVALID_TEST_DATA, ids=lambda x: x.name)
def test_invalid_download(endpoint: Channel, test_data: TestData) -> None:
    assert_error(
        endpoint,
        test_data.name,
        lambda: endpoint.download(**test_data.kwargs),
        ChannelNotFoundError,
    )


@pytest.mark.parametrize(
    "kwargs",
    INVALID_PARAM_COMBINATIONS,
    ids=lambda x: ",".join(x.keys()),
)
def test_invalid_combinations(endpoint: Channel, kwargs: dict[str, str]) -> None:
    with pytest.raises(ValueError, match="Invalid number of arguments"):
        endpoint.download(**kwargs)

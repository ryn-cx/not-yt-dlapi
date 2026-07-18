# TODO: Validate
from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Any

import pytest
from pydantic import BaseModel

from not_yt_dlapi.exceptions import PlaylistItemsNotFoundError
from not_yt_dlapi.playlists import DEFAULT_MAX_RESULTS
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
    from not_yt_dlapi.playlist_item import PlaylistItems
    from not_yt_dlapi.playlist_item.models import PlaylistItemsModel


# The input shapes extract_items accepts.
type ExtractInput = (
    PlaylistItemsModel
    | dict[str, Any]
    | list[PlaylistItemsModel]
    | list[dict[str, Any]]
)


@pytest.fixture(scope="session")
def endpoint(client: NotYTDLAPI) -> PlaylistItems:
    return client.playlist_items


class TestData(BaseModel):
    playlist_id: str
    video_ids: set[str] = set()


# TODO: Find a playlist with no videos.
# TODO: Find a playlist with 50+ videos.
VALID_TEST_DATA = [
    # User uploads (UU). https://www.youtube.com/playlist?list=UU4QobU6STFB0P71PMvOGN5A
    TestData(
        playlist_id="UU4QobU6STFB0P71PMvOGN5A",
        video_ids={"jNQXAC9IVRw"},
    ),
    # Playlist (PL). https://www.youtube.com/playlist?list=PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh
    TestData(
        playlist_id="PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh",
        video_ids={"lVI_J1cbFb4", "XAJEXUNmP5M", "VaLXzI92t9M", "jNQXAC9IVRw"},
    ),
    # Official list (OL). https://www.youtube.com/playlist?list=OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q
    TestData(
        playlist_id="OLAK5uy_nt1Nw4wT6I7VlzNknxTiIz3hfED0ttO8Q",
        video_ids={
            "hCcwCv3G1FQ",
            "R_clisSImS4",
            "Qer3lwd5hyA",
            "kZfz5UlsHlQ",
            "qFfjnPOXmUM",
            "bKTmpKPjJxs",
            "FQUI8KmRUw0",
            "16KSivdIGjQ",
            "JPOjiXoPmOk",
            "n2KOgQJbZAw",
            "HS1OUFCfFdY",
            "dgUHE8wWhiE",
            "eZNxD4NbxLA",
            "AUA3_lX6g-s",
        },
    ),
]

# Tests that exercise pagination need a playlist with more than one video.
MULTI_VIDEO_TEST_DATA = [data for data in VALID_TEST_DATA if len(data.video_ids) > 1]

INVALID_PLAYLIST_ID = "PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"


@pytest.mark.parametrize(
    "valid_test_data",
    VALID_TEST_DATA,
    ids=lambda x: x.playlist_id,
)
def test_download(
    endpoint: PlaylistItems,
    valid_test_data: TestData,
) -> None:
    download_and_save(
        endpoint,
        valid_test_data.playlist_id,
        lambda: endpoint.download(valid_test_data.playlist_id),
    )


@pytest.mark.parametrize(
    "valid_test_data",
    MULTI_VIDEO_TEST_DATA,
    ids=lambda x: x.playlist_id,
)
def test_download_all(
    endpoint: PlaylistItems,
    valid_test_data: TestData,
) -> None:
    video_count = len(valid_test_data.video_ids)
    download_and_save(
        endpoint,
        valid_test_data.playlist_id,
        lambda: endpoint.download_all_pages(
            valid_test_data.playlist_id,
            max_results=min(video_count - 1, DEFAULT_MAX_RESULTS),
        ),
        folder="PlaylistItemsAll",
    )


@pytest.mark.parametrize(
    "valid_test_data",
    VALID_TEST_DATA,
    ids=lambda x: x.playlist_id,
)
def test_parse(
    endpoint: PlaylistItems,
    valid_test_data: TestData,
) -> None:
    data = parse_json(endpoint, valid_test_data.playlist_id)
    video_ids = {item.content_details.video_id for item in data.items}
    assert valid_test_data.video_ids == video_ids


EXTRACT_CASES = [
    pytest.param(data, load, id=f"{name}-{data.playlist_id}")
    for name, dataset, load in (
        ("dict", VALID_TEST_DATA, single_dict),
        ("model", VALID_TEST_DATA, parse_json),
        (
            "dicts",
            MULTI_VIDEO_TEST_DATA,
            partial(page_dicts, folder="PlaylistItemsAll"),
        ),
        (
            "models",
            MULTI_VIDEO_TEST_DATA,
            partial(page_models, folder="PlaylistItemsAll"),
        ),
    )
    for data in dataset
]


@pytest.mark.parametrize(("valid_test_data", "load"), EXTRACT_CASES)
def test_extract_items(
    endpoint: PlaylistItems,
    valid_test_data: TestData,
    load: Callable[[PlaylistItems, str], ExtractInput],
) -> None:
    items = endpoint.extract_items(load(endpoint, valid_test_data.playlist_id))
    video_ids = {item.content_details.video_id for item in items}
    assert valid_test_data.video_ids == video_ids


def test_invalid_download(endpoint: PlaylistItems) -> None:
    assert_error(
        endpoint,
        INVALID_PLAYLIST_ID,
        lambda: endpoint.download(INVALID_PLAYLIST_ID),
        PlaylistItemsNotFoundError,
    )


@pytest.mark.parametrize("part", [None, "part_value"])
@pytest.mark.parametrize("max_results", [None, 10])
def test_log_id(
    endpoint: PlaylistItems,
    max_results: int | None,
    part: str | None,
) -> None:
    playlist_id = "playlist_id_value"
    kwargs: dict[str, Any] = {}
    expected = f"PlaylistItems playlist_id='{playlist_id}'"
    if max_results is not None:
        kwargs["max_results"] = max_results
        expected += f" max_results={max_results}"
    if part is not None:
        kwargs["part"] = part
        expected += f" part='{part}'"
    assert endpoint.get_log_id(playlist_id, **kwargs) == expected

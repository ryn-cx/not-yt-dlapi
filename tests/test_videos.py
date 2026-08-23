# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import APIError
from not_yt_dlapi.videos import MAX_IDS
from not_yt_dlapi.videos.models import VideosModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

BAD_REQUEST = 400
"""What the API answers a request carrying more ids than it takes with."""

LONG_PLAYLIST_ID = "PLbpi6ZahtOH4kNyb9pjnMYg4PB7qiljiH"
"""A playlist of 76 videos, which is more than one request can ask about.

No video is in it twice, so its ids are 76 distinct ids rather than fewer
repeated. A playlist that repeats one would be answered for in a single request
even though it lists more than fifty items, and so would not show the limit.
"""

LONG_PLAYLIST_COUNT = 76
"""How many videos that playlist holds, which takes two requests to gather."""

SEVERAL_VIDEO_IDS = ("jNQXAC9IVRw", "LY8Wi7XRXCA")
"""Asking about several videos at once is one request answering with a list."""

VIDEO_IDS = [
    # https://www.youtube.com/watch?v=jNQXAC9IVRw
    pytest.param("jNQXAC9IVRw", id="video"),
    # It's my fault for choosing this show as a joke...
    # https://www.youtube.com/watch?v=6JTFYuloLFM
    pytest.param("6JTFYuloLFM", id="no view count"),
    # An id nothing is under is answered with what was found, which is nothing.
    pytest.param("00000000000", id="invalid video"),
    # https://www.youtube.com/watch?v=zKQGAv8gtBA
    pytest.param("zKQGAv8gtBA", id="free movie"),
    # https://www.youtube.com/watch?v=g1eZjGhN8oo
    pytest.param("g1eZjGhN8oo", id="paid movie"),
    pytest.param("+".join(SEVERAL_VIDEO_IDS), id="several videos at once"),
]


# TODO: Validate
class VideosTest(RecordedEndpoint):
    MODEL = VideosModel
    # etag changes whenever anything in the response does.
    IGNORED = ("VideosModel.etag", "Video.etag")
    SORTED = (
        "VideoTopicDetails.topic_ids",
        "VideoTopicDetails.relevant_topic_ids",
        "VideoTopicDetails.topic_categories",
    )
    # Counts wobble in both directions between downloads, so only their type is
    # held against the recording.
    SAME_TYPE = (
        "VideoStatistics.view_count",
        "VideoStatistics.like_count",
        "VideoStatistics.comment_count",
        "VideoStatistics.favorite_count",
    )


# TODO: Validate
def playlist_video_ids(client: NotYTDLAPI, playlist_id: str) -> list[str]:
    """Return the id of every video in a playlist, however many pages it takes."""
    pages = client.playlist_items.download_all(playlist_id)
    return [
        item.content_details.video_id
        for item in client.playlist_items.extract_items(pages)
    ]


# TODO: Validate
@pytest.mark.parametrize("video_ids", VIDEO_IDS)
def test_download(client: NotYTDLAPI, video_ids: str) -> None:
    VideosTest.download_test(
        video_ids,
        lambda: client.videos.download(video_ids.split("+")),
    )


# TODO: Validate
@pytest.mark.parametrize("video_ids", VIDEO_IDS)
def test_parse(client: NotYTDLAPI, video_ids: str) -> None:
    videos = client.videos.load(VideosTest.recorded_content(video_ids))
    assert videos.kind == "youtube#videoListResponse"
    VideosTest.parse_test(video_ids)


# TODO: Validate
def test_download_max_ids(client: NotYTDLAPI) -> None:
    # Fifty ids, which the API answers rather than cutting short.
    video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)[:MAX_IDS]
    VideosTest.download_test(
        f"{LONG_PLAYLIST_ID}-{MAX_IDS}",
        lambda: client.videos.download(video_ids),
    )


# TODO: Validate
def test_parse_max_ids() -> None:
    VideosTest.parse_test(f"{LONG_PLAYLIST_ID}-{MAX_IDS}")


# TODO: Validate
def test_download_all(client: NotYTDLAPI) -> None:
    # What one request refuses, `download_all` asks for fifty at a time.
    def batched() -> list[str]:
        video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)
        assert len(video_ids) == LONG_PLAYLIST_COUNT
        return client.videos.download_all(video_ids)

    VideosTest.download_test(f"{LONG_PLAYLIST_ID}-all", batched, "Multipage")


# TODO: Validate
def test_parse_all(client: NotYTDLAPI) -> None:
    pages = VideosTest.recorded_documents(f"{LONG_PLAYLIST_ID}-all", "Multipage")
    videos = client.videos.extract_items(pages)
    assert len(videos) > MAX_IDS
    VideosTest.parse_test(f"{LONG_PLAYLIST_ID}-all", "Multipage")


# TODO: Validate
def test_download_too_many_ids(client: NotYTDLAPI) -> None:
    # More ids than one request takes is refused rather than cut short, so
    # anything wanting the whole playlist has to ask in batches.
    video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)
    assert len(video_ids) == LONG_PLAYLIST_COUNT

    with pytest.raises(APIError) as error:
        client.videos.download(video_ids)

    assert error.value.code == BAD_REQUEST
    assert error.value.error["errors"][0]["reason"] == "invalidFilters"

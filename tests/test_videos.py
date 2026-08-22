# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from not_yt_dlapi.exceptions import APIError
from not_yt_dlapi.videos import Videos
from not_yt_dlapi.videos.models import VideoListResponse
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

LONG_PLAYLIST_ID = "PLbpi6ZahtOH4kNyb9pjnMYg4PB7qiljiH"
"""A playlist of 76 videos, which is more than one request can ask about.

No video is in it twice, so its ids are 76 distinct ids rather than fewer
repeated. A playlist that repeats one would be answered for in a single request
even though it lists more than fifty items, and so would not show the limit.
"""

LONG_PLAYLIST_COUNT = 76
"""How many videos that playlist holds, which takes two pages to gather."""

MAX_IDS = 50
"""The most ids one request takes. Past this the API refuses rather than cuts."""


# TODO: Validate
def playlist_video_ids(client: NotYTDLAPI, playlist_id: str) -> list[str]:
    """Return the id of every video in a playlist, however many pages it takes."""
    return [
        response.items[0].content_details.video_id
        for response in client.playlist_items.list_all(playlist_id)
    ]


# TODO: Validate
class VideoTest(RecordedEndpoint):
    ENDPOINT = Videos
    # etag changes whenever anything in the response does.
    IGNORED = ("VideoListResponse.etag", "Video.etag")
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
class TestList(VideoTest):
    MODEL = VideoListResponse
    VIDEO_IDS = (
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
    )

    SEVERAL_VIDEO_IDS = ("jNQXAC9IVRw", "LY8Wi7XRXCA")
    SEVERAL_VIDEOS = "+".join(SEVERAL_VIDEO_IDS)
    """Asking about several videos at once is one request answering with a list."""

    MAX_IDS_NAME = f"{LONG_PLAYLIST_ID}-{MAX_IDS}"
    """Fifty ids, which the API answers rather than cutting short."""

    # TODO: Validate
    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_download(self, client: NotYTDLAPI, video_id: str) -> None:
        self.download_test(video_id, lambda: client.videos.list(video_id))

    # TODO: Validate
    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_parse(self, video_id: str) -> None:
        self.parse_test(video_id)

    # TODO: Validate
    def test_download_several_videos(self, client: NotYTDLAPI) -> None:
        self.download_test(
            self.SEVERAL_VIDEOS,
            lambda: client.videos.list(self.SEVERAL_VIDEO_IDS),
        )

    # TODO: Validate
    def test_parse_several_videos(self) -> None:
        self.parse_test(self.SEVERAL_VIDEOS)

    # TODO: Validate
    def test_download_max_ids(self, client: NotYTDLAPI) -> None:
        video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)[:MAX_IDS]
        self.download_test(self.MAX_IDS_NAME, lambda: client.videos.list(video_ids))

    # TODO: Validate
    def test_parse_max_ids(self) -> None:
        self.parse_test(self.MAX_IDS_NAME)

    # TODO: Validate
    def test_too_many_ids(self, client: NotYTDLAPI) -> None:
        # More ids than one request takes is refused rather than cut short, so
        # anything wanting the whole playlist has to ask in batches.
        video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)
        assert len(video_ids) == LONG_PLAYLIST_COUNT

        with pytest.raises(APIError) as error:
            client.videos.list(video_ids)

        assert error.value.code == 400  # noqa: PLR2004 - The status code is the point.
        assert error.value.error["errors"][0]["reason"] == "invalidFilters"


# TODO: Validate
class TestListAll(VideoTest):
    MODEL = VideoListResponse
    NAME = f"{LONG_PLAYLIST_ID}-all"

    # TODO: Validate
    def test_download(self, client: NotYTDLAPI) -> None:
        # What one request refuses, `list_all` asks for fifty at a time. Every
        # video comes back in a response of its own, and a playlist can list a
        # video that has since been deleted, so fewer come back than went in.
        def batched() -> list[VideoListResponse]:
            video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)
            assert len(video_ids) == LONG_PLAYLIST_COUNT
            return client.videos.list_all(video_ids)

        self.download_test(self.NAME, batched)

    # TODO: Validate
    def test_parse(self) -> None:
        self.parse_test(self.NAME)

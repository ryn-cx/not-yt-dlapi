# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, Any

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


def playlist_video_ids(client: NotYTDLAPI, playlist_id: str) -> list[str]:
    """Return the id of every video in a playlist, however many pages it takes."""
    return [
        response.items[0].content_details.video_id
        for response in client.playlist_items.list_all(playlist_id)
    ]


# TODO: Validate
class VideoTest(RecordedEndpoint):
    ENDPOINT = Videos


# TODO: Validate
class TestList:
    """Test `videos.list`."""

    # TODO: Validate
    class TestVideo(VideoTest):
        VIDEO_ID = "jNQXAC9IVRw"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.VIDEO_ID,
                lambda: client.videos.list(self.VIDEO_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.VIDEO_ID, VideoListResponse)

    # TODO: Validate
    class TestVideoWithoutViewCount(VideoTest):
        VIDEO_ID = "6JTFYuloLFM"
        """It's my fault for choosing this show as a joke...
        https://www.youtube.com/watch?v=6JTFYuloLFM"""

        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.VIDEO_ID,
                lambda: client.videos.list(self.VIDEO_ID).raw,
            )

        def test_parse(self) -> None:
            self.parse_test(self.VIDEO_ID, VideoListResponse)

    # TODO: Validate
    class TestMultipleVideos(VideoTest):
        """Asking about several videos at once is one request answering with a list."""

        VIDEO_IDS = ("jNQXAC9IVRw", "LY8Wi7XRXCA")
        NAME = "+".join(VIDEO_IDS)

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(self.NAME, lambda: client.videos.list(self.VIDEO_IDS).raw)

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.NAME, VideoListResponse)

    # TODO: Validate
    class TestMostIdsOneRequestTakes(VideoTest):
        """The most ids one request takes, gathered from a playlist and asked at once.

        Fifty ids are taken where fifty-one are refused, which is what asking about
        exactly fifty shows: the request is answered rather than turned down.
        """

        NAME = f"{LONG_PLAYLIST_ID}-{MAX_IDS}"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)[:MAX_IDS]
            self.record_test(self.NAME, lambda: client.videos.list(video_ids).raw)

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.NAME, VideoListResponse)

        # TODO: Validate
        def test_no_more_came_back_than_was_asked_about(self) -> None:
            """Fifty ids are answered for by no more than fifty videos.

            Not every id is answered for. A playlist can list a video that has since
            been deleted or made private, and its id is asked about like any other
            but nothing comes back for it, so fifty ids give fewer than fifty
            videos.
            """
            response = VideoListResponse.from_response(self.recorded_content(self.NAME))

            assert 0 < len(response.items) <= MAX_IDS

    # TODO: Validate
    class TestMoreIdsThanOneRequestTakes:
        """More ids than one request takes is refused rather than cut short.

        The playlist holds more videos than the API will take ids for, so asking
        about every one of them at once is answered with a 400 rather than with the
        first fifty. Anything wanting the whole playlist has to ask in batches,
        which is what `list_all` does.

        There is no response to record, only the refusal.
        """

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)
            assert len(video_ids) == LONG_PLAYLIST_COUNT

            with pytest.raises(APIError) as error:
                client.videos.list(video_ids)

            assert error.value.code == 400  # noqa: PLR2004 - The status code is the point.
            assert error.value.error["errors"][0]["reason"] == "invalidFilters"

    # TODO: Validate
    class TestUnknownVideo(VideoTest):
        """An id nothing is under is answered with what was found, which is nothing."""

        VIDEO_ID = "00000000000"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            self.record_test(
                self.VIDEO_ID,
                lambda: client.videos.list(self.VIDEO_ID).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.VIDEO_ID, VideoListResponse)


# TODO: Validate
class TestListAll:
    """Test `videos.list_all`."""

    # TODO: Validate
    class TestListAllAsksInBatches(VideoTest):
        """What one request refuses, `list_all` asks for fifty at a time.

        Every video that comes back comes back in a response of its own, and more
        come back than one request would have taken, so both batches were asked for
        rather than only the first.

        A playlist can list a video that has since been deleted or made private. The
        item stays in the playlist but the video is not answered for, so fewer come
        back than went in. What comes back is in the API's own order rather than the
        order it was asked about, so only the set of them is checked.

        What is recorded is what the batches gave, so they are asked for once
        rather than on every run.
        """

        NAME = f"{LONG_PLAYLIST_ID}-all"

        # TODO: Validate
        def test_download(self, client: NotYTDLAPI) -> None:
            def batched() -> list[dict[str, Any]]:
                video_ids = playlist_video_ids(client, LONG_PLAYLIST_ID)
                assert len(video_ids) == LONG_PLAYLIST_COUNT
                return [response.raw for response in client.videos.list_all(video_ids)]

            self.record_test(self.NAME, batched)

        # TODO: Validate
        def test_each_video_arrived_once(self) -> None:
            """Every video came back in a response of its own, and only once."""
            responses = self.recorded_content(self.NAME)
            answered = [response["items"][0]["id"] for response in responses]

            assert all(len(response["items"]) == 1 for response in responses)
            assert len(answered) > MAX_IDS
            assert len(set(answered)) == len(answered)

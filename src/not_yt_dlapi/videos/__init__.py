# TODO: Validate
"""A `video` resource represents a YouTube video.

https://developers.google.com/youtube/v3/docs/videos
"""

from __future__ import annotations

from itertools import batched
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.videos.models import VideoListResponse

if TYPE_CHECKING:
    import builtins
    from collections.abc import Sequence

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = (
    "contentDetails,"
    "id,"
    "liveStreamingDetails,"
    "localizations,"
    "paidProductPlacementDetails,"
    "player,"
    "recordingDetails,"
    "snippet,"
    "statistics,"
    "status,"
    "topicDetails"
)


# TODO: Validate
class Videos(BaseEndpoint):
    """A `video` resource represents a YouTube video.

    https://developers.google.com/youtube/v3/docs/videos
    """

    # TODO: Validate
    def list(self, video_ids: str | Sequence[str]) -> VideoListResponse:
        """Videos: list.

        Returns a list of videos that match the API request parameters.
        """
        log_id = self.get_log_id(self.list, locals())
        ids = [video_ids] if isinstance(video_ids, str) else list(video_ids)
        data = self._client.download(
            "videos",
            {"part": PART, "id": ",".join(ids)},
            log_id,
        )
        return VideoListResponse.from_response(data)

    # TODO: Validate
    def list_all(self, video_ids: Sequence[str]) -> builtins.list[VideoListResponse]:
        """list() alternative that automatically batches the VideoListResponse."""
        pages = (self.list(batch).raw for batch in batched(video_ids, 50, strict=False))
        return self.split(VideoListResponse.from_response, pages)

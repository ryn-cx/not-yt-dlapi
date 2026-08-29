# TODO: Validate
"""Contains the Videos class."""

from __future__ import annotations

from itertools import batched
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.videos.models import VideosModel, model_validate_json

if TYPE_CHECKING:
    from collections.abc import Sequence

    from not_yt_dlapi.videos.models import Item

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
"""Every part a key can ask for, which is what is always asked for."""

MAX_IDS = 50
"""The most ids one request takes. Past this the API refuses rather than cuts."""


# TODO: Validate
class Videos(BaseEndpoint):
    """A `video` resource represents a YouTube video.

    Source: https://developers.google.com/youtube/v3/docs/videos

    Example request:
        - GET /youtube/v3/videos?
            - part={part}&
            - id={video_ids}&
            - key=__REDACTED__
            - HTTP/2
        - Host: www.googleapis.com
    """

    # TODO: Validate
    def __call__(self, video_ids: str | Sequence[str]) -> VideosModel:
        """Look the videos up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(video_ids), log_id)

    # TODO: Validate
    def download(self, video_ids: str | Sequence[str]) -> str:
        """Download the videos file.

        An id nothing is under is not an error to the API: it answers with the
        videos it did find and says nothing about the rest.
        """
        log_id = self.get_log_id(self.download, locals())
        ids = [video_ids] if isinstance(video_ids, str) else list(video_ids)
        return self._client.download(
            endpoint="videos",
            params={"part": PART, "id": ",".join(ids)},
            headers={},
            log_id=log_id,
        )

    # TODO: Validate
    def download_all(self, video_ids: Sequence[str]) -> list[str]:
        """Download every video asked for, fifty ids to a request.

        One request takes fifty ids and refuses more, so the ids are asked
        about fifty at a time and every answer is returned.
        """
        return [
            self.download(batch) for batch in batched(video_ids, MAX_IDS, strict=False)
        ]

    # TODO: Validate
    def download_merged(self, video_ids: Sequence[str]) -> str:
        """Download every video asked for as a single file.

        The requests the ids were split across are put together into one file
        holding every video, which is what was asked for written the way one
        answer is, rather than the answers themselves.
        """
        return self.merge_pages(self.download_all(video_ids))

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> VideosModel:
        """Read a downloaded videos file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[VideosModel]:
        """Read the files `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    # TODO: Validate
    def extract_items(self, datas: Sequence[VideosModel | str]) -> list[Item]:
        """Extract the items from one or more files."""
        return [
            item
            for entry in datas
            for item in (
                entry if isinstance(entry, VideosModel) else self.load(entry)
            ).items
        ]

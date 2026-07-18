from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.exceptions import VideoNotFoundError
from not_yt_dlapi.video.models import VideosModel

if TYPE_CHECKING:
    from not_yt_dlapi.video.models import Item

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
DEFAULT_MAX_RESULTS = 50


class Videos(BaseEndpoint[VideosModel]):
    _response_model = VideosModel

    def get_log_id(self, video_ids: list[str], part: str = PART) -> str:
        return self.append_non_default_args(
            f"{self.__class__.__name__} {video_ids=}",
            part=(part, PART),
        )

    def download(
        self,
        video_ids: str | list[str],
        part: str = PART,
    ) -> dict[str, Any]:
        video_ids = [video_ids] if isinstance(video_ids, str) else video_ids

        log_id = self.get_log_id(video_ids, part)
        response = self._client.download(
            "videos",
            params={"part": part, "id": ",".join(video_ids)},
            log_id=log_id,
        )
        found_ids = {item["id"] for item in response.get("items", [])}
        missing_ids = [video_id for video_id in video_ids if video_id not in found_ids]
        if missing_ids:
            msg = f"Video not found: {', '.join(missing_ids)}"
            raise VideoNotFoundError(msg, response)
        return response

    def download_and_parse(
        self,
        video_ids: str | list[str],
        part: str = PART,
    ) -> VideosModel:
        return self.parse(self.download(video_ids, part))

    # TODO: Consider making a generalized version of this function for downloading
    # values from a list if more lists are ever added.
    def download_all(
        self,
        video_ids: list[str],
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> list[dict[str, Any]]:
        return [
            self.download(video_ids[i : i + max_results], part)
            for i in range(0, len(video_ids), max_results)
        ]

    def download_and_parse_all(
        self,
        video_ids: list[str],
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> list[VideosModel]:
        return [
            self.parse(page) for page in self.download_all(video_ids, max_results, part)
        ]

    @staticmethod
    def extract_items(
        files: VideosModel | dict[str, Any] | list[VideosModel] | list[dict[str, Any]],
    ) -> list[Item]:
        if isinstance(files, (dict)):
            files = [files]

        if isinstance(files, (VideosModel)):
            files = [files]

        models = [
            page if isinstance(page, VideosModel) else VideosModel.model_validate(page)
            for page in files
        ]
        return [item for model in models for item in model.items]

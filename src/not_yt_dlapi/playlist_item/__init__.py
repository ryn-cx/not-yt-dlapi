# TODO: Validate

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.exceptions import PlaylistNotFoundError
from not_yt_dlapi.playlist_item.models import PlaylistItemsModel

if TYPE_CHECKING:
    from not_yt_dlapi.playlist_item.models import Item

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,snippet,status"
DEFAULT_MAX_RESULTS = 50


class PlaylistItems(BaseEndpoint[PlaylistItemsModel]):
    _response_model = PlaylistItemsModel

    def get_log_id(
        self,
        playlist_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> str:
        return self.append_non_default_args(
            f"{self.__class__.__name__} {playlist_id=}",
            max_results=(max_results, DEFAULT_MAX_RESULTS),
            part=(part, PART),
        )

    def download(
        self,
        playlist_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(playlist_id, max_results, part)
        return self._client.download(
            "playlistItems",
            params={
                "part": part,
                "playlistId": playlist_id,
                "maxResults": max_results,
            },
            not_found_error=PlaylistNotFoundError,
            log_id=log_id,
        )

    def download_all_pages(
        self,
        playlist_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> list[dict[str, Any]]:
        log_id = self.get_log_id(playlist_id, max_results, part)
        return self._client.download_all_pages(
            "playlistItems",
            {"part": part, "playlistId": playlist_id, "maxResults": max_results},
            log_id,
            not_found_error=PlaylistNotFoundError,
        )

    def download_and_parse(
        self,
        playlist_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> PlaylistItemsModel:
        response = self.download(playlist_id, max_results, part)
        return self.parse(response)

    def download_and_parse_all_pages(
        self,
        playlist_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> list[PlaylistItemsModel]:
        return [
            self.parse(responses)
            for responses in self.download_all_pages(playlist_id, max_results, part)
        ]

    @staticmethod
    def extract_items(
        files: PlaylistItemsModel
        | dict[str, Any]
        | list[PlaylistItemsModel]
        | list[dict[str, Any]],
    ) -> list[Item]:
        if isinstance(files, (dict)):
            files = [files]

        if isinstance(files, (PlaylistItemsModel)):
            files = [files]

        models = [
            page
            if isinstance(page, PlaylistItemsModel)
            else PlaylistItemsModel.model_validate(page)
            for page in files
        ]
        return [item for model in models for item in model.items]

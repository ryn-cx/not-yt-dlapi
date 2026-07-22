from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.exceptions import ChannelNotFoundError, PlaylistNotFoundError
from not_yt_dlapi.playlists.models import PlaylistsModel

if TYPE_CHECKING:
    from not_yt_dlapi.playlists.models import Item

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,localizations,player,snippet,status"
DEFAULT_MAX_RESULTS = 50


class Playlists(BaseEndpoint[PlaylistsModel]):
    _response_model = PlaylistsModel

    @overload
    def download(
        self,
        *,
        playlist_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> dict[str, Any]: ...
    @overload
    def download(
        self,
        *,
        channel_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> dict[str, Any]: ...
    def download(
        self,
        *,
        playlist_id: str | None = None,
        channel_id: str | None = None,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        params = self.get_single_arg(
            id=playlist_id,
            channelId=channel_id,
        )
        params["part"] = part
        params["maxResults"] = max_results

        # As far as I can tell playlists will always complete the download but return an
        # empty result but the channel will actually raise a 404 error.
        response = self._client.download(
            path="playlists",
            params=params,
            log_id=log_id,
            not_found_error=ChannelNotFoundError,
        )
        if not response.get("items"):
            msg = f"Playlist not found: {playlist_id}"
            raise PlaylistNotFoundError(msg, response)
        return response

    def download_all(
        self,
        channel_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> list[dict[str, Any]]:
        log_id = self.get_log_id(self.download_all, locals())
        return self._client.download_all_pages(
            "playlists",
            {"part": part, "channelId": channel_id, "maxResults": max_results},
            log_id,
            not_found_error=ChannelNotFoundError,
        )

    @overload
    def download_and_parse(
        self,
        *,
        playlist_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> PlaylistsModel: ...
    @overload
    def download_and_parse(
        self,
        *,
        channel_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> PlaylistsModel: ...
    def download_and_parse(
        self,
        *,
        playlist_id: str | None = None,
        channel_id: str | None = None,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> PlaylistsModel:
        single_arg = self.get_single_arg(
            playlist_id=playlist_id,
            channel_id=channel_id,
        )
        return self.parse(
            self.download(**single_arg, max_results=max_results, part=part),
        )

    def download_and_parse_all(
        self,
        channel_id: str,
        max_results: int = DEFAULT_MAX_RESULTS,
        part: str = PART,
    ) -> list[PlaylistsModel]:
        return [
            self.parse(file_content)
            for file_content in self.download_all(channel_id, max_results, part)
        ]

    @staticmethod
    def extract_items(
        files: PlaylistsModel
        | dict[str, Any]
        | list[PlaylistsModel]
        | list[dict[str, Any]],
    ) -> list[Item]:
        if isinstance(files, (dict)):
            files = [files]

        if isinstance(files, (PlaylistsModel)):
            files = [files]

        models = [
            page
            if isinstance(page, PlaylistsModel)
            else PlaylistsModel.model_validate(page)
            for page in files
        ]
        return [item for model in models for item in model.items]

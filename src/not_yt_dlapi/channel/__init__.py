from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.channel.models import ChannelsModel
from not_yt_dlapi.exceptions import ChannelNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = (
    "brandingSettings,"
    "contentDetails,"
    "contentOwnerDetails,"
    "id,"
    "localizations,"
    "snippet,"
    "statistics,"
    "status,"
    "topicDetails"
)


class Channel(BaseEndpoint[ChannelsModel]):
    _response_model = ChannelsModel

    def get_log_id(
        self,
        *,
        channel_id: str | None = None,
        channel_handle: str | None = None,
        channel_username: str | None = None,
        part: str = PART,
    ) -> str:
        return self.append_non_default_args(
            f"{self.__class__.__name__}",
            channel_id=(channel_id, None),
            channel_handle=(channel_handle, None),
            channel_username=(channel_username, None),
            part=(part, PART),
        )

    @overload
    def download(self, *, channel_id: str, part: str = PART) -> dict[str, Any]: ...
    @overload
    def download(self, *, channel_handle: str, part: str = PART) -> dict[str, Any]: ...
    @overload
    def download(
        self,
        *,
        channel_username: str,
        part: str = PART,
    ) -> dict[str, Any]: ...
    def download(
        self,
        *,
        channel_id: str | None = None,
        channel_handle: str | None = None,
        channel_username: str | None = None,
        part: str = PART,
    ) -> dict[str, Any]:
        params = self.get_single_arg(
            id=channel_id,
            for_handle=channel_handle,
            for_username=channel_username,
        )
        log_id = self.get_log_id(
            channel_id=channel_id,
            channel_handle=channel_handle,
            channel_username=channel_username,
            part=part,
        )

        params["part"] = part

        response = self._client.download("channels", params, log_id)
        if "items" not in response:
            identifier = log_id.removeprefix(f"{self.__class__.__name__} ")
            msg = f"Channel not found: {identifier}"
            raise ChannelNotFoundError(msg, response)
        return response

    @overload
    def download_and_parse(
        self,
        *,
        channel_id: str,
        part: str = PART,
    ) -> ChannelsModel: ...
    @overload
    def download_and_parse(
        self,
        *,
        channel_handle: str,
        part: str = PART,
    ) -> ChannelsModel: ...
    @overload
    def download_and_parse(
        self,
        *,
        channel_username: str,
        part: str = PART,
    ) -> ChannelsModel: ...
    def download_and_parse(
        self,
        *,
        channel_id: str | None = None,
        channel_handle: str | None = None,
        channel_username: str | None = None,
        part: str = PART,
    ) -> ChannelsModel:
        params = self.get_single_arg(
            channel_id=channel_id,
            channel_handle=channel_handle,
            channel_username=channel_username,
        )
        response = self.download(**params, part=part)
        return self.parse(response)

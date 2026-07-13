# TODO: Validate
"""Contains the Channels class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.channel.models import ChannelsModel
from not_yt_dlapi.constants import BASE_URL
from not_yt_dlapi.exceptions import (
    HTTP_NOT_FOUND,
    ChannelNotFoundError,
    NotYTDLAPIError,
)

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


class Channels(BaseEndpoint[ChannelsModel]):
    """Manage the channels file."""

    _response_model = ChannelsModel

    def download(
        self,
        *,
        channel_id: str | None = None,
        handle: str | None = None,
        username: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the channels file."""
        if (channel_id is None) == (handle is None) == (username is None):
            msg = "Exactly one of channel_id, handle, or username must be provided."
            raise ValueError(msg)

        params: dict[str, str] = {"part": PART}
        if channel_id is not None:
            params["id"] = channel_id
            logger.info("Downloading: %s", f"{self.__class__.__name__} {channel_id}")
        elif handle is not None:
            params["forHandle"] = handle
            logger.info("Downloading: %s", f"{self.__class__.__name__} {handle}")
        elif username is not None:
            params["forUsername"] = username
            logger.info("Downloading: %s", f"{self.__class__.__name__} {username}")

        output = self._client.authenticated_get(
            f"{BASE_URL}/channels",
            params=params,
        ).json()

        if "error" in output:
            msg = output["error"]["message"]
            if output["error"]["code"] == HTTP_NOT_FOUND:
                raise ChannelNotFoundError(msg)
            raise NotYTDLAPIError(msg)

        return output

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response.get("items"))

    def get(
        self,
        *,
        channel_id: str | None = None,
        handle: str | None = None,
        username: str | None = None,
    ) -> ChannelsModel:
        """Downloads and parses the channels file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        data = self.download(channel_id=channel_id, handle=handle, username=username)
        return self._parse_or_raise(
            data,
            f"{self.__class__.__name__} {channel_id or handle or username}",
        )

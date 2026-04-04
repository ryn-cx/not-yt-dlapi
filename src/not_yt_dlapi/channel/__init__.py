"""Channel API endpoint."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from not_yt_dlapi.base_api_endpoint import BaseEndpoint, generate_timestamp
from not_yt_dlapi.channel.models import ChannelModel
from not_yt_dlapi.constants import BASE_URL
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


class Channels(BaseEndpoint[ChannelModel]):
    """Provides methods to download, parse, and retrieve channel data."""

    _response_model = ChannelModel

    def download(
        self,
        *,
        channel_id: str | None = None,
        handle: str | None = None,
    ) -> dict[str, Any]:
        """Downloads channel data by channel ID or YouTube handle.

        Args:
            channel_id: The ID of the channel to download.
            handle: The YouTube handle to download.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        if (channel_id is None) == (handle is None):
            msg = "Exactly one of channel_id or handle must be provided."
            raise ValueError(msg)

        params: dict[str, str] = {"part": PART, "key": self._client.api_key}
        if channel_id is not None:
            params["id"] = channel_id
            logger.info("Downloading Channel: %s", channel_id)
        elif handle is not None:
            params["forHandle"] = handle
            logger.info("Downloading Channel by handle: %s", handle)

        output = self._client.get_around.get(
            f"{BASE_URL}/channels",
            params=params,
        ).json()
        output["not_yt_dlapi"] = {
            "channel_id": channel_id or handle,
            "part": PART,
            "timestamp": generate_timestamp(),
        }
        return output

    def get(
        self,
        *,
        channel_id: str | None = None,
        handle: str | None = None,
    ) -> ChannelModel:
        """Downloads and parses channel data by channel ID or YouTube handle.

        Args:
            channel_id: The ID of the channel to get.
            handle: The YouTube handle to get.

        Returns:
            A ChannelModel containing the parsed data.
        """
        response = self.download(channel_id=channel_id, handle=handle)
        if not response.get("items"):
            identifier = channel_id or handle
            msg = f"Channel '{identifier}' not found."
            raise ChannelNotFoundError(msg)

        return self.parse(response)

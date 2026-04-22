"""Channel API endpoint."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from good_ass_pydantic_integrator import CustomSerializer

from not_yt_dlapi.base_api_endpoint import BaseEndpoint, generate_timestamp
from not_yt_dlapi.channel.models import ChannelModel
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


class Channels(BaseEndpoint[ChannelModel]):
    """Provides methods to download, parse, and retrieve channel data."""

    _response_model = ChannelModel

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="Snippet",
                field_name="published_at",
                serializer_code="return value.strftime("
                '"%Y-%m-%dT%H:%M:%S.%f"'
                ').rstrip("0").rstrip(".") + "Z"',
                output_type="str",
            ),
        ]

    def download(
        self,
        *,
        channel_id: str | None = None,
        handle: str | None = None,
        username: str | None = None,
    ) -> dict[str, Any]:
        """Downloads channel data by channel ID or YouTube handle.

        Args:
            channel_id: The ID of the channel to download.
            handle: The YouTube handle to download.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        if (channel_id is None) == (handle is None) == (username is None):
            msg = "Exactly one of channel_id, handle, or username must be provided."
            raise ValueError(msg)

        params: dict[str, str] = {"part": PART, "key": self._client.api_key}
        if channel_id is not None:
            params["id"] = channel_id
            logger.info("Downloading Channel: %s", channel_id)
        elif handle is not None:
            params["forHandle"] = handle
            logger.info("Downloading Channel by handle: %s", handle)
        elif username is not None:
            params["forUsername"] = username
            logger.info("Downloading Channel by username: %s", username)

        output = self._client.get_around.get(
            f"{BASE_URL}/channels",
            params=params,
        ).json()
        output["not_yt_dlapi"] = {
            "part": PART,
            "timestamp": generate_timestamp(),
        }

        if channel_id:
            output["not_yt_dlapi"]["channel_id"] = channel_id
        if handle:
            output["not_yt_dlapi"]["handle"] = handle
        if username:
            output["not_yt_dlapi"]["username"] = username

        if "error" in output:
            msg = output["error"]["message"]
            if output["error"]["code"] == HTTP_NOT_FOUND:
                raise ChannelNotFoundError(msg)
            raise NotYTDLAPIError(msg)
        if output.get("pageInfo", {}).get("totalResults") == 0:
            identifier = channel_id or handle
            msg = f"Channel '{identifier}' not found."
            raise ChannelNotFoundError(msg)

        return output

    def get(
        self,
        *,
        channel_id: str | None = None,
        handle: str | None = None,
        username: str | None = None,
    ) -> ChannelModel:
        """Downloads and parses channel data by channel ID or YouTube handle.

        Args:
            channel_id: The ID of the channel to get.
            handle: The YouTube handle to get.
            username: The username of the channel to get.

        Returns:
            A ChannelModel containing the parsed data.
        """
        return self.parse(
            self.download(channel_id=channel_id, handle=handle, username=username),
        )

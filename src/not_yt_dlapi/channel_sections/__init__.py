# TODO: Validate
"""Contains the ChannelSections class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.channel_sections.models import (
    ChannelSectionsModel,
    model_validate_json,
)
from not_yt_dlapi.exceptions import ChannelNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,snippet"
"""Every part a key can ask for, which is what is always asked for."""


# TODO: Validate
class ChannelSections(BaseEndpoint):
    """The sets of videos a channel has chosen to feature, up to ten of them.

    Source: https://developers.google.com/youtube/v3/docs/channelSections

    Example request:
        - GET /youtube/v3/channelSections?
            - part={part}&
            - channelId={channel_id}&
            - key=__REDACTED__
            - HTTP/2
        - Host: www.googleapis.com
    """

    # TODO: Validate
    def __call__(self, channel_id: str) -> ChannelSectionsModel:
        """Look the channel's sections up and return the model they read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(channel_id), log_id)

    # TODO: Validate
    def download(self, channel_id: str) -> str:
        """Download the channel sections file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint="channelSections",
                params={"part": PART, "channelId": channel_id},
                headers={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ChannelNotFoundError(
                channel_id,
                err.error,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ChannelSectionsModel:
        """Read a downloaded channel sections file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

# TODO: Validate
"""Contains the Channels class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.channels.models import ChannelsModel, model_validate_json

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
"""Every part a key can ask for, which is what is always asked for.

`auditDetails` is left out because the API only hands it to a request carrying
the channel-audit scope, so asking for it would turn an ordinary request into
an error.
"""


# TODO: Validate
class Channels(BaseEndpoint):
    """A `channel` resource contains information about a YouTube channel.

    Source: https://developers.google.com/youtube/v3/docs/channels

    Example request:
        - GET /youtube/v3/channels?
            - part={part}&
            - id={channel_id}&
            - key=__REDACTED__
            - HTTP/2
        - Host: www.googleapis.com
    """

    # TODO: Validate
    @overload
    def __call__(self, *, channel_id: str) -> ChannelsModel: ...

    # TODO: Validate
    @overload
    def __call__(self, *, channel_handle: str) -> ChannelsModel: ...

    # TODO: Validate
    @overload
    def __call__(self, *, channel_username: str) -> ChannelsModel: ...

    # TODO: Validate
    def __call__(
        self,
        *,
        channel_id: str | None = None,
        channel_handle: str | None = None,
        channel_username: str | None = None,
    ) -> ChannelsModel:
        """Look the channel up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                channel_id=channel_id,
                channel_handle=channel_handle,
                channel_username=channel_username,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        *,
        channel_id: str | None = None,
        channel_handle: str | None = None,
        channel_username: str | None = None,
    ) -> str:
        """Download the channel file.

        A channel nothing is under is not an error to the API: it answers with
        no items rather than refusing.

        Raises:
            ValueError: If the channel is not named by exactly one of the three
                things it can be named by, which is all the API accepts.
        """
        log_id = self.get_log_id(self.download, locals())
        given = {
            name: value
            for name, value in (
                ("id", channel_id),
                ("for_handle", channel_handle),
                ("for_username", channel_username),
            )
            if value is not None
        }
        if len(given) != 1:
            msg = "Invalid number of arguments."
            raise ValueError(msg)

        return self._client.download(
            endpoint="channels",
            params={**given, "part": PART},
            headers={},
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ChannelsModel:
        """Read a downloaded channel file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

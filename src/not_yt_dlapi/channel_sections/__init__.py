# TODO: Validate
"""Contains the ChannelSections class.

Unlike a channel or a video, a channel id nothing is under is refused here
rather than answered with nothing, so an unknown channel raises.
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.channel_sections.models import ChannelSectionListResponse

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,snippet"
"""Every part a key can ask for, which is what is always asked for."""


# TODO: Validate
class ChannelSections(BaseEndpoint):
    """The shelves on a channel's page."""

    # TODO: Validate
    def list(
        self,
        channel_id: str,
    ) -> ChannelSectionListResponse:
        """Download a channel's sections and read them.

        Raises:
            NotFoundError: If there is no channel with that id.
        """
        log_id = self.get_log_id(self.list, locals())
        data = self._client.download(
            "channelSections",
            {"part": PART, "channelId": channel_id},
            log_id,
        )
        return ChannelSectionListResponse.from_response(data)

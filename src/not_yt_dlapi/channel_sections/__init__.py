# TODO: Validate
"""A `channelSection` resource contains information about a set of videos that
a channel has chosen to feature. For example, a section could feature a
channel's latest uploads, most popular uploads, or videos from one or more
playlists. A channel can create a maximum of 10 shelves.

https://developers.google.com/youtube/v3/docs/channelSections
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
    """A `channelSection` resource contains information about a set of videos that
    a channel has chosen to feature. For example, a section could feature a
    channel's latest uploads, most popular uploads, or videos from one or more
    playlists. A channel can create a maximum of 10 shelves.

    https://developers.google.com/youtube/v3/docs/channelSections
    """

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

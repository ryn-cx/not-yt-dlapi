# TODO: Validate
"""Contains the Topic class.

A Topic channel is generated for a musician rather than made by one, and its
page holds the albums and singles YouTube has for them. The API answers for the
channel but says nothing about its releases, so this goes to browse.

https://www.youtube.com/channel/UCooTDYkIERWBwDC1JKyoElQ
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, overload

if TYPE_CHECKING:
    import builtins

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.topic.models import TopicReleases

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Topic(BaseEndpoint):
    """The albums and singles a Topic channel lists."""

    # TODO: Validate
    @overload
    def list(self, channel_id: str) -> TopicReleases: ...

    # TODO: Validate
    @overload
    def list(self, *, continuation: str) -> TopicReleases: ...

    # TODO: Validate
    def list(
        self,
        channel_id: str | None = None,
        *,
        continuation: str | None = None,
    ) -> TopicReleases:
        """Download one stretch of a channel's releases and read it.

        The channel is opened by its id, which answers with the dozen releases
        its shelf shows, and the rest are asked for by the token that answer
        ends with. Browse takes one of the two, so this does too.

        Raises:
            ValueError: If the request is not named by exactly one of the two
                things it can be named by, which is all browse accepts.
        """
        log_id = self.get_log_id(self.list, locals())
        given: dict[str, Any] = {
            name: value
            for name, value in (
                ("browseId", channel_id),
                ("continuation", continuation),
            )
            if value is not None
        }
        if len(given) != 1:
            msg = "Invalid number of arguments."
            raise ValueError(msg)

        return TopicReleases.from_response(self._client.browse(given, log_id))

    # TODO: Validate
    def list_all(self, channel_id: str) -> builtins.list[TopicReleases]:
        """Download every release a Topic channel lists, first stretch to last.

        Opening the channel gives the shelf, whose token opens the panel holding
        every release, so the releases on the shelf are the same ones the first
        panel page lists again.
        """
        pages = [self.list(channel_id)]
        while pages[-1].continuation is not None:
            pages.append(self.list(continuation=pages[-1].continuation))
        return pages

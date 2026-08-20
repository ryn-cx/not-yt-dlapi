# TODO: Validate
"""Contains the Channels class.

Every part the API will hand out is always asked for, so what a request
answers with is decided only by the channel rather than by the caller. That is
what lets `models` say which properties a channel always carries.

A channel can be asked for by id, by the `@handle` it is reachable at or by the
username it had before handles existed, and the API takes exactly one of the
three, so the endpoint does too.

`feed` is not the API. It is the Atom feed of the channel's fifteen most recent
videos, which is served from youtube.com, takes no key and costs no quota. It
answers a much smaller question than `list` does and is only worth asking when
that question is all that was wanted.
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import overload

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.channels.models import ChannelFeedResponse, ChannelListResponse

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
    """Channels, by id, handle or legacy username."""

    # TODO: Validate
    @overload
    def list(
        self,
        *,
        channel_id: str,
    ) -> ChannelListResponse: ...

    # TODO: Validate
    @overload
    def list(
        self,
        *,
        channel_handle: str,
    ) -> ChannelListResponse: ...

    # TODO: Validate
    @overload
    def list(
        self,
        *,
        channel_username: str,
    ) -> ChannelListResponse: ...

    # TODO: Validate
    def list(
        self,
        *,
        channel_id: str | None = None,
        channel_handle: str | None = None,
        channel_username: str | None = None,
    ) -> ChannelListResponse:
        """Download a channel and read it.

        A channel nothing is under is not an error to the API: it answers with
        no items rather than refusing, so an unknown channel comes back empty.

        Raises:
            ValueError: If the channel is not named by exactly one of the three
                things it can be named by, which is all the API accepts.
        """
        log_id = self.get_log_id(self.list, locals())
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

        data = self._client.download(
            "channels",
            {**given, "part": PART},
            log_id,
        )
        return ChannelListResponse.from_response(data)

    # TODO: Validate
    def feed(self, *, channel_id: str) -> ChannelFeedResponse:
        """Download the channel's feed and read it.

        The feed is the fifteen most recent videos and nothing else: there is no
        paging and no way to ask for more, so a channel's whole upload history
        is still only `playlist_items.list` on the uploads playlist.

        Only an id names a channel here. The handle and the legacy username that
        `list` takes are the API's doing rather than the feed's, and the feed
        refuses both.

        Raises:
            HTTPError: If there is no channel with that id, which the feed
                refuses rather than answering empty, and equally if the feed
                simply will not answer. The feeds go down for a while at a time
                and a channel that answered an hour ago is refused the same way
                one that does not exist is, so a caller that means to tell the
                two apart cannot do it from the refusal alone.
        """
        log_id = self.get_log_id(self.feed, locals())
        data = self._client.download_feed({"channel_id": channel_id}, log_id)
        return ChannelFeedResponse.from_response(data)

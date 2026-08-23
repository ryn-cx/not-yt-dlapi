# TODO: Validate
"""Contains the ChannelFeed class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.channel_feed.models import ChannelFeedModel, model_validate_json
from not_yt_dlapi.exceptions import ChannelFeedNotFoundError, HTTPError
from not_yt_dlapi.feed import read_feed

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class ChannelFeed(BaseEndpoint):
    """The fifteen most recent videos a channel published.

    The feed takes no key and spends no quota, but it is the newest fifteen and
    nothing else: a channel's whole upload history is still `playlist_items` on
    the uploads playlist. Only an id names a channel here; the handle and the
    legacy username that `channels` takes are both refused.

    Source: https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}

    Example request:
        - GET /feeds/videos.xml?
            - channel_id={channel_id}
            - HTTP/2
        - Host: www.youtube.com
    """

    # TODO: Validate
    def __call__(self, channel_id: str) -> ChannelFeedModel:
        """Look the channel's feed up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(channel_id), log_id)

    # TODO: Validate
    def download(self, channel_id: str) -> str:
        """Download the channel feed file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download_feed(
                params={"channel_id": channel_id},
                headers={},
                log_id=log_id,
            )
        except HTTPError as err:
            raise ChannelFeedNotFoundError(
                channel_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ChannelFeedModel:
        """Read a downloaded channel feed file into its model."""
        return model_validate_json(read_feed(data), log_id or type(self).__name__)

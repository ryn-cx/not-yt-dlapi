# TODO: Validate
"""Contains the PlaylistFeed class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.exceptions import HTTPError, PlaylistFeedNotFoundError
from not_yt_dlapi.feed import extract_feed
from not_yt_dlapi.playlist_feed.models import (
    PlaylistFeedModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class PlaylistFeed(BaseEndpoint):
    """The fifteen most recent videos a playlist holds.

    YouTube is currently refusing every playlist feed it is asked for, so at the
    moment the download always raises.

    Source: https://www.youtube.com/feeds/videos.xml?playlist_id={playlist_id}

    Example request:
        - GET /feeds/videos.xml?
            - playlist_id={playlist_id}
            - HTTP/2
        - Host: www.youtube.com
    """

    # TODO: Validate
    def __call__(self, playlist_id: str) -> PlaylistFeedModel:
        """Download and parse the playlist's feed file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(playlist_id), log_id)

    # TODO: Validate
    def download(self, playlist_id: str) -> str:
        """Download the playlist feed file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download_feed(
                params={"playlist_id": playlist_id},
                headers={},
                log_id=log_id,
            )
        except HTTPError as err:
            raise PlaylistFeedNotFoundError(
                playlist_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> PlaylistFeedModel:
        """Load a playlist feed file into its model."""
        return model_validate_json(extract_feed(data), log_id or self.default_log_id)

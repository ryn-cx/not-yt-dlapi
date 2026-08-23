# TODO: Validate
"""Contains the Topic class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.topic.models import TopicModel, model_validate_json
from not_yt_dlapi.utils import find, read_continuation

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Topic(BaseEndpoint):
    """The albums and singles a Topic channel lists.

    A Topic channel is generated for a musician rather than made by one. The
    API answers for the channel but says nothing about its releases, so this
    asks browse. One download is one stretch of the listing; `download_all`
    follows it to the end.

    Source: https://www.youtube.com/channel/{channel_id}

    Example request:
        - POST /youtubei/v1/browse HTTP/2
        - Host: www.youtube.com
        - Content-Type: application/json
        - Body: {"browseId": "{channel_id}", "context": {"client": ...}}
    """

    # TODO: Validate
    @overload
    def __call__(self, channel_id: str) -> TopicModel: ...

    # TODO: Validate
    @overload
    def __call__(self, *, continuation: str) -> TopicModel: ...

    # TODO: Validate
    def __call__(
        self,
        channel_id: str | None = None,
        *,
        continuation: str | None = None,
    ) -> TopicModel:
        """Look one stretch of the releases up and return the model it reads into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(channel_id, continuation=continuation),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        channel_id: str | None = None,
        *,
        continuation: str | None = None,
    ) -> str:
        """Download one stretch of a channel's releases.

        The channel is opened by its id, which answers with the dozen releases
        its shelf shows, and the rest are asked for by the token that answer
        ends with.

        Raises:
            ValueError: If the request is not named by exactly one of the two
                things it can be named by, which is all browse accepts.
        """
        log_id = self.get_log_id(self.download, locals())
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

        return self._client.browse(given, log_id)

    # TODO: Validate
    def download_all(self, channel_id: str) -> list[str]:
        """Download every release a Topic channel lists, first stretch to last.

        Opening the channel gives the shelf, whose token opens the panel holding
        every release, so the releases on the shelf are the same ones the first
        panel page lists again.
        """
        pages = [self.download(channel_id)]
        continuation = self.extract_continuation(self.load(pages[0]))
        while continuation is not None:
            page = self.download(continuation=continuation)
            pages.append(page)
            continuation = self.extract_continuation(self.load(page))
        return pages

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TopicModel:
        """Read a downloaded releases file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[TopicModel]:
        """Read the stretches `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    # TODO: Validate
    @staticmethod
    def extract_channel_id(data: TopicModel) -> str | None:
        """Extract the id of the channel the releases are of.

        Only the answer to opening the channel says it; a panel page does not.
        """
        metadata = data.raw_input.get("metadata", {})
        return next(find(metadata, "externalId"), None)

    # TODO: Validate
    @staticmethod
    def extract_release_ids(data: TopicModel) -> list[str]:
        """Extract the playlist id of every release the stretch listed.

        The shelf writes a release as a lockup and the panel behind it writes
        one as a grid entry, so both are read.
        """
        grid = [
            entry["gridPlaylistRenderer"]["playlistId"]
            for entries in find(data.raw_input, "items")
            for entry in entries
            if "gridPlaylistRenderer" in entry
        ]
        if grid:
            return grid
        shelf = next(find(data.raw_input, "shelfRenderer"), {})
        return [
            lockup["contentId"]
            for lockup in find(shelf, "lockupViewModel")
            if "contentId" in lockup
        ]

    # TODO: Validate
    @staticmethod
    def extract_continuation(data: TopicModel) -> str | None:
        """Extract what the stretch after this one is asked for by.

        The shelf's own token is what opens the panel holding every release, and
        a panel page ends with the token for the next.
        """
        shelf = next(find(data.raw_input, "shelfRenderer"), None)
        if shelf is not None:
            return next(find(shelf["endpoint"], "token"), None)
        return read_continuation(data.raw_input)

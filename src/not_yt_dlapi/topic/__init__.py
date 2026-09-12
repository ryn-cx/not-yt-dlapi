# TODO: Validate
"""Contains the Topic class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, overload

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.topic.models import (
    GridPlaylistRenderer,
    Item,
    Item1,
    ShelfRenderer,
    TopicModel,
    model_validate_json,
)

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
        """Load a releases file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

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
        if data.metadata is None:
            return None
        return data.metadata.channel_metadata_renderer.external_id

    # TODO: Validate
    @classmethod
    def extract_release_ids(cls, data: TopicModel) -> list[str]:
        """Extract the playlist id of every release the stretch listed.

        The shelf writes a release as a lockup and the panel behind it writes
        one as a grid entry, so both are read.
        """
        grid = [
            entry.playlist_id for entry in cls._grid_releases(data) if entry is not None
        ]
        if grid:
            return grid
        return [item.lockup_view_model.content_id for item in cls._shelf_items(data)]

    # TODO: Validate
    @classmethod
    def extract_continuation(cls, data: TopicModel) -> str | None:
        """Extract what the stretch after this one is asked for by.

        The shelf's own token is what opens the panel holding every release, and
        a panel page ends with the token for the next.
        """
        for shelf in cls._shelves(data):
            panel = shelf.endpoint.show_engagement_panel_endpoint.engagement_panel
            return next(
                (
                    content.continuation_item_renderer.continuation_endpoint.continuation_command.token
                    for section in (
                        panel.engagement_panel_section_list_renderer.content.section_list_renderer.contents
                    )
                    for content in section.item_section_renderer.contents
                ),
                None,
            )

        return next(
            (
                grid_item.continuation_item_renderer.continuation_endpoint.continuation_command.token
                for grid_item in cls._grid_items(data)
                if grid_item.continuation_item_renderer is not None
            ),
            None,
        )

    # TODO: Validate
    @staticmethod
    def _shelves(data: TopicModel) -> list[ShelfRenderer]:
        if data.contents is None:
            return []
        return [
            item.shelf_renderer
            for tab in data.contents.two_column_browse_results_renderer.tabs
            for section in tab.tab_renderer.content.section_list_renderer.contents
            for item in section.item_section_renderer.contents
        ]

    # TODO: Validate
    @classmethod
    def _shelf_items(cls, data: TopicModel) -> list[Item]:
        return [
            shelf_item
            for shelf in cls._shelves(data)
            for shelf_item in shelf.content.horizontal_list_renderer.items
        ]

    # TODO: Validate
    @staticmethod
    def _grid_items(data: TopicModel) -> list[Item1]:
        if data.on_response_received_endpoints is None:
            return []
        return [
            grid_item
            for endpoint in data.on_response_received_endpoints
            for continuation_item in (
                endpoint.append_continuation_items_action.continuation_items
            )
            if continuation_item.grid_renderer is not None
            for grid_item in continuation_item.grid_renderer.items
        ]

    # TODO: Validate
    @classmethod
    def _grid_releases(cls, data: TopicModel) -> list[GridPlaylistRenderer | None]:
        return [grid_item.grid_playlist_renderer for grid_item in cls._grid_items(data)]

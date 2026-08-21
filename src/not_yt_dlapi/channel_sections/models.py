# TODO: Validate
"""Channel sections models.

Shaped after the channelSection resource as the API documents it: one class per
documented object, one field per documented property, and the API's own wording
for what each property is.

Every part is always asked for, so a property is optional here only when the
resource itself decides whether to carry it, never because the request might not
have asked.
"""

from __future__ import annotations

import json
from typing import Self, override

from pydantic import Field

from not_yt_dlapi.base_response_model import BaseResponseModel
from not_yt_dlapi.common_models import APIModel


# TODO: Validate
class ChannelSectionSnippet(APIModel):
    """The `snippet` object contains basic details about the channel section, such as its type and title.

    Attributes:
        type: The channel section's type. Valid values include: `allPlaylists`,
            `completedEvents`, `liveEvents`, `multipleChannels`,
            `multiplePlaylists`, `popularUploads`, `recentUploads`,
            `singlePlaylist`, `subscriptions`, `upcomingEvents`.
        channel_id: The ID that YouTube uses to uniquely identify the channel
            that published the channel section.
        title: The section's title. Settable only for `multiplePlaylists` or
            `multipleChannels` types. Maximum length: 100 characters; may
            contain all valid UTF-8 characters except `<` and `>`.
        position: The section's position on the channel page using 0-based
            indexing. If unspecified during insertion, displays the new section
            last.
    """  # noqa: E501

    type: str
    channel_id: str
    # Only the two types that are titled by hand carry a title.
    title: str | None = None
    position: int


# TODO: Validate
class ChannelSectionContentDetails(APIModel):
    """Contains details about the channel section's content, such as featured playlists or channels.

    Attributes:
        playlists: Playlist IDs featured in the section; required for
            `singlePlaylist` or `multiplePlaylists` types.
        channels: Channel IDs featured in the section; required for
            `multipleChannels` type; cannot include your own channel.
    """  # noqa: E501

    playlists: list[str] | None = None
    channels: list[str] | None = None


# TODO: Validate
class ChannelSection(APIModel):
    """One shelf on a channel's page.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#channelSection`.
        etag: The Etag of this resource.
        id: The ID that YouTube uses to uniquely identify the channel section.
        snippet: The `snippet` object contains basic details about the channel
            section, such as its type and title.
        content_details: Contains details about the channel section's content,
            such as featured playlists or channels.
    """

    kind: str
    etag: str
    id: str
    snippet: ChannelSectionSnippet
    # A shelf whose contents YouTube picks, such as `recentUploads`, has nothing
    # of its own to list and so carries no `contentDetails` at all.
    content_details: ChannelSectionContentDetails | None = None


# TODO: Validate
class ChannelSectionListResponse(BaseResponseModel, APIModel):
    """Every shelf on one channel's page.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#channelSectionListResponse`.
        etag: The Etag of this resource.
        items: A list of ChannelSections that match the request criteria.
        raw: The response as it was served, which is the document
            itself rather than the reading of it.
    """

    kind: str
    etag: str
    # A channel that has arranged no shelves has no `items` at all.
    items: list[ChannelSection] = Field(default_factory=list)
    raw: str = Field(repr=False, exclude=True)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: str) -> Self:
        return cls.model_validate({**json.loads(data), "raw": data})

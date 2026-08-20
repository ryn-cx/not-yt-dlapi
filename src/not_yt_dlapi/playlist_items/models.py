# TODO: Validate
"""Playlist items models.

Shaped after the playlistItem resource as the API documents it: one class per
documented object, one field per documented property, and the API's own wording
for what each property is.

Every part is always asked for, so a property is optional here only when the
resource itself decides whether to carry it, never because the request might not
have asked.
"""

from __future__ import annotations

from typing import Any, Self, override

from pydantic import Field, SkipValidation

from not_yt_dlapi.base_response_model import BaseResponseModel
from not_yt_dlapi.common_models import APIModel, PageInfo, Thumbnails


# TODO: Validate
class ResourceId(APIModel):
    """The `id` object contains information that can be used to uniquely identify the resource that is included in the playlist.

    Attributes:
        kind: The kind, or type, of the referred resource.
        video_id: If the `snippet.resourceId.kind` property's value is
            `youtube#video`, then this property will be present and its value
            will contain the ID that YouTube uses to uniquely identify the video
            in the playlist.
    """  # noqa: E501

    kind: str
    video_id: str | None = None


# TODO: Validate
class PlaylistItemSnippet(APIModel):
    """The `snippet` object contains basic details about the playlist item, such as its title and position in the playlist.

    Attributes:
        published_at: The date and time that the item was added to the playlist.
        channel_id: The ID that YouTube uses to uniquely identify the user that
            added the item to the playlist.
        title: The item's title.
        description: The item's description.
        thumbnails: The thumbnail images associated with the playlist item.
        channel_title: The channel title of the channel that the playlist item
            belongs to.
        video_owner_channel_title: The channel title of the channel that
            uploaded this video.
        video_owner_channel_id: The channel ID of the channel that uploaded this
            video.
        playlist_id: The ID that YouTube uses to uniquely identify the playlist
            that the playlist item is in.
        position: The order in which the item appears in the playlist.
        resource_id: The `id` object contains information that can be used to
            uniquely identify the resource that is included in the playlist.
    """  # noqa: E501

    published_at: str
    channel_id: str
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str
    # A video that has been deleted or made private stops saying who uploaded it.
    video_owner_channel_title: str | None = None
    video_owner_channel_id: str | None = None
    playlist_id: str
    position: int
    resource_id: ResourceId


# TODO: Validate
class PlaylistItemContentDetails(APIModel):
    """The `contentDetails` object is included in the resource if the included item is a YouTube video.

    Attributes:
        video_id: The ID that YouTube uses to uniquely identify a video.
        start_at: **Note:** This property has been deprecated and, if set, its
            value is ignored.
        end_at: **Note:** This property has been deprecated and, if set, its
            value is ignored.
        note: A user-generated note for this item. The property value has a
            maximum length of 280 characters.
        video_published_at: The date and time that the video was published to
            YouTube.
    """  # noqa: E501

    video_id: str
    start_at: str | None = None
    end_at: str | None = None
    note: str | None = None
    # A video that is no longer watchable keeps its place in the playlist but
    # stops saying when it went up.
    video_published_at: str | None = None


# TODO: Validate
class PlaylistItemStatus(APIModel):
    """The `status` object contains information about the playlist item's privacy status.

    Attributes:
        privacy_status: The playlist item's privacy status.
    """  # noqa: E501

    privacy_status: str


# TODO: Validate
class PlaylistItem(APIModel):
    """One video's place in a playlist.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#playlistItem`.
        etag: The Etag of this resource.
        id: The ID that YouTube uses to uniquely identify the playlist item.
        snippet: The `snippet` object contains basic details about the playlist
            item, such as its title and position in the playlist.
        content_details: The `contentDetails` object is included in the resource
            if the included item is a YouTube video.
        status: The `status` object contains information about the playlist
            item's privacy status.
    """

    kind: str
    etag: str
    id: str
    snippet: PlaylistItemSnippet
    content_details: PlaylistItemContentDetails
    status: PlaylistItemStatus


# TODO: Validate
class PlaylistItemListResponse(BaseResponseModel, APIModel):
    """One page of a playlist's items.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#playlistItemListResponse`.
        etag: The Etag of this resource.
        next_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the next page in the result set.
        prev_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the previous page in the result
            set.
        page_info: The `pageInfo` object encapsulates paging information for the
            result set.
        items: A list of playlist items that match the request criteria.
        raw: The response as it was downloaded.
    """

    kind: str
    etag: str
    next_page_token: str | None = None
    prev_page_token: str | None = None
    page_info: PageInfo
    # An empty playlist has no `items` at all.
    items: tuple[PlaylistItem, ...] = ()
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})

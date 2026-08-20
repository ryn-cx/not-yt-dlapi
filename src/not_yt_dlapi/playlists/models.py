# TODO: Validate
"""Playlists models.

Shaped after the playlist resource as the API documents it: one class per
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
from not_yt_dlapi.common_models import (
    APIModel,
    Localization,
    Localizations,
    PageInfo,
    Thumbnails,
)
from not_yt_dlapi.feed_models import FeedResponse


# TODO: Validate
class PlaylistSnippet(APIModel):
    """The `snippet` object contains basic details about the playlist, such as its title and description.

    Attributes:
        published_at: The date and time that the playlist was created. The value
            is specified in ISO 8601 format.
        channel_id: The ID that YouTube uses to uniquely identify the channel
            that published the playlist.
        title: The playlist's title.
        description: The playlist's description.
        thumbnails: The thumbnail images associated with the playlist.
        channel_title: The channel title of the channel that the video belongs
            to.
        default_language: The language of the text in the `playlist` resource's
            `snippet.title` and `snippet.description` properties.
        localized: The `snippet.localized` object contains either a localized
            title and description for the playlist or the title in the default
            language for the playlist's metadata.
    """  # noqa: E501

    published_at: str
    channel_id: str
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str
    # Only a playlist whose owner said what language they wrote it in has one.
    default_language: str | None = None
    localized: Localization


# TODO: Validate
class PlaylistStatus(APIModel):
    """The `status` object contains status information for the playlist.

    Attributes:
        privacy_status: The playlist's privacy status.
        podcast_status: The playlist's podcast status. If value is `enabled`,
            the playlist is marked as a podcast show. To set a playlist's
            podcast status to `enabled`, the playlist must have a playlist
            image.
    """

    privacy_status: str
    podcast_status: str | None = None


# TODO: Validate
class PlaylistContentDetails(APIModel):
    """The `contentDetails` object contains information about the playlist content.

    Attributes:
        item_count: The number of videos in the playlist.
    """

    item_count: int


# TODO: Validate
class PlaylistPlayer(APIModel):
    """The `player` object contains information for embedded playlist playback.

    Attributes:
        embed_html: An `<iframe>` tag that embeds a player that will play the
            playlist.
    """

    embed_html: str


# TODO: Validate
class Playlist(APIModel):
    """One playlist.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#playlist`.
        etag: The Etag of this resource.
        id: The ID that YouTube uses to uniquely identify the playlist.
        snippet: The `snippet` object contains basic details about the playlist,
            such as its title and description.
        status: The `status` object contains status information for the
            playlist.
        content_details: The `contentDetails` object contains information about
            the playlist content.
        player: The `player` object contains information for embedded playlist
            playback.
        localizations: The `localizations` object encapsulates translations of
            the playlist's metadata.
    """

    kind: str
    etag: str
    id: str
    snippet: PlaylistSnippet
    status: PlaylistStatus
    content_details: PlaylistContentDetails
    player: PlaylistPlayer
    # Only a playlist that has been translated carries translations.
    localizations: Localizations | None = None


# TODO: Validate
class PlaylistListResponse(BaseResponseModel, APIModel):
    """One page of playlists.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#playlistListResponse`.
        etag: The Etag of this resource.
        next_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the next page in the result set.
        prev_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the previous page in the result
            set.
        page_info: The `pageInfo` object encapsulates paging information for the
            result set.
        items: A list of playlists that match the request criteria.
        raw: The response as it was downloaded.
    """

    kind: str
    etag: str
    next_page_token: str | None = None
    prev_page_token: str | None = None
    page_info: PageInfo
    # A page that found nothing has no `items` at all.
    items: tuple[Playlist, ...] = ()
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})


# TODO: Validate
class PlaylistFeedResponse(FeedResponse):
    """The fifteen most recent videos a playlist holds.

    Everything a feed carries is the same whatever the feed is of, so all of it
    is described on `FeedResponse`. What a playlist feed adds is saying which
    playlist it is of.

    Nothing here has been checked against a downloaded feed, because YouTube is
    currently refusing every playlist feed it is asked for. It is written from
    the channel feed on the understanding that the two documents are the same
    but for this field, which is what the two were before playlist feeds
    stopped answering.

    Attributes:
        playlist_id: Which playlist the feed is of. A channel feed writes its
            channel id with the leading `UC` taken off, so whether a playlist
            feed writes its id in full is one of the things that cannot be known
            until playlist feeds answer again.
    """

    playlist_id: str

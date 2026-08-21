# TODO: Validate
"""Channels models.

Shaped after the channel resource as the API documents it: one class per
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
from not_yt_dlapi.common_models import (
    APIModel,
    Localization,
    Localizations,
    PageInfo,
    Thumbnails,
)
from not_yt_dlapi.feed_models import FeedResponse


# TODO: Validate
class ChannelSnippet(APIModel):
    """The `snippet` object contains basic details about the channel, such as its title, description, and thumbnail images.

    Attributes:
        title: The channel's title.
        description: The channel's description. The property's value has a
            maximum length of 1000 characters.
        custom_url: The channel's custom URL. The YouTube Help Center explains
            eligibility requirements for getting a custom URL as well as how to
            set up the URL.
        published_at: The date and time that the channel was created. The value
            is specified in ISO 8601 format.
        thumbnails: The thumbnail images associated with the channel.
        default_language: The language of the text in the `channel` resource's
            `snippet.title` and `snippet.description` properties.
        localized: The `snippet.localized` object contains a localized title and
            description for the channel or it contains the channel's title and
            description in the default language for the channel's metadata.
        country: The country with which the channel is associated. To set this
            property's value, update the value of the
            `brandingSettings.channel.country` property.
    """  # noqa: E501

    title: str
    description: str
    # Only a channel that has claimed a handle has one.
    custom_url: str | None = None
    published_at: str
    thumbnails: Thumbnails
    default_language: str | None = None
    localized: Localization
    country: str | None = None


# TODO: Validate
class RelatedPlaylists(APIModel):
    """The `relatedPlaylists` object is a map that identifies playlists associated with the channel, such as the channel's uploaded videos or liked videos.

    Attributes:
        likes: The ID of the playlist that contains the channel's liked videos.
            Use the `playlistItems.insert` and `playlistItems.delete` methods to
            add or remove items from that list.
        favorites: This property has been deprecated. The ID of the playlist
            that contains the channel's favorite videos.
        uploads: The ID of the playlist that contains the channel's uploaded
            videos. Use the `videos.insert` method to upload new videos and the
            `videos.delete` method to delete previously uploaded videos.
    """  # noqa: E501

    likes: str
    # Favourites were taken away, so no channel names that playlist any more.
    favorites: str | None = None
    uploads: str


# TODO: Validate
class ChannelContentDetails(APIModel):
    """The `contentDetails` object encapsulates information about the channel's content.

    Attributes:
        related_playlists: The `relatedPlaylists` object is a map that
            identifies playlists associated with the channel, such as the
            channel's uploaded videos or liked videos.
    """

    related_playlists: RelatedPlaylists


# TODO: Validate
class ChannelStatistics(APIModel):
    """The `statistics` object encapsulates statistics for the channel.

    Attributes:
        view_count: The sum of the number of times all the videos in all formats
            have been viewed for a channel.
        subscriber_count: The number of subscribers that the channel has. This
            value is rounded down to three significant figures.
        hidden_subscriber_count: Indicates whether the channel's subscriber
            count is publicly visible.
        video_count: The number of public videos uploaded to the channel. Note
            that the value reflects the count of the channel's public videos
            only, even to owners.
    """

    view_count: int
    subscriber_count: int
    hidden_subscriber_count: bool
    video_count: int


# TODO: Validate
class ChannelTopicDetails(APIModel):
    """The `topicDetails` object encapsulates information about topics associated with the channel.

    Attributes:
        topic_ids: A list of topic IDs associated with the channel. This
            property has been deprecated as of November 10, 2016.
        topic_categories: A list of Wikipedia URLs that describe the channel's
            content.
    """  # noqa: E501

    topic_ids: list[str] | None = None
    topic_categories: list[str] | None = None


# TODO: Validate
class ChannelStatus(APIModel):
    """The `status` object encapsulates information about the privacy status of the channel.

    Attributes:
        privacy_status: Privacy status of the channel. Valid values for this
            property are: `private`, `public`, `unlisted`
        is_linked: Indicates whether the channel data identifies a user that is
            already linked to either a YouTube username or a Google+ account.
        long_uploads_status: Indicates whether the channel is eligible to upload
            videos that are more than 15 minutes long. This property is only
            returned if the channel owner authorized the API request.
        made_for_kids: This value indicates whether the channel is designated as
            child-directed, and it contains the current 'made for kids' status
            of the channel.
        self_declared_made_for_kids: In a `channels.update` request, this
            property allows the channel owner to designate the channel as
            child-directed. The property value is only returned if the channel
            owner authorized the API request.
    """  # noqa: E501

    privacy_status: str
    is_linked: bool
    long_uploads_status: str | None = None
    made_for_kids: bool | None = None
    self_declared_made_for_kids: bool | None = None


# TODO: Validate
class ChannelBrandingSettings(APIModel):
    """The `channel` object encapsulates branding properties of the channel page.

    Attributes:
        title: The channel's title. The title has a maximum length of 30
            characters.
        description: The channel description, which appears in the channel
            information box on your channel page. The property's value has a
            maximum length of 1000 characters.
        keywords: Keywords associated with your channel. The value is a
            space-separated list of strings. Channel keywords might be truncated
            if they exceed the maximum allowed length of 500 characters or if
            they contained unescaped quotation marks. Note that the 500
            character limit is not a per-keyword limit but rather a limit on the
            total length of all keywords.
        tracking_analytics_account_id: The ID for a Google Analytics account
            that you want to use to track and measure traffic to your channel.
        unsubscribed_trailer: The video that should play in the featured video
            module in the channel page's browse view for unsubscribed viewers.
            Subscribed viewers may see a different video that highlights more
            recent channel activity. If specified, the property's value must be
            the YouTube video ID of a public or unlisted video that is owned by
            the channel owner.
        default_language: The language of the text in the `channel` resource's
            `snippet.title` and `snippet.description` properties.
        country: The country with which the channel is associated. Update this
            property to set the value of the `snippet.country` property.
    """

    title: str
    description: str | None = None
    keywords: str | None = None
    tracking_analytics_account_id: str | None = None
    unsubscribed_trailer: str | None = None
    default_language: str | None = None
    country: str | None = None


# TODO: Validate
class WatchBrandingSettings(APIModel):
    """The `watch` object encapsulates branding properties of the watch pages for the channel's videos.

    **Note:** This object and all of its child properties have been deprecated.

    Attributes:
        text_color: **Note:** This property has been deprecated. The text color
            for the video watch page's branded area.
        background_color: **Note:** This property has been deprecated. The
            background color for the video watch page's branded area.
        featured_playlist_id: **Note:** This property has been deprecated. The
            API returns an error if you attempt to set its value.
    """  # noqa: E501

    text_color: str | None = None
    background_color: str | None = None
    featured_playlist_id: str | None = None


# TODO: Validate
class ImageBrandingSettings(APIModel):
    """The `image` object encapsulates information about images that display on the channel's channel page or video watch pages.

    This property and all of its child properties have been deprecated. Of
    everything the docs still list under it, `banner_external_url` is the only
    one the API answers with, so it is the only one given a field.

    Attributes:
        banner_external_url: This property specifies the location of the banner
            image that YouTube uses to generate the various banner image sizes
            for a channel.
    """  # noqa: E501

    banner_external_url: str | None = None


# TODO: Validate
class BrandingHint(APIModel):
    """The `hints` object encapsulates additional branding properties.

    This property and all of its child properties have been deprecated.

    Attributes:
        property: This property has been deprecated. A property.
        value: This property has been deprecated. The property's value.
    """

    property: str | None = None
    value: str | None = None


# TODO: Validate
class BrandingSettings(APIModel):
    """The `brandingSettings` object encapsulates information about the branding of the channel.

    Attributes:
        channel: The `channel` object encapsulates branding properties of the
            channel page.
        watch: **Note:** This object and all of its child properties have been
            deprecated. The `watch` object encapsulates branding properties of
            the watch pages for the channel's videos.
        image: This property and all of its child properties have been
            deprecated. The `image` object encapsulates information about images
            that display on the channel's channel page or video watch pages.
        hints: This property and all of its child properties have been
            deprecated. The `hints` object encapsulates additional branding
            properties.
    """  # noqa: E501

    channel: ChannelBrandingSettings
    watch: WatchBrandingSettings | None = None
    image: ImageBrandingSettings | None = None
    hints: list[BrandingHint] | None = None


# TODO: Validate
class AuditDetails(APIModel):
    """The `auditDetails` object encapsulates channel data that a multichannel network (MCN) would evaluate while determining whether to accept or reject a particular channel.

    Any API request that retrieves this resource part must provide an
    authorization token that carries the channel-audit scope, which is why the
    part is never asked for and this object never arrives.

    Attributes:
        overall_good_standing: This field indicates whether there are any issues
            with the channel. Currently, this field represents the result of the
            logical `AND` operation over the `communityGuidelinesGoodStanding`,
            `copyrightStrikesGoodStanding`, and `contentIdClaimsGoodStanding`
            properties, meaning that this property has a value of `true` if all
            of those other properties also have a value of `true`. However, this
            property will have a value of `false` if any of those properties has
            a value of `false`.
        community_guidelines_good_standing: Indicates whether the channel
            respects YouTube's community guidelines.
        copyright_strikes_good_standing: Indicates whether the channel has any
            copyright strikes.
        content_id_claims_good_standing: Indicates whether the channel has any
            unresolved claims.
    """  # noqa: E501

    overall_good_standing: bool | None = None
    community_guidelines_good_standing: bool | None = None
    copyright_strikes_good_standing: bool | None = None
    content_id_claims_good_standing: bool | None = None


# TODO: Validate
class ContentOwnerDetails(APIModel):
    """The `contentOwnerDetails` object encapsulates channel data that is visible only to the YouTube Partner that has linked the channel to their Content Manager.

    The object itself always arrives; a channel no partner has linked answers
    with it empty.

    Attributes:
        content_owner: The ID of the content owner linked to the channel.
        time_linked: The date and time of when the channel was linked to the
            content owner. The value is specified in ISO 8601 format.
    """  # noqa: E501

    content_owner: str | None = None
    time_linked: str | None = None


# TODO: Validate
class Channel(APIModel):
    """One channel.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#channel`.
        etag: The Etag of this resource.
        id: The ID that YouTube uses to uniquely identify the channel.
        snippet: The `snippet` object contains basic details about the channel,
            such as its title, description, and thumbnail images.
        content_details: The `contentDetails` object encapsulates information
            about the channel's content.
        statistics: The `statistics` object encapsulates statistics for the
            channel.
        topic_details: The `topicDetails` object encapsulates information about
            topics associated with the channel.
        status: The `status` object encapsulates information about the privacy
            status of the channel.
        branding_settings: The `brandingSettings` object encapsulates
            information about the branding of the channel.
        audit_details: The `auditDetails` object encapsulates channel data that
            a multichannel network (MCN) would evaluate while determining
            whether to accept or reject a particular channel.
        content_owner_details: The `contentOwnerDetails` object encapsulates
            channel data that is visible only to the YouTube Partner that has
            linked the channel to their Content Manager.
        localizations: The `localizations` object encapsulates translations of
            the channel's metadata.
    """

    kind: str
    etag: str
    id: str
    snippet: ChannelSnippet
    content_details: ChannelContentDetails
    statistics: ChannelStatistics
    # A channel YouTube has worked out no topics for carries none.
    topic_details: ChannelTopicDetails | None = None
    status: ChannelStatus
    branding_settings: BrandingSettings
    # The channel-audit scope is never asked for, so this never arrives.
    audit_details: AuditDetails | None = None
    content_owner_details: ContentOwnerDetails
    # Only a channel that has been translated carries translations.
    localizations: Localizations | None = None


# TODO: Validate
class ChannelListResponse(BaseResponseModel, APIModel):
    """Every channel one request asked about.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#channelListResponse`.
        etag: The Etag of this resource.
        next_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the next page in the result set.
        prev_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the previous page in the result
            set.
        page_info: The `pageInfo` object encapsulates paging information for the
            result set.
        items: A list of channels that match the request criteria.
        raw: The response as it was served, which is the document
            itself rather than the reading of it.
    """

    kind: str
    etag: str
    next_page_token: str | None = None
    prev_page_token: str | None = None
    page_info: PageInfo
    # A response that found nothing has no `items` at all.
    items: list[Channel] = Field(default_factory=list)
    raw: str = Field(repr=False, exclude=True)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: str) -> Self:
        return cls.model_validate({**json.loads(data), "raw": data})


# TODO: Validate
class ChannelFeedResponse(FeedResponse):
    """The fifteen most recent videos a channel published.

    Everything a feed carries is the same whatever the feed is of, so all of it
    is described on `FeedResponse`. What a channel feed adds is saying which
    channel it is of.

    Attributes:
        channel_id: Which channel the feed is of, with the leading `UC` of the
            channel's id taken off, the same way `id` writes it. It is not an id
            anything else accepts, so a caller that wants one has to put the
            `UC` back or read it off an entry, which writes the id in full.
    """

    channel_id: str

# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from typing import Any

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_results: int = Field(..., alias="totalResults")
    results_per_page: int = Field(..., alias="resultsPerPage")


class Default(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Medium(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class High(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Thumbnails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    default: Default
    medium: Medium
    high: High


class Localized(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Snippet(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str
    custom_url: str = Field(..., alias="customUrl")
    published_at: AwareDatetime = Field(..., alias="publishedAt")
    thumbnails: Thumbnails
    localized: Localized
    country: str | None = None


class RelatedPlaylists(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    likes: str
    uploads: str


class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    related_playlists: RelatedPlaylists = Field(..., alias="relatedPlaylists")


class Statistics(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    view_count: str = Field(..., alias="viewCount")
    subscriber_count: str = Field(..., alias="subscriberCount")
    hidden_subscriber_count: bool = Field(..., alias="hiddenSubscriberCount")
    video_count: str = Field(..., alias="videoCount")


class TopicDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    topic_ids: list[str] = Field(..., alias="topicIds")
    topic_categories: list[str] = Field(..., alias="topicCategories")


class Status(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    privacy_status: str = Field(..., alias="privacyStatus")
    is_linked: bool = Field(..., alias="isLinked")
    long_uploads_status: str = Field(..., alias="longUploadsStatus")
    made_for_kids: bool | None = Field(None, alias="madeForKids")


class Channel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    keywords: str | None = None
    unsubscribed_trailer: str | None = Field(None, alias="unsubscribedTrailer")
    country: str | None = None
    description: str | None = None
    tracking_analytics_account_id: str | None = Field(
        None,
        alias="trackingAnalyticsAccountId",
    )


class Image(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    banner_external_url: str = Field(..., alias="bannerExternalUrl")


class BrandingSettings(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    channel: Channel
    image: Image | None = None


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias="contentDetails")
    statistics: Statistics
    topic_details: TopicDetails | None = Field(None, alias="topicDetails")
    status: Status
    branding_settings: BrandingSettings = Field(..., alias="brandingSettings")
    content_owner_details: dict[str, Any] = Field(..., alias="contentOwnerDetails")


class ChannelsModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias="pageInfo")
    items: list[Item]

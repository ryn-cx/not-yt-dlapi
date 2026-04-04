# ruff: noqa: COM812, D100, D101
from __future__ import annotations

from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class PageInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total_results: int = Field(..., alias="totalResults")
    results_per_page: int = Field(..., alias="resultsPerPage")


class Default(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Medium(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class High(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Thumbnails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    default: Default
    medium: Medium
    high: High


class Localized(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Snippet(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str
    custom_url: str = Field(..., alias="customUrl")
    published_at: AwareDatetime = Field(..., alias="publishedAt")
    thumbnails: Thumbnails
    localized: Localized
    country: str | None = None


class RelatedPlaylists(BaseModel):
    model_config = ConfigDict(extra="forbid")
    likes: str
    uploads: str


class ContentDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    related_playlists: RelatedPlaylists = Field(..., alias="relatedPlaylists")


class Statistics(BaseModel):
    model_config = ConfigDict(extra="forbid")
    view_count: str = Field(..., alias="viewCount")
    subscriber_count: str = Field(..., alias="subscriberCount")
    hidden_subscriber_count: bool = Field(..., alias="hiddenSubscriberCount")
    video_count: str = Field(..., alias="videoCount")


class TopicDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    topic_ids: list[str] = Field(..., alias="topicIds")
    topic_categories: list[str] = Field(..., alias="topicCategories")


class Status(BaseModel):
    model_config = ConfigDict(extra="forbid")
    privacy_status: str = Field(..., alias="privacyStatus")
    is_linked: bool = Field(..., alias="isLinked")
    long_uploads_status: str = Field(..., alias="longUploadsStatus")
    made_for_kids: bool = Field(..., alias="madeForKids")


class Channel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str | None = None
    keywords: str
    tracking_analytics_account_id: str | None = Field(
        None, alias="trackingAnalyticsAccountId"
    )
    unsubscribed_trailer: str = Field(..., alias="unsubscribedTrailer")
    country: str | None = None


class Image(BaseModel):
    model_config = ConfigDict(extra="forbid")
    banner_external_url: str = Field(..., alias="bannerExternalUrl")


class BrandingSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")
    channel: Channel
    image: Image


class Item(BaseModel):
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


class NotYtDlapi(BaseModel):
    model_config = ConfigDict(extra="forbid")
    channel_id: str
    part: str
    timestamp: AwareDatetime


class ChannelModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias="pageInfo")
    items: list[Item]
    not_yt_dlapi: NotYtDlapi

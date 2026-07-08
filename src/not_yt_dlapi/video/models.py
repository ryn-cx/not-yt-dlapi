# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from datetime import timedelta

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field, field_serializer


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


class Standard(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Maxres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Thumbnails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    default: Default
    medium: Medium
    high: High
    standard: Standard | None = None
    maxres: Maxres | None = None


class Localized(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Snippet(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    published_at: AwareDatetime = Field(..., alias="publishedAt")
    channel_id: str = Field(..., alias="channelId")
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias="channelTitle")
    tags: list[str]
    category_id: str = Field(..., alias="categoryId")
    live_broadcast_content: str = Field(..., alias="liveBroadcastContent")
    default_language: str = Field(..., alias="defaultLanguage")
    localized: Localized
    default_audio_language: str = Field(..., alias="defaultAudioLanguage")


class ContentRating(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    yt_rating: str | None = Field(None, alias="ytRating")


class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    duration: timedelta
    dimension: str
    definition: str
    caption: str
    licensed_content: bool = Field(..., alias="licensedContent")
    content_rating: ContentRating = Field(..., alias="contentRating")
    projection: str

    @field_serializer("duration")
    def serialize_duration(self, value: timedelta) -> timedelta:
        if value == timedelta(days=0):
            return "P0D"
        return value


class Status(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    upload_status: str = Field(..., alias="uploadStatus")
    privacy_status: str = Field(..., alias="privacyStatus")
    license: str
    embeddable: bool
    public_stats_viewable: bool = Field(..., alias="publicStatsViewable")
    made_for_kids: bool = Field(..., alias="madeForKids")


class Statistics(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    view_count: str = Field(..., alias="viewCount")
    like_count: str = Field(..., alias="likeCount")
    favorite_count: str = Field(..., alias="favoriteCount")
    comment_count: str = Field(..., alias="commentCount")


class Player(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    embed_html: str = Field(..., alias="embedHtml")


class Location(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    latitude: float
    longitude: float
    altitude: int


class RecordingDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    location_description: str | None = Field(None, alias="locationDescription")
    location: Location | None = None
    recording_date: AwareDatetime | None = Field(None, alias="recordingDate")


class De(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class En(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Ru(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Ja(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Localizations(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    de: De | None = None
    en: En
    ru: Ru | None = None
    ja: Ja | None = None


class PaidProductPlacementDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    has_paid_product_placement: bool = Field(..., alias="hasPaidProductPlacement")


class TopicDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    topic_categories: list[str] = Field(..., alias="topicCategories")


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias="contentDetails")
    status: Status
    statistics: Statistics
    player: Player
    recording_details: RecordingDetails = Field(..., alias="recordingDetails")
    localizations: Localizations
    paid_product_placement_details: PaidProductPlacementDetails = Field(
        ...,
        alias="paidProductPlacementDetails",
    )
    topic_details: TopicDetails | None = Field(None, alias="topicDetails")


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_results: int = Field(..., alias="totalResults")
    results_per_page: int = Field(..., alias="resultsPerPage")


class NotYtDlapi(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    video_id: str
    part: str
    timestamp: AwareDatetime


class VideoModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    items: list[Item]
    page_info: PageInfo = Field(..., alias="pageInfo")
    not_yt_dlapi: NotYtDlapi

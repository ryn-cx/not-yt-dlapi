# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
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
    published_at: str | AwareDatetime = Field(..., alias="publishedAt")
    channel_id: str = Field(..., alias="channelId")
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias="channelTitle")
    localized: Localized
    default_language: str | None = Field(None, alias="defaultLanguage")


class Status(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    privacy_status: str = Field(..., alias="privacyStatus")
    podcast_status: str | None = Field(None, alias="podcastStatus")


class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    item_count: int = Field(..., alias="itemCount")


class Player(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    embed_html: str = Field(..., alias="embedHtml")


class En(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Localizations(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    en: En


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    status: Status
    content_details: ContentDetails = Field(..., alias="contentDetails")
    player: Player
    localizations: Localizations | None = None


class PlaylistsModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    next_page_token: str | None = Field(None, alias="nextPageToken")
    page_info: PageInfo = Field(..., alias="pageInfo")
    items: list[Item]

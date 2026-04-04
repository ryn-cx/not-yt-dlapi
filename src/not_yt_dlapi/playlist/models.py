# ruff: noqa: D100, D101
from __future__ import annotations

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


class Standard(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Maxres(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Thumbnails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    default: Default
    medium: Medium
    high: High
    standard: Standard | None = None
    maxres: Maxres | None = None


class Localized(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Snippet(BaseModel):
    model_config = ConfigDict(extra="forbid")
    published_at: str = Field(..., alias="publishedAt")
    channel_id: str = Field(..., alias="channelId")
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias="channelTitle")
    localized: Localized
    default_language: str | None = Field(None, alias="defaultLanguage")


class Status(BaseModel):
    model_config = ConfigDict(extra="forbid")
    privacy_status: str = Field(..., alias="privacyStatus")


class ContentDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    item_count: int = Field(..., alias="itemCount")


class Player(BaseModel):
    model_config = ConfigDict(extra="forbid")
    embed_html: str = Field(..., alias="embedHtml")


class En(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Localizations(BaseModel):
    model_config = ConfigDict(extra="forbid")
    en: En


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    status: Status
    content_details: ContentDetails = Field(..., alias="contentDetails")
    player: Player
    localizations: Localizations | None = None


class NotYtDlapi(BaseModel):
    model_config = ConfigDict(extra="forbid")
    channel_id: str
    part: str
    timestamp: AwareDatetime


class PlaylistModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    next_page_token: str | None = Field(None, alias="nextPageToken")
    page_info: PageInfo = Field(..., alias="pageInfo")
    items: list[Item]
    not_yt_dlapi: NotYtDlapi

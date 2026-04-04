# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


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


class ResourceId(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    video_id: str = Field(..., alias="videoId")


class Snippet(BaseModel):
    model_config = ConfigDict(extra="forbid")
    published_at: AwareDatetime = Field(..., alias="publishedAt")
    channel_id: str = Field(..., alias="channelId")
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias="channelTitle")
    playlist_id: str = Field(..., alias="playlistId")
    position: int
    resource_id: ResourceId = Field(..., alias="resourceId")
    video_owner_channel_title: str = Field(..., alias="videoOwnerChannelTitle")
    video_owner_channel_id: str = Field(..., alias="videoOwnerChannelId")


class ContentDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    video_id: str = Field(..., alias="videoId")
    video_published_at: AwareDatetime = Field(..., alias="videoPublishedAt")


class Status(BaseModel):
    model_config = ConfigDict(extra="forbid")
    privacy_status: str = Field(..., alias="privacyStatus")


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias="contentDetails")
    status: Status


class PageInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total_results: int = Field(..., alias="totalResults")
    results_per_page: int = Field(..., alias="resultsPerPage")


class NotYtDlapi(BaseModel):
    model_config = ConfigDict(extra="forbid")
    playlist_id: str
    part: str
    timestamp: AwareDatetime


class PlaylistItemModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    next_page_token: str | None = Field(None, alias="nextPageToken")
    items: list[Item]
    page_info: PageInfo = Field(..., alias="pageInfo")
    not_yt_dlapi: NotYtDlapi

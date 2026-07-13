# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_results: int = Field(..., alias="totalResults")
    results_per_page: int = Field(..., alias="resultsPerPage")


class Medium(GAPIBaseModel):
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
    medium: Medium
    standard: Standard
    maxres: Maxres


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
    localized: Localized


class Status(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    privacy_status: str = Field(..., alias="privacyStatus")


class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    item_count: int = Field(..., alias="itemCount")


class Player(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    embed_html: str = Field(..., alias="embedHtml")


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    status: Status
    content_details: ContentDetails = Field(..., alias="contentDetails")
    player: Player


class PlaylistModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias="pageInfo")
    items: list[Item]

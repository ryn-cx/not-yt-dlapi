# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Snippet(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    channel_id: str = Field(..., alias="channelId")
    position: int
    title: str | None = None


class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    channels: list[str]


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails | None = Field(None, alias="contentDetails")


class ChannelSectionsModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    items: list[Item]

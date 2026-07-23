from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field

class Default(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Medium(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class High(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Standard(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Maxres(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Thumbnails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    default: Default | None = None
    medium: Medium | None = None
    high: High | None = None
    standard: Standard | None = None
    maxres: Maxres | None = None

class ResourceId(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    video_id: str = Field(..., alias='videoId')

class Snippet(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    published_at: AwareDatetime = Field(..., alias='publishedAt')
    channel_id: str = Field(..., alias='channelId')
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias='channelTitle')
    playlist_id: str = Field(..., alias='playlistId')
    position: int
    resource_id: ResourceId = Field(..., alias='resourceId')
    video_owner_channel_title: str | None = Field(None, alias='videoOwnerChannelTitle')
    video_owner_channel_id: str | None = Field(None, alias='videoOwnerChannelId')

class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_id: str = Field(..., alias='videoId')
    video_published_at: AwareDatetime | None = Field(None, alias='videoPublishedAt')
    note: str | None = None

class Status(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    privacy_status: str = Field(..., alias='privacyStatus')

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias='contentDetails')
    status: Status

class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

class PlaylistItemsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    etag: str
    prev_page_token: str | None = Field(None, alias='prevPageToken')
    items: list[Item]
    page_info: PageInfo = Field(..., alias='pageInfo')
    next_page_token: str | None = Field(None, alias='nextPageToken')

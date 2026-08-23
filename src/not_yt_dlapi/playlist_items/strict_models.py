from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field

class Default(BaseModel):
    url: str
    width: int
    height: int

class Medium(BaseModel):
    url: str
    width: int
    height: int

class High(BaseModel):
    url: str
    width: int
    height: int

class Standard(BaseModel):
    url: str
    width: int
    height: int

class Maxres(BaseModel):
    url: str
    width: int
    height: int

class Thumbnails(BaseModel):
    default: Default | None = None
    medium: Medium | None = None
    high: High | None = None
    standard: Standard | None = None
    maxres: Maxres | None = None

class ResourceId(BaseModel):
    kind: str
    video_id: str = Field(..., alias='videoId')

class Snippet(BaseModel):
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

class ContentDetails(BaseModel):
    video_id: str = Field(..., alias='videoId')
    video_published_at: AwareDatetime | None = Field(None, alias='videoPublishedAt')

class Status(BaseModel):
    privacy_status: str = Field(..., alias='privacyStatus')

class Item(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias='contentDetails')
    status: Status

class PageInfo(BaseModel):
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

class PlaylistItemsModel(BaseModel):
    kind: str
    etag: str
    items: list[Item]
    page_info: PageInfo = Field(..., alias='pageInfo')
    next_page_token: str | None = Field(None, alias='nextPageToken')
    prev_page_token: str | None = Field(None, alias='prevPageToken')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input

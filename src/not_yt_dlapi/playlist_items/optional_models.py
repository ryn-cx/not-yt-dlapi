from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Default(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Medium(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class High(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Standard(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Maxres(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default | None = None
    medium: Medium | None = None
    high: High | None = None
    standard: Standard | None = None
    maxres: Maxres | None = None

class ResourceId(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    video_id: str | None = Field(None, alias='videoId')

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore')
    published_at: AwareDatetime | None = Field(None, alias='publishedAt')
    channel_id: str | None = Field(None, alias='channelId')
    title: str | None = None
    description: str | None = None
    thumbnails: Thumbnails | None = None
    channel_title: str | None = Field(None, alias='channelTitle')
    playlist_id: str | None = Field(None, alias='playlistId')
    position: int | None = None
    resource_id: ResourceId | None = Field(None, alias='resourceId')
    video_owner_channel_title: str | None = Field(None, alias='videoOwnerChannelTitle')
    video_owner_channel_id: str | None = Field(None, alias='videoOwnerChannelId')

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    video_published_at: AwareDatetime | None = Field(None, alias='videoPublishedAt')

class Status(BaseModel):
    model_config = ConfigDict(extra='ignore')
    privacy_status: str | None = Field(None, alias='privacyStatus')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    id: str | None = None
    snippet: Snippet | None = None
    content_details: ContentDetails | None = Field(None, alias='contentDetails')
    status: Status | None = None

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    total_results: int | None = Field(None, alias='totalResults')
    results_per_page: int | None = Field(None, alias='resultsPerPage')

class PlaylistItemsModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    items: list[Item] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
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

from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Default(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Medium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class High(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Standard(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Maxres(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Uhd(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Thumbnails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default: Default | Any = Field(default=None, union_mode='left_to_right')
    medium: Medium | Any = Field(default=None, union_mode='left_to_right')
    high: High | Any = Field(default=None, union_mode='left_to_right')
    standard: Standard | Any = Field(default=None, union_mode='left_to_right')
    maxres: Maxres | Any = Field(default=None, union_mode='left_to_right')
    uhd: Uhd | Any = Field(default=None, union_mode='left_to_right')

class ResourceId(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    published_at: AwareDatetime | Any = Field(None, alias='publishedAt', union_mode='left_to_right')
    channel_id: str | Any = Field(None, alias='channelId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnails: Thumbnails | Any = Field(default=None, union_mode='left_to_right')
    channel_title: str | Any = Field(None, alias='channelTitle', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    position: int | Any = Field(default=None, union_mode='left_to_right')
    resource_id: ResourceId | Any = Field(None, alias='resourceId', union_mode='left_to_right')
    video_owner_channel_title: str | Any = Field(None, alias='videoOwnerChannelTitle', union_mode='left_to_right')
    video_owner_channel_id: str | Any = Field(None, alias='videoOwnerChannelId', union_mode='left_to_right')

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    video_published_at: AwareDatetime | Any = Field(None, alias='videoPublishedAt', union_mode='left_to_right')

class Status(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    privacy_status: str | Any = Field(None, alias='privacyStatus', union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    snippet: Snippet | Any = Field(default=None, union_mode='left_to_right')
    content_details: ContentDetails | Any = Field(None, alias='contentDetails', union_mode='left_to_right')
    status: Status | Any = Field(default=None, union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_results: int | Any = Field(None, alias='totalResults', union_mode='left_to_right')
    results_per_page: int | Any = Field(None, alias='resultsPerPage', union_mode='left_to_right')

class PlaylistItemsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    prev_page_token: str | Any = Field(None, alias='prevPageToken', union_mode='left_to_right')
    next_page_token: str | Any = Field(None, alias='nextPageToken', union_mode='left_to_right')
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

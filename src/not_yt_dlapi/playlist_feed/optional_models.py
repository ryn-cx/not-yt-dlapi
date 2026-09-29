from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class LinkItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rel: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class Author(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | Any = Field(default=None, union_mode='left_to_right')
    uri: str | Any = Field(default=None, union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    width: str | Any = Field(default=None, union_mode='left_to_right')
    height: str | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: str | Any = Field(default=None, union_mode='left_to_right')
    height: str | Any = Field(default=None, union_mode='left_to_right')

class StarRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    count: str | Any = Field(default=None, union_mode='left_to_right')
    average: str | Any = Field(default=None, union_mode='left_to_right')
    min: str | Any = Field(default=None, union_mode='left_to_right')
    max: str | Any = Field(default=None, union_mode='left_to_right')

class Statistics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    views: str | Any = Field(default=None, union_mode='left_to_right')

class Community(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    star_rating: StarRating | Any = Field(None, alias='starRating', union_mode='left_to_right')
    statistics: Statistics | Any = Field(default=None, union_mode='left_to_right')

class Group(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    thumbnail: Thumbnail | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    community: Community | Any = Field(default=None, union_mode='left_to_right')

class EntryItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    channel_id: str | Any = Field(None, alias='channelId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    link: list[LinkItem] | Any = Field(default=None, union_mode='left_to_right')
    author: Author | Any = Field(default=None, union_mode='left_to_right')
    published: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    updated: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    group: Group | Any = Field(default=None, union_mode='left_to_right')

class PlaylistFeedModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: list[LinkItem] | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    channel_id: str | Any = Field(None, alias='channelId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    author: Author | Any = Field(default=None, union_mode='left_to_right')
    published: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    entry: list[EntryItem] | Any = Field(default=None, union_mode='left_to_right')
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

from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class LinkItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    rel: str | None = None
    href: str | None = None

class Author(BaseModel):
    model_config = ConfigDict(extra='ignore')
    name: str | None = None
    uri: str | None = None

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    type: str | None = None
    width: str | None = None
    height: str | None = None

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: str | None = None
    height: str | None = None

class StarRating(BaseModel):
    model_config = ConfigDict(extra='ignore')
    count: str | None = None
    average: str | None = None
    min: str | None = None
    max: str | None = None

class Statistics(BaseModel):
    model_config = ConfigDict(extra='ignore')
    views: str | None = None

class Community(BaseModel):
    model_config = ConfigDict(extra='ignore')
    star_rating: StarRating | None = Field(None, alias='starRating')
    statistics: Statistics | None = None

class Group(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    content: Content | None = None
    thumbnail: Thumbnail | None = None
    description: str | None = None
    community: Community | None = None

class EntryItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    video_id: str | None = Field(None, alias='videoId')
    channel_id: str | None = Field(None, alias='channelId')
    title: str | None = None
    link: list[LinkItem] | None = None
    author: Author | None = None
    published: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    group: Group | None = None

class PlaylistFeedModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    link: list[LinkItem] | None = None
    id: str | None = None
    playlist_id: str | None = Field(None, alias='playlistId')
    channel_id: str | None = Field(None, alias='channelId')
    title: str | None = None
    author: Author | None = None
    published: AwareDatetime | None = None
    entry: list[EntryItem] | None = None
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

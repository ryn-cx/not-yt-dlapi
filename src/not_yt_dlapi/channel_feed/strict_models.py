from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field

class LinkItem(BaseModel):
    rel: str
    href: str

class Author(BaseModel):
    name: str
    uri: str

class Content(BaseModel):
    url: str
    type: str
    width: str
    height: str

class Thumbnail(BaseModel):
    url: str
    width: str
    height: str

class StarRating(BaseModel):
    count: str
    average: str
    min: str
    max: str

class Statistics(BaseModel):
    views: str

class Community(BaseModel):
    star_rating: StarRating = Field(..., alias='starRating')
    statistics: Statistics

class Group(BaseModel):
    title: str
    content: Content
    thumbnail: Thumbnail
    description: str
    community: Community

class EntryItem(BaseModel):
    id: str
    video_id: str = Field(..., alias='videoId')
    channel_id: str = Field(..., alias='channelId')
    title: str
    link: list[LinkItem]
    author: Author
    published: AwareDatetime
    updated: AwareDatetime
    group: Group

class ChannelFeedModel(BaseModel):
    link: list[LinkItem]
    id: str
    channel_id: str = Field(..., alias='channelId')
    title: str
    author: Author
    published: AwareDatetime
    entry: list[EntryItem]
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

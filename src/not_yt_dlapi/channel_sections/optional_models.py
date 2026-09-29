from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    channel_id: str | Any = Field(None, alias='channelId', union_mode='left_to_right')
    position: int | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    channels: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    snippet: Snippet | Any = Field(default=None, union_mode='left_to_right')
    content_details: ContentDetails | Any = Field(None, alias='contentDetails', union_mode='left_to_right')

class ChannelSectionsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
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

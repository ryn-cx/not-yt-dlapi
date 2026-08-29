from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field

class Snippet(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    channel_id: str = Field(..., alias='channelId')
    position: int
    title: str | None = None

class ContentDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    channels: list[str]

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails | None = Field(None, alias='contentDetails')

class ChannelSectionsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kind: str
    etag: str
    items: list[Item]
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

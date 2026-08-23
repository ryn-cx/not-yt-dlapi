from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    channel_id: str | None = Field(None, alias='channelId')
    position: int | None = None
    title: str | None = None

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    channels: list[str] | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    id: str | None = None
    snippet: Snippet | None = None
    content_details: ContentDetails | None = Field(None, alias='contentDetails')

class ChannelSectionsModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    items: list[Item] | None = None
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

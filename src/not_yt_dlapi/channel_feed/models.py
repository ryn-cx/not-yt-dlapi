# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ChannelFeedModel as OptionalModel
from .strict_models import ChannelFeedModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Author,
        ChannelFeedModel,
        Community,
        Content,
        EntryItem,
        Group,
        LinkItem,
        StarRating,
        Statistics,
        Thumbnail,
    )
else:
    from .optional_models import (
        Author,
        ChannelFeedModel,
        Community,
        Content,
        EntryItem,
        Group,
        LinkItem,
        StarRating,
        Statistics,
        Thumbnail,
    )

__all__ = [
    "Author",
    "ChannelFeedModel",
    "Community",
    "Content",
    "EntryItem",
    "Group",
    "LinkItem",
    "StarRating",
    "Statistics",
    "Thumbnail",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ChannelFeedModel:
    """Read a downloaded file into ChannelFeedModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

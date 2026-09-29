# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import PlaylistItemsModel as OptionalModel
from .strict_models import PlaylistItemsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ContentDetails,
        Default,
        High,
        Item,
        Maxres,
        Medium,
        PageInfo,
        PlaylistItemsModel,
        ResourceId,
        Snippet,
        Standard,
        Status,
        Thumbnails,
        Uhd,
    )
else:
    from .optional_models import (
        ContentDetails,
        Default,
        High,
        Item,
        Maxres,
        Medium,
        PageInfo,
        PlaylistItemsModel,
        ResourceId,
        Snippet,
        Standard,
        Status,
        Thumbnails,
        Uhd,
    )

__all__ = [
    "ContentDetails",
    "Default",
    "High",
    "Item",
    "Maxres",
    "Medium",
    "PageInfo",
    "PlaylistItemsModel",
    "ResourceId",
    "Snippet",
    "Standard",
    "Status",
    "Thumbnails",
    "Uhd",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> PlaylistItemsModel:
    """Read a downloaded file into PlaylistItemsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

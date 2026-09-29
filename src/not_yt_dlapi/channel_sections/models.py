# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ChannelSectionsModel as OptionalModel
from .strict_models import ChannelSectionsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ChannelSectionsModel,
        ContentDetails,
        Item,
        Snippet,
    )
else:
    from .optional_models import (
        ChannelSectionsModel,
        ContentDetails,
        Item,
        Snippet,
    )

__all__ = [
    "ChannelSectionsModel",
    "ContentDetails",
    "Item",
    "Snippet",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ChannelSectionsModel:
    """Read a downloaded file into ChannelSectionsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

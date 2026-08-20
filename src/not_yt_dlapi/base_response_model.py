# TODO: Validate
"""Base class for what an endpoint reads its response into."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Self

from pydantic import BaseModel


# TODO: Validate
class BaseResponseModel(BaseModel, ABC):
    """What an endpoint reads its response into.

    Every endpoint has a model of its own, and what they have in common is only
    that they are read from a response. Saying that here rather than in a
    protocol the tests keep is what makes a model that does not read one a
    failure where it is written instead of where it is used.
    """

    # TODO: Validate
    @classmethod
    @abstractmethod
    def from_response(cls, data: Any) -> Self:  # noqa: ANN401 - A response body can be any JSON value.
        """Return the model the response is read into."""

# TODO: Validate
"""Base class for what an endpoint reads its response into."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Self

from pydantic import BaseModel, Field


# TODO: Validate
class BaseResponseModel(BaseModel, ABC):
    """What an endpoint reads its response into.

    Every endpoint has a model of its own, and what they have in common is that
    they are read from a response and keep the response they were read from.
    Saying that here rather than in a protocol the tests keep is what makes a
    model that does neither a failure where it is written instead of where it is
    used.

    Attributes:
        raw: The response as it was served, which is the document itself rather
            than the reading of it. It is left out of what the model dumps to,
            since a dump holding it is the whole response again.
    """

    raw: str = Field(repr=False, exclude=True)

    # TODO: Validate
    @classmethod
    @abstractmethod
    def from_response(cls, data: Any) -> Self:  # noqa: ANN401 - A response body can be any JSON value.
        """Return the model the response is read into."""

# TODO: Validate
"""Contains the Endpoint base class.

The base every hand-parsed endpoint is built on. It holds the client the
request goes through and the log id a download is named by, and nothing else:
the response classes do their own reading, so there is no model machinery here
to inherit.
"""

from __future__ import annotations

import json
from inspect import Parameter, signature
from typing import TYPE_CHECKING, Any

from not_yt_dlapi.base_response_model import BaseResponseModel

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class BaseEndpoint:
    """Base class for API endpoints."""

    # TODO: Validate
    def __init__(self, client: NotYTDLAPI) -> None:
        """Initialize the endpoint with the NotYTDLAPI client."""
        self._client = client

    # TODO: Validate
    @staticmethod
    def non_default_args(
        func: Callable[..., Any],
        values: dict[str, Any],
    ) -> dict[str, Any]:
        """Return the args that are changed from their default values."""
        return {
            name: values[name]
            for name, param in signature(func).parameters.items()
            if param.default is not Parameter.empty
            and name in values
            and values[name] != param.default
        }

    # TODO: Validate
    def get_log_id(self, func: Callable[..., Any], values: dict[str, Any]) -> str:
        """Get the log id.

        Example: ClassName (arg1='value1' arg2='value2')
        """
        required = {
            name: values[name]
            for name, param in signature(func).parameters.items()
            if param.default is Parameter.empty and name in values
        }
        set_args = {**required, **self.non_default_args(func, values)}
        parts = [
            *(f"{name}={value!r}" for name, value in set_args.items()),
        ]
        name = self.__class__.__name__
        if not parts:
            return name
        return f"{name} ({' '.join(parts)})"

    # TODO: Validate
    @staticmethod
    def split[ResponseT: BaseResponseModel](
        load: Callable[[str], ResponseT],
        pages: Iterable[str],
    ) -> list[ResponseT]:
        """Put every item several requests answered with in a response of its own.

        A `list_all` asks in batches or walks pages, so what it has to hand is
        several responses where the caller asked one question. Splitting them
        gives one response per item, each carrying whatever the response it
        arrived in said around it, which is describing a request that was never
        made: no one request answered with exactly that one item.

        The reading is the model's own `from_response`, so what a `list_all`
        answers with was read the same way a `list` would have read it.

        Nothing found is no responses rather than one holding nothing.

        A response holding one item is written out again for the model to read,
        since a response is text now and there is no such text to hand: what one
        of these carries on `raw` is a response nobody was ever served, which is
        the same thing its paging tokens are.
        """
        return [
            load(json.dumps({**page, "items": [item]}))
            for page in map(json.loads, pages)
            for item in page.get("items", ())
        ]

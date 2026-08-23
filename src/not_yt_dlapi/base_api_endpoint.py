# TODO: Validate
"""Contains BaseEndpoint."""

from __future__ import annotations

import json
from inspect import Parameter, signature
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

    from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
class BaseEndpoint:
    """Base class for API endpoints."""

    def __init__(self, client: NotYTDLAPI) -> None:
        """Initialize the endpoint with the NotYTDLAPI client."""
        self._client = client

    # TODO: Validate
    @staticmethod
    def merge_pages(pages: list[str]) -> str:
        """Return the pages of one listing written out as a single file.

        The first page is what the merged file is built on, since everything it
        says around the items is what the listing is, and its items are replaced
        by the items of every page in the order they were served. The paging
        tokens are dropped: they name a page of a walk that is over, and a file
        holding the whole listing is not a page of anything.

        Raises:
            ValueError: If there are no pages, since there is nothing to say the
                listing was answered with.
        """
        if not pages:
            msg = "Expected at least one page, got none."
            raise ValueError(msg)

        documents: list[dict[str, Any]] = [json.loads(page) for page in pages]
        merged = dict(documents[0])
        merged["items"] = [
            item for document in documents for item in document.get("items", ())
        ]
        merged.pop("nextPageToken", None)
        merged.pop("prevPageToken", None)
        return json.dumps(merged)

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

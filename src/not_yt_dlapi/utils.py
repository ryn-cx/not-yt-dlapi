# TODO: Validate
"""Helpers for reading the page browse answers with.

Browse is not the API. It is what the watch site runs on, and what it answers
with is the site's own drawing of a page rather than a documented resource, so
finding anything in it is a matter of looking for what a thing is written as.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterator


# TODO: Validate
def find(node: Any, key: str) -> Iterator[Any]:  # noqa: ANN401 - Browse data is any JSON.
    """Yield every value filed under `key`, however deep in the data it is.

    Where browse writes a thing moves as the site is rebuilt, and what is wanted
    from it here is one named thing rather than a path to it, so it is looked
    for by name everywhere rather than reached for where it last was.
    """
    if isinstance(node, dict):
        for name, value in node.items():
            if name == key:
                yield value
            yield from find(value, key)
    elif isinstance(node, list):
        for value in node:
            yield from find(value, key)


# TODO: Validate
def read_continuation(browsed: dict[str, Any]) -> str | None:
    """Return what the rest of a listing is asked for by, if there is more.

    Browse hands out a long listing a stretch at a time, and an answer that is
    not the last of them ends in the token the next is asked for by.
    """
    return next(
        (
            renderer["continuationEndpoint"]["continuationCommand"]["token"]
            for renderer in find(browsed, "continuationItemRenderer")
            if "continuationEndpoint" in renderer
        ),
        None,
    )

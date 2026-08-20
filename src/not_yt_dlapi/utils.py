# TODO: Validate
"""What reading browse takes, which both the download and the models need.

Browse is not the API. It is what the watch site runs on, and what it answers
with is the site's own drawing of a page rather than a documented resource, so
finding anything in it is a matter of looking for what a thing is written as.

The download needs this to know what to ask for next and the models need it to
know what an answer holds, so it belongs to neither of them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from urllib.parse import parse_qs, urlsplit

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
def read_text(node: dict[str, Any]) -> str:
    """Return the text of a node, which browse writes one of two ways.

    A string is written either as itself or as the runs it is styled in, and
    which of the two is used is the site's business rather than the reader's, so
    both are read as the text they spell.
    """
    if "simpleText" in node:
        simple: str = node["simpleText"]
        return simple
    return "".join(run["text"] for run in node.get("runs", ()))


# TODO: Validate
def read_seasons(
    browsed: dict[str, Any],
) -> tuple[dict[int, dict[str, Any]], int | None]:
    """Return what each season is asked for by, and which one is already here.

    A show of more than one season is one playlist with a menu over it, and
    asking for the playlist gives whichever season the menu starts on rather
    than all of them. Each season is its own thing to ask browse for, so a whole
    show takes one request per season, less the one already answered: the menu
    says which season that is, and it is not asked for twice.

    The menu a season is chosen from is the menu a playlist is sorted from, so
    what tells the two apart is that a season says which season it is. It says
    so in the address a person would read it at rather than in the endpoint it
    is asked for by, which is why the number is taken from there.

    A playlist with nothing to choose between has no seasons and none open.
    """
    menu = next(find(browsed, "sortFilterSubMenuRenderer"), None)
    if menu is None:
        return {}, None

    seasons: dict[int, dict[str, Any]] = {}
    open_season: int | None = None
    for item in menu.get("subMenuItems", ()):
        endpoint = item.get("navigationEndpoint")
        if endpoint is None:
            continue
        path = endpoint["commandMetadata"]["webCommandMetadata"]["url"]
        numbers = parse_qs(urlsplit(path).query).get("season", ())
        if not numbers or not numbers[0].isdigit():
            continue
        number = int(numbers[0])
        seasons[number] = endpoint["browseEndpoint"]
        if item.get("selected"):
            open_season = number
    return seasons, open_season


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

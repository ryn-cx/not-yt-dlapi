# TODO: Validate
"""Reads the Atom feed YouTube serves into the JSON it is equivalent to.

The feed is not the Data API. It is an Atom document served from
`youtube.com/feeds/videos.xml`, it takes no key, and it hands out the most
recent fifteen videos and nothing else. `read_feed` is what turns it into the
dict the feed's model is validated from, and the model generator reads the
recorded feeds with the same function so the two can never disagree.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from xml.etree.ElementTree import fromstring

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


PLURAL = frozenset({"link", "entry"})
"""The elements a feed can carry more than one of, always read as a list.

Everything else arrives at most once and is read as itself. Deciding this by
name rather than by how many happened to arrive is what keeps a feed holding one
video the same shape as a feed holding fifteen, so a model never has to say a
thing is either an object or a list of them.
"""


# TODO: Validate
def _name(element: Element) -> str:
    """Return the element's name with the namespace it is written in dropped.

    An element parsed out of a namespaced document is named
    `{http://www.youtube.com/xml/schemas/2015}videoId`, which is the same thing
    the feed writes as `yt:videoId`. Nothing here needs to tell two namespaces
    apart, because no two elements inside one element share a name once the
    namespace is gone, so the name alone is enough to file it under.
    """
    _, _, name = element.tag.rpartition("}")
    return name


# TODO: Validate
def _read(element: Element) -> Any:  # noqa: ANN401 - An element is read as whatever it holds.
    """Return the element as the JSON it is equivalent to.

    An element in this feed carries exactly one of three things, so which of the
    three it is decides what it is read as:

    - other elements, which is an object of them, attributes included;
    - attributes only, which is an object of those;
    - text, which is the text itself. An element written open-and-closed with
      nothing between carries no text at all and is read as an empty string,
      since a video described with nothing is described with nothing rather than
      undescribed.
    """
    children = list(element)
    if not children:
        if element.attrib:
            return dict(element.attrib)
        return element.text or ""

    read: dict[str, Any] = dict(element.attrib)
    for child in children:
        name = _name(child)
        value = _read(child)
        if name in PLURAL:
            read.setdefault(name, []).append(value)
        else:
            read[name] = value
    return read


# TODO: Validate
def read_feed(xml: str) -> dict[str, Any]:
    """Return the feed document as the JSON it is equivalent to.

    Nothing is left behind and nothing is renamed beyond dropping namespaces, so
    what comes back is the document itself in the only shape the rest of the
    library keeps a downloaded response in.

    Raises:
        ParseError: If the document is not XML, which is something other than
            the feed answering.
    """
    return _read(fromstring(xml))  # noqa: S314 - The feed is YouTube's own document.

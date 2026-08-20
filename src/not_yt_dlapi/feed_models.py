# TODO: Validate
"""The feed of videos a channel or a playlist publishes, and how it is read.

The feed is not the Data API. It is an Atom document served from
`youtube.com/feeds/videos.xml`, it takes no key, and it hands out the most
recent fifteen videos and nothing else: there is no paging and no way to ask for
more. What it does give is given without spending quota, which is the whole
reason to ask it rather than `playlistItems.list`.

A channel feed and a playlist feed are the same document with one field
different, so everything but that field is described once here and the two
endpoints each add the field that names what they asked about.

Every model here is shaped the way the feed is written: one class per element
that carries other elements, one field per element or attribute inside it. The
names are the feed's own, in snake_case and read back through the camelCase the
feed writes them in. The namespace an element is written in is dropped, since no
two elements in one place share a name once it is.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Self, override
from xml.etree.ElementTree import fromstring

from pydantic import Field, SkipValidation

from not_yt_dlapi.base_response_model import BaseResponseModel
from not_yt_dlapi.common_models import APIModel

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


# TODO: Validate
class FeedLink(APIModel):
    """One of the links a feed or an entry points at.

    Attributes:
        rel: What the link is to what carries it. A feed carries a `self` link,
            which is the address it was asked for at, and an `alternate` link,
            which is the page a person would read it on. An entry carries only
            the `alternate` link.
        href: The address the link points at.
    """

    rel: str
    href: str


# TODO: Validate
class FeedAuthor(APIModel):
    """Who published a feed or an entry, which is the channel either way.

    Attributes:
        name: The channel's title.
        uri: The address of the channel's page.
    """

    name: str
    uri: str


# TODO: Validate
class MediaContent(APIModel):
    """Where the video itself is, as the feed still describes it.

    The feed hands out a Flash player address, which nothing has been able to
    play for years. It is kept because it is in the document, not because it is
    of any use.

    Attributes:
        url: The address of the player.
        type: The MIME type of the player, which is always
            `application/x-shockwave-flash`.
        width: The player's width.
        height: The player's height.
    """

    url: str
    type: str
    width: int
    height: int


# TODO: Validate
class MediaThumbnail(APIModel):
    """The one thumbnail the feed gives, which is the `hqdefault` one.

    Attributes:
        url: The image's URL.
        width: The image's width.
        height: The image's height.
    """

    url: str
    width: int
    height: int


# TODO: Validate
class MediaStarRating(APIModel):
    """How the video was rated, written the way a five star rating would be.

    YouTube stopped rating out of five long ago and now counts likes, so what
    this actually says is that `count` people liked the video and every one of
    them is reported as having given it five stars.

    Attributes:
        count: The number of ratings, which is the number of likes.
        average: The average rating, which is `5.00` for a video with any likes
            at all.
        min: The lowest rating that could be given, which is always `1`.
        max: The highest rating that could be given, which is always `5`.
    """

    count: int
    average: float
    min: int
    max: int


# TODO: Validate
class MediaStatistics(APIModel):
    """How much the video was watched.

    Attributes:
        views: The number of times the video has been viewed.
    """

    views: int


# TODO: Validate
class MediaCommunity(APIModel):
    """What everyone other than the uploader did with the video.

    Attributes:
        star_rating: How the video was rated. A video whose uploader hid its
            likes carries no rating.
        statistics: How much the video was watched. A video whose uploader hid
            its view count carries no statistics.
    """

    star_rating: MediaStarRating | None = None
    statistics: MediaStatistics | None = None


# TODO: Validate
class MediaGroup(APIModel):
    """Everything the entry says about the video rather than about the posting.

    Attributes:
        title: The video's title, which is the same title the entry itself
            carries.
        content: Where the video itself is, as the feed still describes it.
        thumbnail: The one thumbnail the feed gives.
        description: The video's description. A video described with nothing
            carries an empty description rather than none.
        community: What everyone other than the uploader did with the video. A
            video whose uploader hid both its likes and its view count carries
            nothing here at all.
    """

    title: str
    content: MediaContent
    thumbnail: MediaThumbnail
    description: str
    community: MediaCommunity | None = None


# TODO: Validate
class FeedEntry(APIModel):
    """One video in a feed.

    Attributes:
        id: What the feed names the entry, which is `yt:video:` and then the
            video's id.
        video_id: The ID that YouTube uses to uniquely identify the video.
        channel_id: The ID of the channel that uploaded the video. In a playlist
            feed this is the uploader rather than the playlist's owner, so it is
            not the same for every entry.
        title: The video's title.
        links: The links the entry points at, which is the video's page. A short
            is linked at `/shorts/` rather than at `/watch`, so this is also the
            only thing in the feed that says a video is one.
        author: The channel that uploaded the video.
        published: The date and time the video was published, in ISO 8601
            format.
        updated: The date and time the video was last changed, in ISO 8601
            format. A video published and never touched again is still updated
            some minutes after it was published, as YouTube finishes with it.
        media_group: Everything the entry says about the video rather than about
            the posting.
    """

    id: str
    video_id: str
    channel_id: str
    title: str
    links: tuple[FeedLink, ...] = Field(alias="link")
    author: FeedAuthor
    published: str
    updated: str
    media_group: MediaGroup = Field(alias="group")


# TODO: Validate
class FeedResponse(BaseResponseModel, APIModel):
    """The fifteen most recent videos of whatever was asked about.

    What a feed says about itself is what the thing publishing it is called and
    when that thing began, and then the videos. There is no `etag`, no paging
    and no count of how many there are in total, because the feed is only ever
    the newest fifteen.

    Attributes:
        id: What the feed names itself, which is `yt:channel:` or `yt:playlist:`
            and then an id. For a channel that id is the channel's id with the
            leading `UC` taken off, which is not an id anything else accepts.
        links: The links the feed points at: the address it was asked for at,
            and the page a person would read it on.
        title: The title of the channel or playlist the feed is of.
        author: Who publishes the feed. A channel publishes its own; a playlist
            is published by YouTube rather than by whoever made it.
        published: The date and time the channel or playlist was created, in ISO
            8601 format.
        entries: The videos, newest first. A channel that has published nothing
            has none.
        raw: The feed as it was downloaded, which is the XML document itself
            rather than anything made of it.
    """

    id: str
    links: tuple[FeedLink, ...] = Field(alias="link")
    title: str
    author: FeedAuthor
    published: str
    # A feed with nothing in it has no `entry` elements at all.
    entries: tuple[FeedEntry, ...] = Field(alias="entry", default=())
    raw: SkipValidation[str] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: str) -> Self:
        """Read a feed out of the XML it was served as.

        Reading the document is the model's rather than the downloader's, so
        what is downloaded, and so what a recording of it holds, is the document
        exactly as it was served.

        Raises:
            ParseError: If the document is not XML, which is something other
                than the feed answering.
        """
        return cls.model_validate({**read_feed(data), "raw": data})

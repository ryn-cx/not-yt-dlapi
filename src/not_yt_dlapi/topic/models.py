# TODO: Validate
"""Topic channel models.

A Topic channel is generated for a musician rather than made by one, and its
page is a shelf of the albums and singles YouTube has for them. The API does not
describe any of this, so the models are shaped after what browse answers with.

https://www.youtube.com/channel/UCooTDYkIERWBwDC1JKyoElQ
"""

from __future__ import annotations

import json
from typing import Any, Self, override

from pydantic import Field

from not_yt_dlapi.base_response_model import BaseResponseModel
from not_yt_dlapi.common_models import APIModel
from not_yt_dlapi.utils import (
    find,
    read_continuation,
    read_text,
    strip_url_parameters,
)


# TODO: Validate
def read_credit(byline: str) -> tuple[list[str], str | None]:
    """Split "Madvillain, Madlib, MF Doom · Jan 13, 2026" into names and a date.

    The separator is a middle dot rather than the bullet a music playlist's
    subtitle uses.
    """
    credit, _, released = byline.rpartition(" · ")
    if not credit:
        return [], released or None
    return [name.strip() for name in credit.split(",")], released


# TODO: Validate
class TopicThumbnail(APIModel):
    """One of the images a release is pictured by.

    Attributes:
        url: The image's URL.
        width: The image's width.
        height: The image's height.
    """

    url: str
    width: int
    height: int


# TODO: Validate
class TopicRelease(APIModel):
    """One album or single, as the channel lists it.

    Attributes:
        playlist_id: The ID of the playlist the release is published as.
        title: The release's name.
        artists: Everyone the release is credited to, in the order it credits
            them.
        released_text: When it came out, written the way it is shown.
        track_count: How many songs are on it.
        thumbnails: The images the release is pictured by, smallest first.
    """

    playlist_id: str
    title: str
    artists: list[str] = Field(default_factory=list)
    released_text: str | None = None
    track_count: int | None = None
    thumbnails: list[TopicThumbnail] = Field(default_factory=list)

    # TODO: Validate
    @classmethod
    def from_grid(cls, entry: dict[str, Any]) -> Self:
        """Read a release as the panel writes it."""
        artists, released_text = read_credit(read_text(entry["shortBylineText"]))
        count = entry.get("videoCountShortText")
        return cls(
            playlist_id=entry["playlistId"],
            title=read_text(entry["title"]),
            artists=artists,
            released_text=released_text,
            track_count=None if count is None else int(read_text(count)),
            thumbnails=read_images(entry.get("thumbnail", {})),
        )

    # TODO: Validate
    @classmethod
    def from_lockup(cls, lockup: dict[str, Any]) -> Self:
        """Read a release as the shelf writes it."""
        metadata = lockup["metadata"]["lockupMetadataViewModel"]
        rows = [
            [part["text"]["content"] for part in row.get("metadataParts", ())]
            for row in metadata["metadata"]["contentMetadataViewModel"]["metadataRows"]
        ]
        credit = rows[0] if rows else []
        songs = next(
            (
                badge["text"]
                for badge in find(lockup["contentImage"], "thumbnailBadgeViewModel")
                if "text" in badge
            ),
            "",
        )
        return cls(
            playlist_id=lockup["contentId"],
            title=metadata["title"]["content"],
            artists=[name.strip() for name in credit[0].split(",")] if credit else [],
            released_text=credit[1] if len(credit) > 1 else None,
            # The badge reads "14 songs", so the count is the number in front.
            track_count=int(songs.split(" ")[0]) if songs[:1].isdigit() else None,
            thumbnails=read_images(lockup["contentImage"]),
        )


# TODO: Validate
def read_images(node: Any) -> list[TopicThumbnail]:  # noqa: ANN401 - Browse data is any JSON.
    """Return every image under a node, in the order they are written."""
    return [
        TopicThumbnail(**image | {"url": strip_url_parameters(image["url"])})
        for key in ("thumbnails", "sources")
        for images in find(node, key)
        for image in images
        if "url" in image
    ]


# TODO: Validate
class TopicReleases(BaseResponseModel, APIModel):
    """One stretch of the albums and singles a Topic channel lists.

    Opening the channel answers with the dozen releases its shelf shows and the
    token the rest are asked for by. Every stretch after that is a page of the
    panel behind the shelf's "View all".

    Attributes:
        channel_id: The ID of the channel the releases are of, which only the
            answer to opening the channel says.
        releases: The releases this stretch listed, in the order it listed them.
        continuation: What the stretch after this one is asked for by, which is
            nothing once there are no more releases.
        raw: The answer browse gave, as it was served.
    """

    channel_id: str | None = None
    releases: list[TopicRelease] = Field(default_factory=list)
    continuation: str | None = None
    raw: str = Field(repr=False, exclude=True)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: str) -> Self:
        """Read one answer browse gave.

        A shelf writes its releases as lockups and the panel behind it writes
        them as grid entries, so both are read into the same release.
        """
        browsed = json.loads(data)
        shelf = next(find(browsed, "shelfRenderer"), None)
        grid = [
            entry["gridPlaylistRenderer"]
            for entry in find(browsed, "items")
            for entry in entry
            if "gridPlaylistRenderer" in entry
        ]

        return cls(
            channel_id=next(find(browsed.get("metadata", {}), "externalId"), None),
            releases=(
                [TopicRelease.from_grid(entry) for entry in grid]
                if grid
                else [
                    TopicRelease.from_lockup(lockup)
                    for lockup in find(shelf or {}, "lockupViewModel")
                ]
            ),
            # The shelf's own token is what opens the panel holding every
            # release, and a panel page ends with the token for the next.
            continuation=(
                next(find(shelf["endpoint"], "token"), None)
                if shelf is not None
                else read_continuation(browsed)
            ),
            raw=data,
        )

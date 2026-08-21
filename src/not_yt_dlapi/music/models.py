# TODO: Validate
"""Music models.

Shaped after what browse answers with rather than after anything the API
documents, because the API documents nothing useful here: it will hand out an
auto-generated album playlist, but it says the playlist belongs to YouTube and
never says whose music it is. One class per thing browse writes, one field per
thing that thing says, named the way browse names it but in snake_case.

Browse writes the tracks of a music playlist as lockups rather than as the
playlist entries a show is written in, and a lockup says who published the
track, how long it runs, how often it has been watched and how long ago it went
up. It does not number itself, so a track's place in the album is where it sits
in the listing. The answer itself is kept on `raw`, so what browse said and this
does not read is still there to read.
"""

from __future__ import annotations

import json
from collections import Counter
from typing import Any, Self, override

from pydantic import Field

from not_yt_dlapi.base_response_model import BaseResponseModel
from not_yt_dlapi.common_models import APIModel
from not_yt_dlapi.utils import find, read_continuation, read_text, strip_url_parameters


# TODO: Validate
def read_credit(subtitle: dict[str, Any] | None) -> tuple[list[str], str | None]:
    """Return who a playlist is credited to and what kind of release it is.

    The credit is one line reading `Future, Metro Boomin • Album`: everyone the
    release is put out under, then what the release is. It is the only thing in
    an answer that names more than one musician, since every track is published
    by whichever single channel uploaded it, so a collaboration is only ever
    known from here.

    The names are separated by commas and nothing marks where one ends, so an
    artist whose own name has a comma in it comes back as two. Nothing in the
    answer says otherwise, so nothing here can do better.

    A playlist that is not a release says no credit at all, and one that says
    only what kind of release it is is read as the release with nobody credited.
    """
    if subtitle is None:
        return [], None

    credit, _, release_type = read_text(subtitle).rpartition(" • ")
    if not credit:
        return [], release_type or None
    return [name.strip() for name in credit.split(",")], release_type


# TODO: Validate
class MusicThumbnail(APIModel):
    """One of the images a playlist or a track is pictured by.

    Attributes:
        url: The image's URL.
        width: The image's width.
        height: The image's height.
    """

    url: str
    width: int
    height: int


# TODO: Validate
def read_images(node: Any, key: str) -> list[MusicThumbnail]:  # noqa: ANN401 - Browse data is any JSON.
    """Return every image written under `key`, in the order they are written.

    An image that is a piece of the site rather than a picture of something says
    which piece it is instead of where it is served from, so it is passed over.
    """
    return [
        MusicThumbnail(**image | {"url": strip_url_parameters(image["url"])})
        for images in find(node, key)
        for image in images
        if "url" in image
    ]


# TODO: Validate
class MusicTrack(APIModel):
    """One track of a music playlist, as browse lists it.

    Attributes:
        video_id: The ID that YouTube uses to uniquely identify the video.
        title: The track's title, which is the video's title and so is as often
            `Artist - Song (Official Audio)` as it is the name of the song.
        channel_title: The channel that published the track, named the way the
            listing names it.
        channel_id: The ID of that channel.
        length_text: How long the track runs, written the way it is shown.
        view_count_text: How often the track has been watched, written the way
            it is shown, which is rounded and not a number.
        published_text: How long ago the track went up, written the way it is
            shown, which is relative to whenever the answer was given.
        thumbnails: The images the track is pictured by, smallest first.
    """

    video_id: str
    title: str
    channel_title: str | None = None
    channel_id: str | None = None
    length_text: str | None = None
    view_count_text: str | None = None
    published_text: str | None = None
    thumbnails: list[MusicThumbnail] = Field(default_factory=list)

    # TODO: Validate
    @classmethod
    def from_lockup(cls, lockup: dict[str, Any]) -> Self:
        """Read one lockup as browse wrote it.

        The rows under a track are the channel that published it and then how
        often it has been watched and how long ago it went up, in that order and
        with nothing naming either. So they are read as the places they are
        written in, which is all a lockup gives to go on.
        """
        metadata = lockup["metadata"]["lockupMetadataViewModel"]
        rows = [
            [part["text"]["content"] for part in row.get("metadataParts", ())]
            for row in metadata["metadata"]["contentMetadataViewModel"]["metadataRows"]
        ]
        channel, *rest = rows or [[]]
        stats = rest[0] if rest else []

        return cls(
            video_id=lockup["contentId"],
            title=metadata["title"]["content"],
            channel_title=channel[0] if channel else None,
            # The avatar beside a track is the channel's, so what tapping it
            # opens is that channel, which is the one id a lockup carries.
            channel_id=next(find(metadata.get("image", {}), "browseId"), None),
            length_text=next(
                (
                    badge["text"]
                    for badge in find(lockup["contentImage"], "thumbnailBadgeViewModel")
                    if "text" in badge
                ),
                None,
            ),
            view_count_text=stats[0] if stats else None,
            published_text=stats[1] if len(stats) > 1 else None,
            thumbnails=read_images(lockup["contentImage"], "sources"),
        )


# TODO: Validate
class MusicPlaylist(BaseResponseModel, APIModel):
    """One stretch of a music playlist that browse listed, and the tracks on it.

    Browse hands out a long listing a stretch at a time, and only the first of
    them carries the header, because the ones after it are the rest of a listing
    already asked for rather than the playlist again. So everything the header
    says is missing from a stretch that is not the first, and what such a
    stretch holds is tracks and the token for the one after it.

    Attributes:
        playlist_id: The ID that YouTube uses to uniquely identify the playlist.
        title: The playlist's title, which for a release is the release's name.
        artists: Everyone the release is credited to, in the order it credits
            them, so a collaboration holds every musician on it rather than only
            the one whose channel the tracks went up on.
        release_type: What kind of release it is, written the way it is shown
            and so in whatever language the answer came back in: `Album`,
            `Single` and `EP` are what an auto-generated playlist says.
        thumbnails: The images the playlist is pictured by, which for a release
            is its cover art, smallest first. The URL is signed and expires, so
            what to do about that is the caller's.
        artist_channel_id: The channel of the musician whose release this is,
            which is the channel that published the tracks. A release is put out
            on one channel however many people are credited on it, so this names
            the main musician and `artists` is what names the rest. It is read
            from the tracks, so a stretch holding none names nobody.
        tracks: The tracks this stretch listed, in the order it listed them,
            which is the order they are in on the release.
        continuation: What the stretch after this one is asked for by, which is
            nothing once there is no more of the listing.
        raw: The answer browse gave, as it was served.
    """

    playlist_id: str | None = None
    title: str | None = None
    artists: list[str] = Field(default_factory=list)
    release_type: str | None = None
    artist_channel_id: str | None = None
    thumbnails: list[MusicThumbnail] = Field(default_factory=list)
    tracks: list[MusicTrack] = Field(default_factory=list)
    continuation: str | None = None
    raw: str = Field(repr=False, exclude=True)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: str) -> Self:
        """Read one answer browse gave.

        A lockup is how browse writes anything it lists, and a music playlist
        has been seen listing nothing but videos, so anything else one is ever
        written for is not a track and is left out rather than read as one.
        """
        browsed = json.loads(data)
        header = next(find(browsed, "playlistHeaderRenderer"), {})
        artists, release_type = read_credit(header.get("subtitle"))
        title = header.get("title")
        tracks = [
            MusicTrack.from_lockup(lockup)
            for lockup in find(browsed, "lockupViewModel")
            if lockup.get("contentType") == "LOCKUP_CONTENT_TYPE_VIDEO"
        ]
        published_by = Counter(
            track.channel_id for track in tracks if track.channel_id is not None
        )

        return cls(
            playlist_id=header.get("playlistId"),
            title=None if title is None else read_text(title),
            artists=artists,
            release_type=release_type,
            # A release whose tracks went up on more than one channel is put
            # down to whichever published most of it, since the one this asks
            # after is the musician the release is theirs.
            artist_channel_id=next(
                (channel for channel, _ in published_by.most_common(1)),
                None,
            ),
            thumbnails=read_images(
                header.get("playlistHeaderBanner", {}),
                "thumbnails",
            ),
            tracks=tracks,
            continuation=read_continuation(browsed),
            raw=data,
        )

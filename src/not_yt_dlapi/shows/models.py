# TODO: Validate
"""Shows models.

Shaped after what browse answers with rather than after anything the API
documents, because the API documents nothing here: a show is a playlist it will
not hand out. One class per thing browse writes, one field per thing that thing
says, named the way browse names it but in snake_case.

An entry says which video it is, what it is called, how long it is, where it
sits in the season and what it is pictured by. It says nothing about who
published it or when, so there is nothing of that here. The answer itself is
kept on `raw`, so what browse said and this does not read is still there to
read.
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
    read_seasons,
    read_text,
    strip_url_parameters,
)


# TODO: Validate
def read_entries(browsed: dict[str, Any]) -> list[dict[str, Any]]:
    """Return every episode an answer lists, in the order it lists them."""
    return list(find(browsed, "playlistVideoRenderer"))


# TODO: Validate
class ShowThumbnail(APIModel):
    """One of the images an episode is pictured by.

    Attributes:
        url: The image's URL.
        width: The image's width.
        height: The image's height.
    """

    url: str
    width: int
    height: int


# TODO: Validate
class ShowEpisode(APIModel):
    """One episode of a show, as browse lists it.

    Attributes:
        video_id: The ID that YouTube uses to uniquely identify the video.
        title: The episode's title.
        length_seconds: How long the episode runs, in seconds.
        length_text: How long the episode runs, written the way it is shown.
        index: Which episode of its own season it is, counting from one, which
            is the number the site shows beside it. Every season counts from its
            own start, so this repeats between the seasons of one show.
        playlist_id: The playlist the episode was listed under, which is the
            show's own id and the same for every episode of it. An episode that
            has to be bought is not watched from the listing and says no
            playlist, so this is nothing for those.
        is_playable: Whether the episode can be watched. An episode that is
            listed but no longer watchable says so here.
        thumbnails: The images the episode is pictured by, smallest first.
    """

    video_id: str
    title: str
    length_seconds: int | None = None
    length_text: str | None = None
    index: int
    playlist_id: str | None = None
    is_playable: bool
    thumbnails: list[ShowThumbnail] = Field(default_factory=list)

    # TODO: Validate
    @classmethod
    def from_entry(cls, entry: dict[str, Any]) -> Self:
        """Read one entry as browse wrote it."""
        # An episode of a show that is bought rather than watched carries a
        # modal telling the viewer to sign in and buy it, where every other
        # episode carries the endpoint it is watched from.
        watch = entry["navigationEndpoint"].get("watchEndpoint", {})
        length = entry.get("lengthSeconds")
        length_text = entry.get("lengthText")
        return cls(
            video_id=entry["videoId"],
            title=read_text(entry["title"]),
            length_seconds=None if length is None else int(length),
            length_text=None if length_text is None else read_text(length_text),
            index=int(read_text(entry["index"])),
            playlist_id=watch.get("playlistId"),
            is_playable=entry.get("isPlayable", False),
            thumbnails=[
                ShowThumbnail(
                    **thumbnail | {"url": strip_url_parameters(thumbnail["url"])},
                )
                for thumbnail in entry.get("thumbnail", {}).get("thumbnails", ())
            ],
        )


# TODO: Validate
class ShowSeasonLink(APIModel):
    """One season of a show, as the menu of them offers it.

    A season is its own thing to ask browse for, and what it is asked for by is
    written in the menu rather than worked out from the number, so what the menu
    says is kept as it stands and handed back to `list` to ask with.

    Attributes:
        number: Which season it is, counted the way the show counts them, which
            is not always from one.
        browse_id: What browse calls the season, which is the show itself rather
            than the playlist the show was opened by.
        params: What browse is told to narrow the show down to this season,
            which is an opaque string the menu carries.
        selected: Whether this is the season the answer the menu came in holds.
            Opening a show gives whichever season its menu starts on, so this is
            what says which of them was already answered.
    """

    number: int
    browse_id: str
    params: str | None = None
    selected: bool = False


# TODO: Validate
class Show(BaseResponseModel, APIModel):
    """One stretch of one season of a show, and what browse listed in it.

    Browse hands out a season a stretch at a time, and only the stretch that
    begins one carries the menu of seasons, because the ones after it are the
    rest of a season already asked for rather than the show again. So a stretch
    that is not the first says neither which season it is nor what the other
    seasons are, and what it holds is episodes and the token for the one after
    it.

    Attributes:
        season: Which season this stretch is of, if the answer says, which it
            does by marking that season as the one chosen in its menu.
        seasons: The seasons the menu offers, lowest number first, each holding
            what it is asked for by.
        episodes: The episodes this stretch listed, in the order it listed them.
        continuation: What the stretch after this one is asked for by, which is
            nothing once there is no more of the season.
        raw: The answer browse gave, as it was served.
    """

    season: int | None = None
    seasons: list[ShowSeasonLink] = Field(default_factory=list)
    episodes: list[ShowEpisode] = Field(default_factory=list)
    continuation: str | None = None
    raw: str = Field(repr=False, exclude=True)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: str) -> Self:
        """Read one answer browse gave."""
        browsed = json.loads(data)
        menu, open_season = read_seasons(browsed)

        return cls(
            season=open_season,
            seasons=[
                ShowSeasonLink(
                    number=number,
                    browse_id=endpoint["browseId"],
                    params=endpoint.get("params"),
                    selected=number == open_season,
                )
                for number, endpoint in sorted(menu.items())
            ],
            episodes=[ShowEpisode.from_entry(entry) for entry in read_entries(browsed)],
            continuation=read_continuation(browsed),
            raw=data,
        )

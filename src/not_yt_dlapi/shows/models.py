# TODO: Validate
"""Shows models.

Shaped after what browse answers with rather than after anything the API
documents, because the API documents nothing here: a show is a playlist it will
not hand out. One class per thing browse writes, one field per thing that thing
says, named the way browse names it but in snake_case.

An entry says which video it is, what it is called, how long it is, where it
sits in the season and what it is pictured by. It says nothing about who
published it or when, so there is nothing of that here. The entry itself is kept
on `raw`, so what browse said and this does not read is still there to read.
"""

from __future__ import annotations

from typing import Any, Self, override

from pydantic import Field, SkipValidation

from not_yt_dlapi.base_response_model import BaseResponseModel
from not_yt_dlapi.common_models import APIModel
from not_yt_dlapi.utils import find, read_seasons, read_text


# TODO: Validate
def read_open_season(browsed: dict[str, Any]) -> int | None:
    """Return which season an answer holds, if the answer says.

    Every answer carrying a season carries the menu of them too, with the one
    it holds marked as the one chosen. An answer to a continuation carries no
    menu, because it is the rest of a season already named rather than a season
    of its own, and nothing else browse answers with names a season either.
    """
    _, open_season = read_seasons(browsed)
    return open_season


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
            show's own id and the same for every episode of it.
        is_playable: Whether the episode can be watched. An episode that is
            listed but no longer watchable says so here.
        thumbnails: The images the episode is pictured by, smallest first.
    """

    video_id: str
    title: str
    length_seconds: int | None = None
    length_text: str | None = None
    index: int
    playlist_id: str
    is_playable: bool
    thumbnails: list[ShowThumbnail] = Field(default_factory=list)

    # TODO: Validate
    @classmethod
    def from_entry(cls, entry: dict[str, Any]) -> Self:
        """Read one entry as browse wrote it."""
        watch = entry["navigationEndpoint"]["watchEndpoint"]
        length = entry.get("lengthSeconds")
        length_text = entry.get("lengthText")
        return cls(
            video_id=entry["videoId"],
            title=read_text(entry["title"]),
            length_seconds=None if length is None else int(length),
            length_text=None if length_text is None else read_text(length_text),
            index=int(read_text(entry["index"])),
            playlist_id=watch["playlistId"],
            is_playable=entry.get("isPlayable", False),
            thumbnails=[
                ShowThumbnail(**thumbnail)
                for thumbnail in entry.get("thumbnail", {}).get("thumbnails", ())
            ],
        )


# TODO: Validate
class ShowSeason(APIModel):
    """One season of a show, and the episodes browse listed under it.

    Attributes:
        number: Which season it is, counted the way the show counts them, which
            starts at one.
        episodes: The episodes, in the order browse listed them.
    """

    number: int
    episodes: list[ShowEpisode] = Field(default_factory=list)


# TODO: Validate
class Show(BaseResponseModel, APIModel):
    """The seasons of a show that browse listed, and what is in each of them.

    The episodes are kept under the season they belong to rather than run
    together, because that is the only thing that says which season an episode
    is from: an entry says where it sits in its own season and nothing about
    which season that is.

    Attributes:
        seasons: The seasons the answers held, lowest number first.
        raw: The answers browse gave, in the order it gave them.
    """

    seasons: list[ShowSeason] = Field(default_factory=list)
    raw: SkipValidation[list[dict[str, Any]]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: list[dict[str, Any]]) -> Self:
        """Read every answer browse gave, filing each episode under its season.

        An answer says which season it holds, and an answer to a continuation
        says nothing because it is the rest of the season the answer before it
        named. So the answers are read in the order they were given and each
        one that names a season says which season the ones after it belong to
        until another does. A show whose only season is the playlist itself
        names none at all, and its one season is its first.
        """
        episodes: dict[int, list[dict[str, Any]]] = {}
        season = 1
        for answer in data:
            season = read_open_season(answer) or season
            episodes.setdefault(season, []).extend(read_entries(answer))

        return cls(
            seasons=[
                ShowSeason(
                    number=number,
                    episodes=[ShowEpisode.from_entry(entry) for entry in entries],
                )
                for number, entries in sorted(episodes.items())
            ],
            raw=data,
        )

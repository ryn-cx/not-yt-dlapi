# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI

PLAYLIST_ID = "UUEIwxahdLz7bap-VDs9h35A"
"""The uploads playlist of https://www.youtube.com/@SteveMould"""


# TODO: Validate
def test_download(client: NotYTDLAPI) -> None:
    # YouTube is currently refusing every playlist feed it is asked for, so this
    # raises rather than answering until that is fixed.
    feed = client.playlist_feed(PLAYLIST_ID)
    # A playlist feed keeps every character of the id it was asked for.
    assert feed.playlist_id == PLAYLIST_ID

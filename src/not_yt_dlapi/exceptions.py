# TODO: Validate
from __future__ import annotations

from typing import Any

HTTP_NOT_FOUND = 404


class NotYTDLAPIError(Exception):
    def __init__(self, message: str, response: dict[str, Any]) -> None:
        super().__init__(message)
        self.response = response


class VideoNotFoundError(NotYTDLAPIError):
    pass


class ChannelNotFoundError(NotYTDLAPIError):
    pass


class PlaylistNotFoundError(NotYTDLAPIError):
    pass


class PlaylistItemsNotFoundError(NotYTDLAPIError):
    pass

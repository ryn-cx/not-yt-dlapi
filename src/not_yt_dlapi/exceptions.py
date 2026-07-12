# TODO: Validate
"""Exceptions for the not_yt_dlapi library."""

from __future__ import annotations

from typing import Any

HTTP_NOT_FOUND = 404


class NotYTDLAPIError(Exception):
    """Base exception for not_yt_dlapi library."""


class NoContentError(NotYTDLAPIError):
    """Raised when a response has no meaningful content."""

    def __init__(
        self,
        response: dict[str, Any],
        log_id: str,
    ) -> None:
        """Store the downloaded response so it can be recovered by the caller."""
        self.response = response
        super().__init__(f"Response has no content for {log_id}.")


class NotFoundError(NotYTDLAPIError):
    """Base exception for all not-found errors."""


class VideoNotFoundError(NotFoundError):
    """Exception raised when a video is not found."""


class ChannelNotFoundError(NotFoundError):
    """Exception raised when a channel is not found."""


class PlaylistNotFoundError(NotFoundError):
    """Exception raised when a playlist is not found."""


class PlaylistItemsNotFoundError(NotFoundError):
    """Exception raised when playlist items are not found."""

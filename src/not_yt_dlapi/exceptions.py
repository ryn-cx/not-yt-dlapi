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
        *,
        endpoint: str | None = None,
    ) -> None:
        """Store the downloaded response so it can be recovered by the caller.

        Args:
            response: The raw JSON response that was found to be empty.
            endpoint: The endpoint name, included in the error message.
        """
        self.response = response
        location = f" for {endpoint}" if endpoint else ""
        super().__init__(f"Response has no content{location}.")


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

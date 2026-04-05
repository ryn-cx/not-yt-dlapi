"""Exceptions for the not_yt_dlapi library."""

HTTP_NOT_FOUND = 404


class NotYTDLAPIError(Exception):
    """Base exception for not_yt_dlapi library."""


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

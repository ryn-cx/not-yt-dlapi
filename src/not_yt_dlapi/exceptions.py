"""Exceptions for the not_yt_dlapi library."""


class NotYTDLAPIError(Exception):
    """Base exception for not_yt_dlapi library."""


class VideoNotFoundError(NotYTDLAPIError):
    """Exception raised when a video is not found."""


class ChannelNotFoundError(NotYTDLAPIError):
    """Exception raised when a channel is not found."""


class PlaylistNotFoundError(NotYTDLAPIError):
    """Exception raised when a playlist is not found."""


class PlaylistItemsNotFoundError(NotYTDLAPIError):
    """Exception raised when playlist items are not found."""

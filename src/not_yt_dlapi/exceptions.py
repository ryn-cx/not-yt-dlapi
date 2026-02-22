"""Exceptions for the not_yt_dlapi library."""


class NotYTDLAPIError(Exception):
    """Base exception for not_yt_dlapi library."""


class VideoNotFoundError(NotYTDLAPIError):
    """Exception raised when a video is not found."""

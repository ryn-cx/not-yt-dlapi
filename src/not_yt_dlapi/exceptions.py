# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class NotYTDLAPIError(Exception):
    """Base exception for NotYTDLAPI."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(NotYTDLAPIError):
    """Raised when a request is answered with an unexpected status code."""

    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class APIError(HTTPError):
    """Raised when the API answers with an `error` object.

    The whole body is kept as well as the error, so the rest of what the API
    said about the failure is still reachable.
    """

    def __init__(
        self,
        error: dict[str, Any],
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the error object, the status code and the body."""
        self.error = error
        self.code = error["code"]
        super().__init__(status_code, response)


# TODO: Validate
class ResourceNotFoundError(APIError):
    """Raised when the API reports that the requested resource does not exist.

    Asking about something that does not exist is not always an error to this
    API: a video or channel id nothing is under comes back as an empty list of
    items. This is only for the endpoints that refuse the request instead.
    """


# TODO: Validate
class ChannelNotFoundError(ResourceNotFoundError):
    """Raised when the requested channel does not exist."""

    def __init__(
        self,
        channel_id: str,
        error: dict[str, Any],
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the channel id and the originating response."""
        self.channel_id = channel_id
        super().__init__(error, status_code, response)


# TODO: Validate
class PlaylistNotFoundError(ResourceNotFoundError):
    """Raised when the requested playlist does not exist."""

    def __init__(
        self,
        playlist_id: str,
        error: dict[str, Any],
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the playlist id and the originating response."""
        self.playlist_id = playlist_id
        super().__init__(error, status_code, response)


# TODO: Validate
class ChannelFeedNotFoundError(HTTPError):
    """Raised when the feed of the requested channel cannot be read.

    The feeds go down for a while at a time, and a channel that answered an
    hour ago is refused the same way one that does not exist is, so this does
    not say which of the two happened.
    """

    def __init__(
        self,
        channel_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the channel id and the originating response."""
        self.channel_id = channel_id
        super().__init__(status_code, response)


# TODO: Validate
class PlaylistFeedNotFoundError(HTTPError):
    """Raised when the feed of the requested playlist cannot be read.

    YouTube is currently refusing every playlist feed it is asked for, so this
    is what a playlist feed answers with whether or not the playlist exists.
    """

    def __init__(
        self,
        playlist_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the playlist id and the originating response."""
        self.playlist_id = playlist_id
        super().__init__(status_code, response)

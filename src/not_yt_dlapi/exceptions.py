# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import httpx


HTTP_NOT_FOUND = 404


# TODO: Validate
class NotYTDLAPIError(Exception):
    """Base exception for the not-yt-dlapi library.

    Every error carries what caused it in `response`, so a caller that catches
    one can still inspect it instead of only reading the message. What
    `response` holds depends on the error, but it is always the original,
    unmodified value: the whole response for an error raised from one, and the
    data that failed the check for the rest.
    """

    response: Any = None
    """The original data that caused the error, or `None` if there was none."""


# TODO: Validate
class HTTPError(NotYTDLAPIError):
    """Raised when a request is answered with a body that is not JSON.

    An answer the API means as an error is JSON and becomes an `APIError`, so
    what is left for this is an answer that is not the API talking at all: a
    proxy page, an empty body, a gateway timeout.
    """

    response: httpx.Response
    """The response that caused the error, request included."""

    # TODO: Validate
    def __init__(self, response: httpx.Response) -> None:
        """Initialize the HTTPError with the response that caused it.

        The response is kept whole rather than as its parsed body, so what was
        asked for is still reachable through `response.request`.
        """
        self.response = response
        super().__init__(
            f"Unexpected response status code: {response.status_code}\n{response.text}",
        )

    # TODO: Validate
    @property
    def status_code(self) -> int:
        """The status code of the response that caused the error."""
        return self.response.status_code

    # TODO: Validate
    @property
    def body(self) -> str:
        """The raw text of the response that caused the error."""
        return self.response.text


# TODO: Validate
class APIError(NotYTDLAPIError):
    """Raised when the API answers with an `error` object.

    The whole body is kept rather than only the error, because the body is what
    was actually returned and reading it is the only way to see the rest of
    what the API said about the failure.
    """

    # TODO: Validate
    def __init__(self, error: dict[str, Any], response: dict[str, Any]) -> None:
        """Initialize the APIError with the error object and the whole body."""
        self.error = error
        self.code = error["code"]
        self.response = response
        super().__init__(f"{self.code}: {error['message']}")


# TODO: Validate
class NotFoundError(APIError):
    """Raised when the API answers with a 404.

    Asking about something that does not exist is not always an error to this
    API: a video or channel id nothing is under comes back as an empty list of
    items. This is only for the endpoints that refuse the request instead.
    """

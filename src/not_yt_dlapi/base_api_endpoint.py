# TODO: Validate
"""Base API endpoint module."""

from __future__ import annotations

from abc import abstractmethod
from datetime import datetime
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from not_yt_dlapi.constants import FILES_PATH
from not_yt_dlapi.exceptions import NoContentError

if TYPE_CHECKING:
    from pathlib import Path

    from not_yt_dlapi import NotYTDLAPI

logger = getLogger(__name__)
logger.addHandler(NullHandler())


def fetch_all_pages(
    client: NotYTDLAPI,
    url: str,
    params: dict[str, Any],
) -> dict[str, Any]:
    """Fetch all pages from a paginated YouTube API endpoint.

    Args:
        client: The NotYTDLAPI client instance.
        url: The full API URL to request.
        params: Query parameters for the request.

    Returns:
        A combined response dict with all items from every page.
    """
    params.setdefault("maxResults", 50)
    combined: dict[str, Any] | None = None
    all_items: list[dict[str, Any]] = []
    page = 1
    while True:
        logger.info("Downloading page %s: %s", page, params)
        response = client.authenticated_get(url, params=params).json()
        if combined is None:
            combined = response
        all_items.extend(response.get("items", []))
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
        params["pageToken"] = next_page_token
        page += 1

    if combined is None:
        msg = "No pages returned from API"
        raise ValueError(msg)
    combined["items"] = all_items
    return combined


def generate_timestamp() -> str:
    """Generate an ISO 8601 timestamp for metadata."""
    return datetime.now().astimezone().isoformat().replace("+00:00", "Z")


class BaseExtractor[T: GAPIBaseModel](GAPIClient[T]):
    """Base class to extract data from API responses."""

    @override
    @classmethod
    def json_files_folder(cls) -> Path:
        folder_name = cls._folder_name(cls._model_name())
        return FILES_PATH / folder_name.replace("_model", "")


class BaseEndpoint[T: GAPIBaseModel](BaseExtractor[T]):
    """Base class for API endpoints."""

    def __init__(self, client: NotYTDLAPI) -> None:
        """Initialize the endpoint with the NotYTDLAPI client."""
        self._client = client

    @staticmethod
    @abstractmethod
    def has_content(*args: Any, **kwargs: Any) -> bool:  # noqa: ANN401
        """Return whether the response has meaningful content."""

    def _parse_or_raise(self, response: dict[str, Any], log_id: str) -> T:
        """Parse `response`, or raise `NoContentError` when it is empty.

        Raises:
            NoContentError: If `has_content` is false.
        """
        if not self.has_content(response):
            raise NoContentError(response, log_id)
        return self.parse(response)

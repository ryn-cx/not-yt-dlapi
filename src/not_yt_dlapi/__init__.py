# TODO: Validate
"""YouTube Data API.

The client holds one attribute per endpoint and the single download that all of
them go through. An endpoint is reached the way the API reaches it, so
`client.videos.list("jNQXAC9IVRw")` is `videos.list` and is the whole of it: no
download is asked for and then parsed, because the method does both.
"""

from __future__ import annotations

from http import HTTPStatus
from json import JSONDecodeError
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import TYPE_CHECKING, Any, overload

from get_around import GetAround
from google.auth.transport.requests import Request

from not_yt_dlapi.channel_sections import ChannelSections
from not_yt_dlapi.channels import Channels
from not_yt_dlapi.exceptions import HTTP_NOT_FOUND, APIError, HTTPError, NotFoundError
from not_yt_dlapi.playlist_items import PlaylistItems
from not_yt_dlapi.playlists import Playlists
from not_yt_dlapi.videos import Videos

if TYPE_CHECKING:
    from google.oauth2.credentials import Credentials

logger = getLogger(__name__)
logger.addHandler(NullHandler())

BASE_URL = "https://www.googleapis.com/youtube/v3"
"""Where the API lives, which is the same for every endpoint."""

FEED_URL = "https://www.youtube.com/feeds/videos.xml"
"""Where the feeds live, which is not the API and is the same for every feed."""


# TODO: Validate
class NotYTDLAPI:
    """YouTube Data API."""

    # TODO: Validate
    @overload
    def __init__(
        self,
        *,
        api_key: str,
        credentials: Credentials | None = None,
        sleep_time: float = 0,
        get_around_client: GetAround | None = None,
    ) -> None: ...

    # TODO: Validate
    @overload
    def __init__(
        self,
        *,
        api_key: str | None = None,
        credentials: Credentials,
        sleep_time: float = 0,
        get_around_client: GetAround | None = None,
    ) -> None: ...

    # TODO: Validate
    def __init__(
        self,
        *,
        api_key: str | None = None,
        credentials: Credentials | None = None,
        sleep_time: float = 0,
        get_around_client: GetAround | None = None,
    ) -> None:
        """Initialize the client with an API key or OAuth credentials.

        Raises:
            ValueError: If neither an API key nor credentials are given, since
                the API answers nothing without one of them.
        """
        if api_key is None and credentials is None:
            msg = "Either api_key or credentials must be provided."
            raise ValueError(msg)

        self.api_key = api_key
        self.credentials = credentials
        self.sleep_time = sleep_time
        self.get_around_client = get_around_client or GetAround()

        self.videos = Videos(self)
        self.channels = Channels(self)
        self.channel_sections = ChannelSections(self)
        self.playlists = Playlists(self)
        self.playlist_items = PlaylistItems(self)

        super().__init__()

    # TODO: Validate
    def _headers(self) -> dict[str, str]:
        """Return the headers a request goes out with.

        OAuth credentials are refreshed here rather than by the caller, because
        this is the only place that knows a request is about to be made.
        """
        if self.credentials is None:
            return {}
        if not self.credentials.valid:
            self.credentials.refresh(Request())
        return {"Authorization": f"Bearer {self.credentials.token}"}

    # TODO: Validate
    def download(
        self,
        path: str,
        params: dict[str, Any],
        log_id: str,
    ) -> dict[str, Any]:
        """Make a request to the YouTube Data API.

        Raises:
            HTTPError: If the body is not JSON, which is something other than
                the API answering.
            NotFoundError: If the API refuses the request because what was
                asked about does not exist.
            APIError: If the API answers with any other error.
        """
        start = monotonic()

        headers = self._headers()
        query = dict(params)
        if not headers:
            query["key"] = self.api_key

        response = self.get_around_client.get(
            f"{BASE_URL}/{path}",
            params=query,
            headers=headers,
            timeout=30,
        )
        duration = monotonic() - start

        logger.debug("Downloaded: %s - Completed in %.4f seconds", log_id, duration)

        try:
            output: dict[str, Any] = response.json()
        except JSONDecodeError as error:
            raise HTTPError(response) from error

        if error_object := output.get("error"):
            if error_object["code"] == HTTP_NOT_FOUND:
                raise NotFoundError(error_object, output)
            raise APIError(error_object, output)

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response)

        sleep(self.sleep_time)

        return output

    # TODO: Validate
    def download_feed(self, params: dict[str, Any], log_id: str) -> str:
        """Download a feed and return the document as it was served.

        A feed is not the API: it is served from youtube.com rather than from
        the API's host, it costs no quota and it takes no key, so neither the
        key nor the OAuth headers are sent with it.

        What comes back is the XML itself rather than anything made of it, since
        making something of it is the model's to do and what is downloaded is
        what a recording of the download has to be able to be.

        Asking about something that does not exist is refused here rather than
        answered empty, and what comes back is YouTube's own 404 page rather
        than anything machine-readable, so there is nothing to raise a
        `NotFoundError` from and it is an `HTTPError` like any other refusal.

        Raises:
            HTTPError: If the feed is refused.
        """
        start = monotonic()

        response = self.get_around_client.get(
            FEED_URL,
            params=params,
            timeout=30,
        )
        duration = monotonic() - start

        logger.debug("Downloaded: %s - Completed in %.4f seconds", log_id, duration)

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response)

        sleep(self.sleep_time)

        return response.text

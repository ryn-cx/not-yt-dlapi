# TODO: Validate
"""Contains the NotYTDLAPI class."""

from __future__ import annotations

from http import HTTPStatus
from json import JSONDecodeError
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import TYPE_CHECKING, Any, overload

from get_around import GetAround
from google.auth.transport.requests import Request

from not_yt_dlapi.channel_feed import ChannelFeed
from not_yt_dlapi.channel_sections import ChannelSections
from not_yt_dlapi.channels import Channels
from not_yt_dlapi.exceptions import APIError, HTTPError, ResourceNotFoundError
from not_yt_dlapi.music import Music
from not_yt_dlapi.playlist_feed import PlaylistFeed
from not_yt_dlapi.playlist_items import PlaylistItems
from not_yt_dlapi.playlists import Playlists
from not_yt_dlapi.shows import Shows
from not_yt_dlapi.topic import Topic
from not_yt_dlapi.videos import Videos

if TYPE_CHECKING:
    from google.oauth2.credentials import Credentials

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_URL = "https://www.googleapis.com/youtube/v3"
FEED_URL = "https://www.youtube.com/feeds/videos.xml"
BROWSE_URL = "https://www.youtube.com/youtubei/v1/browse"

BROWSE_CLIENT = {"clientName": "WEB", "clientVersion": "2.20240401.00.00"}
"""Which YouTube client browse is asked as, which it wants with every request."""


# TODO: Validate
class NotYTDLAPI:
    """YouTube Data API wrapper."""

    # TODO: Validate
    @overload
    def __init__(
        self,
        *,
        api_key: str,
        credentials: Credentials | None = None,
        sleep_time: float = 1,
        get_around_client: GetAround | None = None,
    ) -> None: ...

    # TODO: Validate
    @overload
    def __init__(
        self,
        *,
        api_key: str | None = None,
        credentials: Credentials,
        sleep_time: float = 1,
        get_around_client: GetAround | None = None,
    ) -> None: ...

    # TODO: Validate
    def __init__(
        self,
        *,
        api_key: str | None = None,
        credentials: Credentials | None = None,
        sleep_time: float = 1,
        get_around_client: GetAround | None = None,
    ) -> None:
        """Initializes the NotYTDLAPI client with an API key or OAuth credentials.

        The client holds one attribute per endpoint, so `client.videos(ids)`
        looks videos up and `client.videos.download(ids)` and
        `client.videos.load(data)` are the halves of it.

        `sleep_time` is how long to wait after asking browse for something.
        Browse answers a run of requests made quickly with a refusal saying the
        network looks automated, so the default is a second rather than nothing.

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
        self.channel_feed = ChannelFeed(self)
        self.channel_sections = ChannelSections(self)
        self.playlists = Playlists(self)
        self.playlist_feed = PlaylistFeed(self)
        self.playlist_items = PlaylistItems(self)
        self.shows = Shows(self)
        self.music = Music(self)
        self.topic = Topic(self)

    # TODO: Validate
    @property
    def _authorization(self) -> dict[str, str]:
        """Return the authorization header, refreshing the credentials first."""
        if self.credentials is None:
            return {}
        if not self.credentials.valid:
            self.credentials.refresh(Request())
        return {"Authorization": f"Bearer {self.credentials.token}"}

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str],
        log_id: str,
    ) -> str:
        """Downloads from the API and returns the body as it was served.

        Raises:
            HTTPError: If the body is not JSON, which is something other than
                the API answering.
            ResourceNotFoundError: If the API refuses the request because what
                was asked about does not exist.
            APIError: If the API answers with any other error.
        """
        authorization = self._authorization
        query = dict(params)
        if not authorization:
            query["key"] = self.api_key

        logger.debug("Downloading: %s", log_id)
        start = monotonic()
        response = self.get_around_client.get(
            f"{API_URL}/{endpoint}",
            params=query,
            headers={**headers, **authorization},
        )
        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)

        try:
            body: dict[str, Any] = response.json()
        except JSONDecodeError as err:
            raise HTTPError(response.status_code, response.text) from err

        if error := body.get("error"):
            if error["code"] == HTTPStatus.NOT_FOUND:
                raise ResourceNotFoundError(error, response.status_code, body)
            raise APIError(error, response.status_code, body)

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        return response.text

    # TODO: Validate
    def download_feed(
        self,
        params: dict[str, Any],
        headers: dict[str, str],
        log_id: str,
    ) -> str:
        """Downloads a feed and returns the XML document as it was served.

        Raises:
            HTTPError: If the feed is refused.
        """
        logger.debug("Downloading: %s", log_id)
        start = monotonic()
        response = self.get_around_client.get(FEED_URL, params=params, headers=headers)
        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        return response.text

    # TODO: Validate
    def browse(self, asked: dict[str, Any], log_id: str) -> str:
        """Asks browse for a page and returns the body as it was served.

        Raises:
            HTTPError: If browse refuses the request.
        """
        logger.debug("Browsing: %s", log_id)
        start = monotonic()
        response = self.get_around_client.post(
            BROWSE_URL,
            json={**asked, "context": {"client": BROWSE_CLIENT}},
            headers={"Content-Type": "application/json"},
        )
        logger.debug("Browsed %s (%.4f s)", log_id, monotonic() - start)

        # The wait comes before the refusal is raised, because a refusal is the
        # answer that most means the next request should not follow at once.
        sleep(self.sleep_time)

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        return response.text

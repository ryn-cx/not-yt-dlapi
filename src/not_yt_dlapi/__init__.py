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
from not_yt_dlapi.music import Music
from not_yt_dlapi.playlist_items import PlaylistItems
from not_yt_dlapi.playlists import Playlists
from not_yt_dlapi.shows import Shows
from not_yt_dlapi.utils import read_continuation, read_seasons
from not_yt_dlapi.videos import Videos

if TYPE_CHECKING:
    from google.oauth2.credentials import Credentials

logger = getLogger(__name__)
logger.addHandler(NullHandler())


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
        """Initialize the client with an API key or OAuth credentials.

        `sleep_time` is how long to wait after asking browse for something, and
        has nothing to say about the API: the API is spent by the unit rather
        than by the second, so waiting between requests costs the same quota
        more slowly. Browse counts requests instead, and answers a run of them
        made quickly with a refusal saying the network looks automated, so the
        default is a second rather than nothing.

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
        self.shows = Shows(self)
        self.music = Music(self)

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
            f"https://www.googleapis.com/youtube/v3/{path}",
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

        return output

    # TODO: Validate
    def download_feed(self, params: dict[str, Any], log_id: str) -> str:
        start = monotonic()

        response = self.get_around_client.get(
            "https://www.youtube.com/feeds/videos.xml",
            params=params,
            timeout=30,
        )
        duration = monotonic() - start

        logger.debug("Downloaded: %s - Completed in %.4f seconds", log_id, duration)

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response)

        return response.text

    # TODO: Validate
    def browse(self, asked: dict[str, Any], log_id: str) -> dict[str, Any]:
        start = monotonic()

        response = self.get_around_client.post(
            "https://www.youtube.com/youtubei/v1/browse",
            json={
                **asked,
                "context": {
                    "client": {
                        "clientName": "WEB",
                        "clientVersion": "2.20240401.00.00",
                    },
                },
            },
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        duration = monotonic() - start

        logger.debug("Downloaded: %s - Completed in %.4f seconds", log_id, duration)

        # The wait comes before the refusal is raised: a refusal is the answer
        # that most means the next request should not follow immediately.
        sleep(self.sleep_time)

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response)

        return response.json()

    # TODO: Validate
    def _browse_to_the_end(
        self,
        browsed: dict[str, Any],
        log_id: str,
    ) -> list[dict[str, Any]]:
        answers = [browsed]
        token = read_continuation(browsed)
        while token is not None:
            answers.append(self.browse({"continuation": token}, log_id))
            token = read_continuation(answers[-1])
        return answers

    # TODO: Validate
    def download_music(
        self,
        playlist_id: str,
        log_id: str,
    ) -> list[dict[str, Any]]:
        """Ask browse for a music playlist and for the rest of it until there is none.

        A release is one playlist with nothing to choose between, unlike a show,
        so what it takes is the playlist itself and then however many
        continuations the listing runs to.
        """
        opened = self.browse({"browseId": f"VL{playlist_id}"}, log_id)
        return self._browse_to_the_end(opened, log_id)

    # TODO: Validate
    def download_show(
        self,
        playlist_id: str,
        log_id: str,
    ) -> list[dict[str, Any]]:
        opened = self.browse({"browseId": f"VL{playlist_id}"}, log_id)
        seasons, open_season = read_seasons(opened)

        asked = [opened] + [
            self.browse(seasons[number], log_id)
            for number in sorted(seasons)
            if number != open_season
        ]
        return [
            answer
            for browsed in asked
            for answer in self._browse_to_the_end(browsed, log_id)
        ]

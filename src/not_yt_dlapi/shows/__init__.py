from __future__ import annotations

from logging import NullHandler, getLogger

from not_yt_dlapi.base_endpoint import BaseEndpoint
from not_yt_dlapi.shows.models import Show

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Shows(BaseEndpoint):
    def list(self, playlist_id: str) -> Show:
        log_id = self.get_log_id(self.list, locals())
        response = self._client.download_show(playlist_id, log_id)
        return Show.from_response(response)

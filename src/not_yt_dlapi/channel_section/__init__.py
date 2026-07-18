from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from not_yt_dlapi.base_api_endpoint import BaseEndpoint
from not_yt_dlapi.channel_section.models import ChannelSectionsModel
from not_yt_dlapi.exceptions import ChannelNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PART = "contentDetails,id,localizations,snippet,targeting"


class ChannelSections(BaseEndpoint[ChannelSectionsModel]):
    _response_model = ChannelSectionsModel

    def get_log_id(self, channel_id: str, part: str = PART) -> str:
        return self.append_non_default_args(
            f"{self.__class__.__name__} {channel_id=}",
            part=(part, PART),
        )

    def download(self, channel_id: str, part: str = PART) -> dict[str, Any]:
        log_id = self.get_log_id(channel_id, part)
        return self._client.download(
            "channelSections",
            params={"part": part, "channelId": channel_id},
            not_found_error=ChannelNotFoundError,
            log_id=log_id,
        )

    def download_and_parse(
        self,
        channel_id: str,
        part: str = PART,
    ) -> ChannelSectionsModel:
        response = self.download(channel_id, part)
        return self.parse(response)

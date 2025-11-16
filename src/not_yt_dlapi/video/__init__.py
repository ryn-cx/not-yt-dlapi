import logging
from typing import Any

from gapi import CustomField, CustomSerializer, GapiCustomizations

from not_yt_dlapi.protocol import YTDLAPIProtocol
from not_yt_dlapi.video.models import Video


class VideoNotFoundError(Exception):
    """Exception raised when a video is not found."""


class VideoMixin(YTDLAPIProtocol):
    youtube: Any
    logger: logging.Logger

    GAPI_CUSTOMIZATIONS = GapiCustomizations(
        custom_fields=[
            CustomField(
                class_name="ContentDetails",
                field_name="dimension",
                new_field="dimension: str",
            ),
        ],
        custom_serializers=[
            CustomSerializer(
                class_name="ContentDetails",
                field_name="duration",
                serializer_code="""if value == timedelta(days=0):
    return "P0D"
return value""",
            ),
        ],
    )

    def download_video(self, video_id: str) -> dict[str, Any]:
        """Download video information from YouTube Data API.

        Args:
            video_id: The YouTube video ID

        Returns:
            Raw API response as a dictionary
        """
        resource = self.youtube.videos()
        method = resource.list
        part = (
            "contentDetails,"
            "id,"
            "liveStreamingDetails,"
            "localizations,"
            "paidProductPlacementDetails,"
            "player,"
            "recordingDetails,"
            "snippet,"
            "statistics,"
            "status,"
            "topicDetails"
        )
        request = method(part=part, id=video_id)

        self.logger.info("Downloading Video: %s ", video_id)

        return request.execute()

    def parse_video(self, data: dict[str, Any], *, update: bool = False) -> Video:
        if update:
            return self._parse_response(Video, data, "video", self.GAPI_CUSTOMIZATIONS)

        return Video.model_validate(data)

    def get_video(self, video_id: str) -> Video:
        """Get video information from YouTube.

        Args:
            video_id: The YouTube video ID

        Returns:
            Parsed Video object
        """
        data = self.download_video(video_id)
        if not data["items"]:
            msg = f"Video with ID '{video_id}' not found."
            raise VideoNotFoundError(msg)

        return self.parse_video(data, update=True)

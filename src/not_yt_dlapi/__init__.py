import json
import logging
import uuid
from typing import Any, override

from gapi import (
    AbstractGapiClient,
    GapiCustomizations,
    apply_customizations,
    update_json_schema_and_pydantic_model,
)
from googleapiclient.discovery import build

from not_yt_dlapi.constants import NOT_YT_DLAPI_PATH

from .constants import FILES_PATH
from .video import VideoMixin

default_logger = logging.getLogger(__name__)


class NotYTDLAPI(AbstractGapiClient, VideoMixin):
    def __init__(
        self,
        api_key: str,
        *,
        logger: logging.Logger = default_logger,
    ) -> None:
        self.api_key = api_key
        self.logger = logger
        self.youtube = build("youtube", "v3", developerKey=api_key)

    @override
    def save_file(self, name: str, data: dict[str, Any], model_type: str) -> None:
        """Add a new test file for a given endpoint."""
        random_file_name = f"{uuid.uuid4()}.json"
        input_path = FILES_PATH / name / random_file_name
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(json.dumps(data, indent=2))

    @override
    def update_model(
        self,
        name: str,
        model_type: str,
        customizations: GapiCustomizations | None = None,
    ) -> None:
        """Update a specific response model based on input data."""
        schema_path = NOT_YT_DLAPI_PATH / f"{name}/schema.json"
        model_path = NOT_YT_DLAPI_PATH / f"{name}/models.py"
        files_path = FILES_PATH / name
        update_json_schema_and_pydantic_model(files_path, schema_path, model_path, name)
        apply_customizations(model_path, customizations)

import json
import logging
from typing import Any

from gapi import GapiCustomizations
from googleapiclient.discovery import build
from pydantic import BaseModel, ValidationError

from .constants import FILES_PATH
from .update_files import save_file, update_model
from .video import VideoMixin

default_logger = logging.getLogger(__name__)


class NotYTDLAPI(VideoMixin):
    def __init__(
        self,
        api_key: str,
        *,
        logger: logging.Logger = default_logger,
    ) -> None:
        self.api_key = api_key
        self.logger = logger
        self.youtube = build("youtube", "v3", developerKey=api_key)

    def _parse_response[T: BaseModel](
        self,
        response_model: type[T],
        data: dict[str, Any],
        name: str,
        customizations: GapiCustomizations | None = None,
    ) -> T:
        try:
            parsed = response_model.model_validate(data)
        except ValidationError as e:
            save_file(name, data)
            update_model(name, customizations)
            msg = "Parsing error, model updated, try again."
            raise ValueError(msg) from e

        if self.dump_response(parsed) != data:
            save_file(name, data)
            temp_path = FILES_PATH / "_temp"
            named_temp_path = temp_path / name
            named_temp_path.mkdir(parents=True, exist_ok=True)
            original_path = named_temp_path / "original.json"
            parsed_path = named_temp_path / "parsed.json"
            original_path.write_text(json.dumps(data, indent=2))
            parsed_path.write_text(json.dumps(self.dump_response(parsed), indent=2))
            msg = "Parsed response does not match original response."
            raise ValueError(msg)

        return parsed

    def dump_response(self, data: BaseModel) -> dict[str, Any]:
        """Dump an API response to a JSON serializable object."""
        return data.model_dump(mode="json", by_alias=True, exclude_unset=True)

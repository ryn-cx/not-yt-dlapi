import json
import uuid
from typing import Any

from gapi import (
    INPUT_TYPE,
    GapiCustomizations,
    apply_customizations,
    update_json_schema_and_pydantic_model,
)

from not_yt_dlapi.constants import FILES_PATH, NOT_YT_DLAPI_PATH


def update_model(
    name: str,
    data: INPUT_TYPE,
    customizations: GapiCustomizations | None = None,
) -> None:
    """Update a specific response model based on input data."""
    schema_path = NOT_YT_DLAPI_PATH / f"{name}/schema.json"
    model_path = NOT_YT_DLAPI_PATH / f"{name}/models.py"
    update_json_schema_and_pydantic_model(data, schema_path, model_path, name)
    apply_customizations(model_path, customizations)


def save_file(name: str, data: dict[str, Any]) -> None:
    """Add a new test file for a given endpoint."""
    random_file_name = f"{uuid.uuid4()}.json"
    input_path = FILES_PATH / name / random_file_name
    input_path.parent.mkdir(parents=True, exist_ok=True)
    input_path.write_text(json.dumps(data, indent=2))

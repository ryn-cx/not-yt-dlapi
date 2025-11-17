from gapi import apply_customizations, update_json_schema_and_pydantic_model

from not_yt_dlapi.constants import FILES_PATH, NOT_YT_DLAPI_PATH
from not_yt_dlapi.video import VideoMixin

if __name__ == "__main__":
    for input_folder in FILES_PATH.iterdir():
        if input_folder.name in {".git", "_temp"} or input_folder.is_file():
            continue

        name = input_folder.name
        schema_path = NOT_YT_DLAPI_PATH / f"{name}/schema.json"
        model_path = NOT_YT_DLAPI_PATH / f"{name}/models.py"

        schema_path.unlink(missing_ok=True)

        json_files = list(input_folder.glob("*.json"))
        update_json_schema_and_pydantic_model(json_files, schema_path, model_path, name)

    apply_customizations(
        NOT_YT_DLAPI_PATH / "video/models.py",
        VideoMixin.GAPI_CUSTOMIZATIONS,
    )

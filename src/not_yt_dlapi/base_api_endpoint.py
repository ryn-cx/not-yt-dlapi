from __future__ import annotations

from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from not_yt_dlapi.constants import FILES_PATH

if TYPE_CHECKING:
    from not_yt_dlapi import NotYTDLAPI


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    JSON_FILES_ROOT = FILES_PATH

    def __init__(self, client: NotYTDLAPI) -> None:
        self._client = client

    def get_single_arg(self, **args: str | None) -> dict[str, Any]:
        params = {key: value for key, value in args.items() if value is not None}
        if len(params) != 1:
            msg = "Invalid number of arguments."
            raise ValueError(msg)
        return params

    @staticmethod
    def append_non_default_args(
        log_id: str,
        **args: tuple[object, object],
    ) -> str:
        for name, (value, default) in args.items():
            if value != default:
                log_id += f" {name}={value!r}"
        return log_id

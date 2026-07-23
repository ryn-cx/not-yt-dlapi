# TODO: Validate
from __future__ import annotations

from inspect import Parameter, signature
from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from not_yt_dlapi.constants import FILES_PATH

if TYPE_CHECKING:
    from collections.abc import Callable

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
    def non_default_args(
        func: Callable[..., Any],
        values: dict[str, Any],
    ) -> dict[str, Any]:
        """Return the args that are changed from their default values."""
        return {
            name: values[name]
            for name, param in signature(func).parameters.items()
            if param.default is not Parameter.empty
            and name in values
            and values[name] != param.default
        }

    def get_log_id(self, func: Callable[..., Any], values: dict[str, Any]) -> str:
        """Gets the log id.

        Example: ClassName (arg1='value1' arg2='value2')
        """
        required = {
            name: values[name]
            for name, param in signature(func).parameters.items()
            if param.default is Parameter.empty and name in values
        }
        set_args = {**required, **self.non_default_args(func, values)}
        parts = [
            *(f"{name}={value!r}" for name, value in set_args.items()),
        ]

        name = self.__class__.__name__
        if not parts:
            return name
        return f"{name} ({' '.join(parts)})"

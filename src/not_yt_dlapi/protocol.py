import logging
from typing import Any, Protocol

from gapi import GapiCustomizations
from pydantic import BaseModel

default_logger = logging.getLogger(__name__)


class YTDLAPIProtocol(Protocol):
    def _api_request(
        self,
        api_key: str,
        *,
        logger: logging.Logger = default_logger,
    ) -> dict[str, Any]: ...

    def _parse_response[T: BaseModel](
        self,
        response_model: type[T],
        data: dict[str, Any],
        name: str,
        customizations: GapiCustomizations | None = None,
    ) -> T: ...

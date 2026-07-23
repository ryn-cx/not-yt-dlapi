# TODO: Validate
import pytest
from get_around import build_client_automatically, get_credential

from not_yt_dlapi import NotYTDLAPI

API_KEY = get_credential("YOUTUBE_API_KEY")


@pytest.fixture(scope="session")
def client() -> NotYTDLAPI:
    return NotYTDLAPI(
        api_key=API_KEY,
        get_around_client=build_client_automatically(),
    )

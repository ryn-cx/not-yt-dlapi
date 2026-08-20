# TODO: Validate
from __future__ import annotations

import pytest
from get_around import build_client_automatically, get_credential

from not_yt_dlapi import NotYTDLAPI

pytest.register_assert_rewrite("tests.utils")


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> NotYTDLAPI:
    # Recording needs a key and a way out; a run that only reads what is
    # already recorded needs neither, so a missing one skips rather than fails.
    try:
        api_key = get_credential("YOUTUBE_API_KEY")
        get_around_client = build_client_automatically()
    except RuntimeError as error:
        pytest.skip(f"No credentials to download with: {error}")
    return NotYTDLAPI(api_key=api_key, get_around_client=get_around_client)

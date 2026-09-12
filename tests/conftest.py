# TODO: Validate
from __future__ import annotations

import pytest
from get_around import build_client_automatically, get_credential

from not_yt_dlapi import NotYTDLAPI


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> NotYTDLAPI:
    # Every test downloads, so a run without a key and a way out skips rather
    # than fails.
    try:
        api_key = get_credential("YOUTUBE_API_KEY")
        get_around_client = build_client_automatically()
    except RuntimeError as error:
        pytest.skip(f"No credentials to download with: {error}")
    return NotYTDLAPI(api_key=api_key, get_around_client=get_around_client)

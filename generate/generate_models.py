from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator.recordings import generate_all

import generate
from not_yt_dlapi import NotYTDLAPI

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_all(
        generate,
        NotYTDLAPI(
            api_key=get_credential("YOUTUBE_API_KEY"),
            get_around_client=build_client_automatically(),
        ),
    )

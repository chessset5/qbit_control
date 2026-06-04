"""
nekobt.to helper

contains api calls to nekobt
"""

import json
from pathlib import Path
from time import sleep
from typing import cast

import requests
from dotenv import dotenv_values

from src import CONFIG_PATH, DATA_FOLDER

NEKOBT_DATA_PATH: Path = DATA_FOLDER / "nekobt data"
NEKOBT_DATA_PATH.mkdir(exist_ok=True)

NEKOBT_CONFIG: dict[str, str | None] = dotenv_values(
    dotenv_path=CONFIG_PATH / ".env.nekobt.to"
)
NEKOBT_KEY: str = cast(str, NEKOBT_CONFIG["api_key"])

NEKOBT_API_URL = "https://nekobt.to/api/v1"

NEKOBT_TRACKER: str = cast(str, NEKOBT_CONFIG["tracker_url"])


def __nekobt_api_call(
    endpoint: str,
    params: dict | None = None,
) -> dict:
    """
    calls the nekobt api with the given values
    """
    if params is None:
        params = dict()

    with requests.Session() as nekobt_session:
        nekobt_session.cookies.update({"ssid": NEKOBT_KEY})
        response: requests.Response = nekobt_session.get(
            url=NEKOBT_API_URL + endpoint, params=params
        )
        content: dict = json.loads(response.content)
    if content["error"] is True:
        if cast(str, content["message"]).startswith(
            "Rate limit exceeded, try again in"
        ):
            sleep(content["retry_after"])
            return __nekobt_api_call(endpoint=endpoint, params=params)
    return content


def get_download_url(nekobt_id: str) -> str:
    """
    From a nekobt_id, get the private tracker download url from
    nekobt.to
    """
    api_endpoint: str = "/torrents/" + nekobt_id
    content: dict = __nekobt_api_call(endpoint=api_endpoint)

    private_magnet: str | None = content["data"]["private_magnet"]
    public_magnet: str | None = content["data"]["magnet"]

    if private_magnet:
        return private_magnet
    if public_magnet:
        return public_magnet
    return ""


def hash_search(hash_v: str) -> str:
    """
    checks nekobt for id value for a given hash
    if hash_v
    """

    api_endpoint: str = "/torrents/search"
    parameters: dict[str, str] = {"query": hash_v}
    content: dict = __nekobt_api_call(endpoint=api_endpoint, params=parameters)
    infohash_match: str | None = content["data"]["infohash_match"]
    if not infohash_match:
        infohash_match = ""

    return infohash_match

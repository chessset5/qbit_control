"""
helper file for qbit functions
"""

from typing import cast

import qbittorrentapi
from dotenv import dotenv_values

from src import CONFIG_PATH

QBIT_CONFIG: dict[str, str | None] = dotenv_values(dotenv_path=CONFIG_PATH / ".env.qbit")

# instantiate a Client using the appropriate WebUI configuration
QBT_CLIENT = qbittorrentapi.Client(
    host=cast(str, QBIT_CONFIG["host"]),
    port=cast(str, QBIT_CONFIG["port"]),
    username=cast(str, QBIT_CONFIG["username"]),
    password=cast(str, QBIT_CONFIG["password"]),
)


def get_torrent_info() -> list[dict]:
    """
    Retrieves the names of all current torrents.

    Returns:
        list[str]: A list containing the name of each torrent managed by the
            QBittorrent client.
    """
    names: list[dict] = []
    with QBT_CLIENT as qc:
        for torrent in qc.torrents.info():
            names.append(torrent)
    return names


def super_seeder(hash_v: list[str], enable: bool = True) -> None:
    """
    sets the super seed value for all the hashes to off or on
    whether enable is False or True
    """
    with QBT_CLIENT as qc:
        for torrent in qc.torrents.info():
            if torrent.hash in hash_v:
                torrent.set_super_seeding(enable=enable)


def get_torrent_names() -> list[str]:
    """
    Retrieves the names of all current torrents.

    Returns:
        list[str]: A list containing the name of each torrent managed by the
            QBittorrent client.
    """
    names: list[str] = []
    with QBT_CLIENT as qc:
        for torrent in qc.torrents.info():
            names.append(torrent.name)
    return names


def get_torrent_name_hashes() -> list[dict[str, str]]:
    """
    Retrieves the names of all current torrents.

    Returns:
        list[str]: A list containing the name of each torrent managed by the
            QBittorrent client.
    """
    names: list[dict[str, str]] = []
    with QBT_CLIENT as qc:
        for torrent in qc.torrents.info():
            names.append({torrent.name: torrent.hash})
    return names


def add_magenet(url: str) -> None:
    """
    Adds a torrent to the client via its magnet link or URL.

    Args:
        url (str): The magnet link or URL of the torrent to be added.
    """
    with QBT_CLIENT as qc:
        qc.torrents_add(urls=url)


def get_trackers(hash_v: str) -> set[str]:
    """
    grabs all the trackers for the given torrent
    """
    trackers: set[str] = set()
    with QBT_CLIENT as qc:
        trackers = {cast(str, tkr["url"]) for tkr in qc.torrents_trackers(torrent_hash=hash_v)}

    return trackers

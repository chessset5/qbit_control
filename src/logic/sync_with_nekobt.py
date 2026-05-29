"""
synchronizes torrents with nekobt

checks nekobt for hash value and grabs the private tracker if available.
"""

from src.helpers.nekobt import NEKOBT_TRACKER, get_download_url, hash_search
from src.helpers.qbit import add_magenet, get_torrent_name_hashes, get_trackers


def neko_sync() -> None:
    """
    runs the hash sync logic
    """

    nhs: list[dict[str, str]] = get_torrent_name_hashes()  # name hash[es]

    for d in nhs:
        for _, hash_v in d.items():
            if hash_v:
                if NEKOBT_TRACKER not in get_trackers(hash_v):
                    nekobt_id: str = hash_search(hash_v=hash_v)
                    if nekobt_id:
                        magnet: str = get_download_url(nekobt_id=nekobt_id)
                        add_magenet(url=magnet)

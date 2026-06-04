"""

turns all hd-torrent files to do not download

"""

from src.helpers.qbit import QBT_CLIENT
from typing import cast


def stop_tracking() -> None:
    """

    makes all files with given tag match priority 0

    """
    with QBT_CLIENT as qc:
        for tag in qc.torrents_tags():
            if "HD" in tag:
                print(tag)
                for torrent in qc.torrents_info(tag=cast(str, tag)):
                    ids: list[int] = [file.id for file in torrent.files]
                    torrent.file_priority(file_ids=ids, priority=0)

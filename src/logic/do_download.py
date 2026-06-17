"""

turns all hd-torrent files to do not download

"""

from src.helpers.qbit import QBT_CLIENT


def start_tracking() -> None:
    """

    makes all files with given tag match priority 0

    """
    with QBT_CLIENT as qc:
        for torrent in qc.torrents_info():
            ids: list[int] = [file.id for file in torrent.files]
            torrent.file_priority(file_ids=ids, priority=1)

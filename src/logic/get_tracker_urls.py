"""
Grab trackers infromation
"""

from pathlib import Path

from src.helpers.qbit import QBT_CLIENT
from src import DATA_FOLDER
import json


def get_trackers() -> None:
    """
    data tracking
    """
    data_file: Path = DATA_FOLDER / "trackers" / "tracker_urls.json"
    data_file.parent.mkdir(exist_ok=True, parents=True)
    trackers: set[str] = set()

    with QBT_CLIENT as qc:
        for torrent in qc.torrents.info():
            trackers |= {i.url for i in torrent.trackers}

    with open(file=data_file, mode="w", encoding="utf-8") as write_file:
        list_data: list[str] = list(trackers)
        list_data.sort(key=lambda x: x[x.find(":") :])
        json.dump(obj=list_data, fp=write_file, indent=4)

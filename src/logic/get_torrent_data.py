"""
grabs the data from the qbit client

"""

import json
from pathlib import Path
from typing import Any

from src import DATA_FOLDER
from src.helpers.qbit import QBT_CLIENT


def get_data() -> None:
    """
    Get user data
    """

    write_path: Path = DATA_FOLDER / "qbit" / "torrents_data.json"
    write_path.parent.mkdir(exist_ok=True, parents=True)
    data: list[dict[str, Any]] = []
    with QBT_CLIENT as qc:
        for torrent in qc.torrents.info():
            add: bool = False
            inner_data: dict = {}
            inner_data["name"] = torrent.name
            inner_data["hash"] = torrent.hash

            files: list[dict[str, Any]] = []
            for file in torrent.files:
                if file.progress > 0 and file.progress < 1:
                    add = True
                files.append(
                    {
                        "availability": file.availability,
                        "name": file.name,
                        "size": file.size,
                        "progress": file.progress,
                        "id": file.id,
                    }
                )
            files.sort(key=lambda x: x["name"])
            inner_data["files"] = files
            if add:
                data.append(inner_data)
    data.sort(key=lambda x: x["name"])
    with open(file=write_path, mode="w", encoding="utf-8") as f:
        json.dump(obj=data, fp=f, indent=4)

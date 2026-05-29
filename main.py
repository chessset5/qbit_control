"""

The purpose of this program is to grab the original trackers for each of the
torrents downloaded.

"""

import sys
from pathlib import Path

PROJECT_PATH: Path = Path(__file__).parent
STR_PP = str(PROJECT_PATH)  # String Project Path
if STR_PP not in sys.path:
    sys.path.insert(0, STR_PP)

from src import runner


def main() -> None:
    """runner"""
    print(f"Hello from {PROJECT_PATH.name}!")
    runner.run()
    print("Good Bye!")


if __name__ == "__main__":
    main()

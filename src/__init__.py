import sys
from pathlib import Path

PROJECT_PATH: Path = Path(__file__).parent.parent
STR_PP = str(PROJECT_PATH)  # String Project Path
if STR_PP not in sys.path:
    sys.path.insert(0, STR_PP)

DATA_PATH: Path = PROJECT_PATH / "data"
DATA_PATH.mkdir(exist_ok=True)
CONFIG_PATH: Path = PROJECT_PATH / "config"
CONFIG_PATH.mkdir(exist_ok=True)

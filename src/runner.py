"""
This file runs the main part of the program.
"""

# from src.logic.sync_with_nekobt import neko_sync as logic
# from src.logic.do_not_download import stop_tracking as logic
# from src.logic.get_tracker_data import get_data as logic
from src.logic.do_download import start_tracking as logic


def run() -> None:
    """
    runs the main logic of the program
    """
    logic()

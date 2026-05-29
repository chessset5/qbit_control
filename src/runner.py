"""
This file runs the main part of the program.
"""

from src.logic.sync_with_nekobt import neko_sync


def run() -> None:
    """
    runs the main logic of the program
    """
    neko_sync()

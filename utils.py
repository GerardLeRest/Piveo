# utils.py
import sys
import os
from pathlib import Path


def get_repertoire_racine() -> Path:
    """
    Retourne le répertoire racine de l'application
    (Python normal, PyInstaller, AppImage)
    """

    # PyInstaller
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    # AppImage
    if "APPDIR" in os.environ:
        return Path(os.environ["APPDIR"])

    # Python normal
    return Path(__file__).resolve().parent
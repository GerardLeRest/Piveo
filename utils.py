#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
Récupère le fichier dans le tmp PyInstaller ou à côté du script
"""
# utils.py
import sys
from pathlib import Path

def resource_path(relative_path: str) -> Path:
    """Récupère le fichier dans le tmp PyInstaller ou à côté du script"""
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).resolve().parent / relative_path

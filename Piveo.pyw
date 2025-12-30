#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, json, locale, gettext
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOCALE_DIR = (BASE_DIR / "locales").resolve()

with open(BASE_DIR / "fichiers" / "configurationLangue.json", "r", encoding="utf-8") as f:
    langue = json.load(f).get("langueSelectionnee", "fr")

locale.setlocale(locale.LC_ALL, "")
gettext.translation(
    "messages",
    localedir=LOCALE_DIR,
    languages=[langue],
    fallback=False,
).install()

# _("Menu")  # TEST

# ⬇️ IMPORTS UI APRÈS gettext
from PySide6.QtWidgets import QApplication
from ChoixOrganisme import ChoixOrganisme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ChoixOrganisme()
    fenetre.show()
    sys.exit(app.exec())

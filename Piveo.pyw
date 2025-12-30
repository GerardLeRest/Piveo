#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Point d'entrée du programme Piveo
"""

import sys
import os
import locale
import gettext

# ------------------------------------------------------------
# Initialisation gettext (Piveo) - 1suel fois dans les classes
# ------------------------------------------------------------
locale.setlocale(locale.LC_ALL, "")

localedir = os.path.join(os.path.dirname(__file__), "locale")

gettext.bindtextdomain("piveo", localedir)
gettext.textdomain("piveo")
_ = gettext.gettext

# -----------------------------
# Qt
# -----------------------------
from PySide6.QtWidgets import QApplication
from ChoixOrganisme import ChoixOrganisme


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ChoixOrganisme()
    fenetre.show()
    sys.exit(app.exec())

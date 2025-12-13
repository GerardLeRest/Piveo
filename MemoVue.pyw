#!/usr/bin/python2
# -*- coding: utf-8 -*

"""     
    Point d'entrée du programme
"""
import sys

from PySide6.QtWidgets import QApplication
from ChoixOrganisme import ChoixOrganisme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ChoixOrganisme()
    fenetre.show()
    sys.exit(app.exec())

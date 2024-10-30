#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
try:
    from PyQt5.QtWidgets import QDialog
    from PyQt5.uic import loadUi
except ImportError as err:
    raise SystemExit("pip3 install PyQt5\n %s" % err)

class NewQDialog(QDialog):
    def __init__(self, parent=None):
        super(NewQDialog, self).__init__(parent)
        if getattr(sys, 'frozen', False):
            # we are running in a |PyInstaller| bundle
            self._basedir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            self._basedir = os.path.dirname(__file__)
        loadUi(os.path.join(self._basedir, 'NewQDialog.ui'), self)

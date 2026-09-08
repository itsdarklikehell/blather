# This is part of Blather
# -- this code is licensed GPLv3
# Copyright 2013 Jezra (original)
# Ported to Python 3 / PySide6

import sys
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout,
    QLabel, QPushButton, QCheckBox
)


class UI(QMainWindow):
    command = Signal(str)

    def __init__(self, opts, continuous):
        super().__init__()
        self.continuous = continuous
        self.setWindowTitle("BlatherQt")
        self.setMaximumSize(400, 200)

        center = QWidget()
        self.setCentralWidget(center)
        layout = QVBoxLayout(center)

        self.status_label = QLabel("Idle")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.listen_btn = QPushButton("Listen")
        self.listen_btn.clicked.connect(lambda: self.command.emit("listen"))
        layout.addWidget(self.listen_btn)

        self.continuous_cb = QCheckBox("Continuous")
        self.continuous_cb.setChecked(continuous)
        self.continuous_cb.toggled.connect(self._on_continuous_toggled)
        layout.addWidget(self.continuous_cb)

        self.quit_btn = QPushButton("Quit")
        self.quit_btn.clicked.connect(lambda: self.command.emit("quit"))
        layout.addWidget(self.quit_btn)

    def run(self):
        pass  # QApplication.exec() handles the loop

    def finished(self, text):
        self.status_label.setText(text)

    def _on_continuous_toggled(self, checked):
        if checked:
            self.command.emit("continuous_listen")
        else:
            self.command.emit("continuous_stop")

    def set_icon_active_asset(self, icon_path):
        self.setWindowIcon(QIcon(icon_path))

    def set_icon_inactive_asset(self, icon_path):
        pass

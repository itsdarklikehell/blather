# This is part of Blather
# -- this code is licensed GPLv3
# Copyright 2013 Jezra (original)
# Ported to Python 3 / GTK 3

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class UI(GObject.GObject):
    __gsignals__ = {
        'command': (GObject.SignalFlags.RUN_LAST, None, (str,))
    }

    def __init__(self, opts, continuous):
        GObject.GObject.__init__(self)
        self.continuous = continuous
        self.window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        self.window.connect("destroy", self._on_destroy)
        self.window.set_title("BlatherGtk")
        self.window.set_resizable(False)

        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.window.add(layout)

        self.lsbutton = Gtk.Button(label="Listen")
        self.lsbutton.connect("clicked", self._on_listen_clicked)
        layout.add(self.lsbutton)

        self.csbutton = Gtk.CheckButton(label="Continuous")
        self.csbutton.set_active(continuous)
        self.csbutton.connect("toggled", self._on_continuous_toggled)
        layout.add(self.csbutton)

        self.quitbutton = Gtk.Button(label="Quit")
        self.quitbutton.connect("clicked", self._on_quit_clicked)
        layout.add(self.quitbutton)

        self.window.show_all()

    def run(self):
        Gtk.main()

    def finished(self, text):
        pass

    def _on_listen_clicked(self, widget):
        self.emit("command", "listen")

    def _on_continuous_toggled(self, widget):
        if widget.get_active():
            self.emit("command", "continuous_listen")
        else:
            self.emit("command", "continuous_stop")

    def _on_quit_clicked(self, widget):
        self.emit("command", "quit")

    def _on_destroy(self, widget):
        Gtk.main_quit()

    def set_icon_active_asset(self, icon_path):
        pass

    def set_icon_inactive_asset(self, icon_path):
        pass

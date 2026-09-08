# This is part of Blather
# -- this code is licensed GPLv3
# Copyright 2013 Jezra (original)
# Ported to Python 3 / GTK 3

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GdkPixbuf


class UI(GObject.GObject):
    __gsignals__ = {
        'command': (GObject.SignalFlags.RUN_LAST, None, (str,))
    }

    def __init__(self, opts, continuous):
        GObject.GObject.__init__(self)
        self.continuous = continuous

        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_title("Blather")
        self.statusicon.set_tooltip_text("Blather - Idle")
        self.statusicon.set_has_tooltip(True)
        self.statusicon.connect("activate", self._on_continuous_toggle)
        self.statusicon.connect("popup-menu", self._on_popup_menu)

        self.menu = Gtk.Menu()
        self.menu_listen = Gtk.MenuItem(label='Listen')
        self.menu_continuous = Gtk.CheckMenuItem(label='Continuous')
        self.menu_quit = Gtk.MenuItem(label='Quit')
        self.menu.append(self.menu_listen)
        self.menu.append(self.menu_continuous)
        self.menu.append(self.menu_quit)
        self.menu_listen.connect("activate", lambda w: self.emit("command", "listen"))
        self.menu_continuous.connect("activate", self._on_continuous_toggle)
        self.menu_quit.connect("activate", lambda w: self.emit("command", "quit"))

    def run(self):
        Gtk.main()

    def finished(self, text):
        pass

    def _on_continuous_toggle(self, widget):
        if self.menu_continuous.get_active():
            self.emit("command", "continuous_stop")
            self.menu_continuous.set_active(False)
        else:
            self.emit("command", "continuous_listen")
            self.menu_continuous.set_active(True)

    def _on_popup_menu(self, icon, button, time):
        self.menu.show_all()
        self.menu.popup(None, None, Gtk.StatusIcon.position_menu, icon, button, time)

    def set_icon_active_asset(self, icon_path):
        self.statusicon.set_from_file(icon_path)

    def set_icon_inactive_asset(self, icon_path):
        pass

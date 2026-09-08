#!/usr/bin/env python3
# -- this code is licensed GPLv3
# Copyright 2013 Jezra (original Python 2 version)
# Ported to Python 3 / GStreamer 1.0

import sys
import signal
import os.path
import subprocess
import argparse

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

try:
    import yaml
except ImportError:
    print("YAML is not supported. ~/blather/config/options.yaml will not function")

# where are the files?
conf_dir = os.path.expanduser("~/.config/blather/")
lang_dir = os.path.join(conf_dir, "language")
command_file = os.path.join(conf_dir, "commands.conf")
strings_file = os.path.join(conf_dir, "sentences.corpus")
history_file = os.path.join(conf_dir, "blather.history")
opt_file = os.path.join(conf_dir, "options.yaml")
lang_file = os.path.join(lang_dir, 'lm')
dic_file = os.path.join(lang_dir, 'dic')

# make the lang dir if it doesn't exist
os.makedirs(lang_dir, exist_ok=True)


class Blather:
    def __init__(self, opts):
        self.ui = None
        self.options = {}
        self.continuous_listen = False
        self.commands = {}

        # read the commands
        self.read_commands()

        # load the options file
        self.load_options()

        # merge the opts
        for k, v in vars(opts).items():
            if k not in self.options or opts.override:
                self.options[k] = v

        if self.options.get('interface') is not None:
            iface = self.options['interface']
            if iface == 'q':
                from QtUI import UI
            elif iface in ('g', 'gt'):
                from GtkUI import UI
            else:
                print("no GUI defined")
                sys.exit(1)

            self.ui = UI(opts, self.options.get('continuous', False))
            self.ui.command.connect(self.process_command)
            # load icons
            icon = self.load_resource("icon.png")
            if icon:
                self.ui.set_icon_active_asset(icon)
            icon_inactive = self.load_resource("icon_inactive.png")
            if icon_inactive:
                self.ui.set_icon_inactive_asset(icon_inactive)

        if self.options.get('history'):
            self.history = []

        # create the recognizer
        try:
            from Recognizer import Recognizer
            self.recognizer = Recognizer(lang_file, dic_file, self.options.get('microphone'))
            self.recognizer.connect('finished', self.recognizer_finished)
        except Exception as e:
            print(f"ERROR: Could not start recognizer: {e}")
            sys.exit(1)

        print("Using Options:", self.options)

    def read_commands(self):
        try:
            with open(command_file) as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"WARNING: command file not found: {command_file}")
            return
        with open(strings_file, "w") as strings:
            for line in lines:
                line = line.strip()
                if len(line) and line[0] != "#":
                    key, value = line.split(":", 1)
                    key = key.strip().lower()
                    value = value.strip()
                    self.commands[key] = value
                    strings.write(key + "\n")

    def load_options(self):
        if 'yaml' not in sys.modules:
            return
        try:
            with open(opt_file) as f:
                text = f.read()
                self.options = yaml.safe_load(text) or {}
        except (FileNotFoundError, yaml.YAMLError):
            pass

    def log_history(self, text):
        if self.options.get('history'):
            self.history.append(text)
            if len(self.history) > self.options['history']:
                self.history.pop(0)
            with open(history_file, "w") as hfile:
                for line in self.history:
                    hfile.write(line + "\n")

    def run_command(self, cmd):
        subprocess.run(cmd, shell=True, check=False)

    def recognizer_finished(self, text):
        t = text.lower()
        if t in self.commands:
            if self.options.get('valid_sentence_command'):
                subprocess.run(self.options['valid_sentence_command'], shell=True, check=False)
            cmd = self.commands[t]
            if self.options.get('pass_words'):
                cmd += " " + t
            self.run_command(cmd)
            self.log_history(text)
        else:
            if self.options.get('invalid_sentence_command'):
                subprocess.run(self.options['invalid_sentence_command'], shell=True, check=False)
            print(f"no matching command {t}")

        if self.ui:
            if not self.continuous_listen:
                self.recognizer.pause()
            self.ui.finished(t)

    def run(self):
        if self.ui:
            self.ui.run()
        else:
            self.recognizer.listen()
            self.main_loop = GLib.MainLoop()
            try:
                self.main_loop.run()
            except KeyboardInterrupt:
                pass

    def process_command(self, command):
        if command == "listen":
            self.recognizer.listen()
        elif command == "stop":
            self.recognizer.pause()
        elif command == "continuous_listen":
            self.continuous_listen = True
            self.recognizer.listen()
        elif command == "continuous_stop":
            self.continuous_listen = False
            self.recognizer.pause()
        elif command == "quit":
            sys.exit(0)

    def load_resource(self, name):
        local_data = os.path.join(os.path.dirname(__file__), 'data')
        paths = ["/usr/share/blather/", "/usr/local/share/blather", local_data]
        for path in paths:
            resource = os.path.join(path, name)
            if os.path.exists(resource):
                return resource
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blather - speech recognizer")
    parser.add_argument("-i", "--interface", type=str, dest="interface",
                        help="Interface to use (if any). 'q' for Qt, 'g' for GTK")
    parser.add_argument("-c", "--continuous", action="store_true", dest="continuous",
                        help="starts interface with 'continuous' listen enabled")
    parser.add_argument("-p", "--pass-words", action="store_true", dest="pass_words",
                        help="passes the recognized words as arguments to the shell command")
    parser.add_argument("-o", "--override", action="store_true", dest="override",
                        help="override config file with command line options")
    parser.add_argument("-H", "--history", type=int, dest="history",
                        help="number of commands to store in history file")
    parser.add_argument("-m", "--microphone", type=int, dest="microphone", default=None,
                        help="Audio input card to use (if other than system default)")
    parser.add_argument("--valid-sentence-command", type=str, dest="valid_sentence_command",
                        help="command to run when a valid sentence is detected")
    parser.add_argument("--invalid-sentence-command", type=str, dest="invalid_sentence_command",
                        help="command to run when an invalid sentence is detected")

    options = parser.parse_args()

    blather = Blather(options)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    blather.run()

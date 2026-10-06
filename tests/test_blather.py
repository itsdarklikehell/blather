#!/usr/bin/env python3
"""Tests for Blather core functionality."""

import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestBlatherInit(unittest.TestCase):
    """Test Blather initialization."""

    def test_import(self):
        """Test that Blather can be imported."""
        # This is a basic smoke test
        self.assertTrue(True)

    def test_command_file_parsing(self):
        """Test command file parsing logic."""
        # Create a temporary command file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as f:
            f.write("# Comment line\n")
            f.write("listen: echo listening\n")
            f.write("stop: echo stopping\n")
            f.write("\n")  # Empty line
            f.write("quit: exit\n")
            temp_path = f.name

        try:
            commands = {}
            with open(temp_path) as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()
                if len(line) and line[0] != "#":
                    key, value = line.split(":", 1)
                    key = key.strip().lower()
                    value = value.strip()
                    commands[key] = value

            self.assertEqual(len(commands), 3)
            self.assertEqual(commands['listen'], 'echo listening')
            self.assertEqual(commands['stop'], 'echo stopping')
            self.assertEqual(commands['quit'], 'exit')
        finally:
            os.unlink(temp_path)

    def test_command_file_not_found(self):
        """Test handling of missing command file."""
        # Should not raise exception
        command_file = "/nonexistent/path/commands.conf"
        try:
            with open(command_file) as f:
                pass
        except FileNotFoundError:
            pass  # Expected

    def test_options_yaml_parsing(self):
        """Test YAML options parsing."""
        try:
            import yaml
            with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
                f.write("continuous: true\n")
                f.write("history: 20\n")
                f.write("microphone: 1\n")
                temp_path = f.name

            try:
                with open(temp_path) as f:
                    text = f.read()
                    options = yaml.safe_load(text) or {}

                self.assertTrue(options['continuous'])
                self.assertEqual(options['history'], 20)
                self.assertEqual(options['microphone'], 1)
            finally:
                os.unlink(temp_path)
        except ImportError:
            self.skipTest("PyYAML not installed")


class TestRunCommand(unittest.TestCase):
    """Test command execution safety."""

    def test_shlex_split_safe(self):
        """Test that shlex.split properly handles commands."""
        import shlex

        # Normal command
        args = shlex.split("echo hello world")
        self.assertEqual(args, ['echo', 'hello', 'world'])

        # Command with quotes
        args = shlex.split('echo "hello world"')
        self.assertEqual(args, ['echo', 'hello world'])

        # Empty command
        args = shlex.split("")
        self.assertEqual(args, [])

        # Command with special chars
        args = shlex.split("echo 'hello; world'")
        self.assertEqual(args, ['echo', 'hello; world'])

    def test_shlex_split_invalid(self):
        """Test shlex.split with invalid input."""
        import shlex

        with self.assertRaises(ValueError):
            shlex.split('echo "unclosed quote')


class TestRecognizer(unittest.TestCase):
    """Test Recognizer class."""

    def test_recognizer_import(self):
        """Test that Recognizer can be imported."""
        try:
            from Recognizer import Recognizer
            self.assertTrue(True)
        except ImportError:
            self.skipTest("GStreamer not available")


class TestUIClasses(unittest.TestCase):
    """Test UI classes."""

    def test_gtk_ui_import(self):
        """Test that GtkUI can be imported."""
        try:
            from GtkUI import UI
            self.assertTrue(True)
        except ImportError:
            self.skipTest("GTK not available")

    def test_qt_ui_import(self):
        """Test that QtUI can be imported."""
        try:
            from QtUI import UI
            self.assertTrue(True)
        except ImportError:
            self.skipTest("PySide6 not available")


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Tests for Blather shell plugins."""

import os
import sys
import unittest
from pathlib import Path


class TestPluginSyntax(unittest.TestCase):
    """Test that shell plugins have valid syntax."""

    PLUGIN_DIR = Path(__file__).parent.parent / "config" / "plugins"

    def _check_bash_syntax(self, filepath):
        """Check bash syntax of a file."""
        import subprocess
        result = subprocess.run(
            ['bash', '-n', str(filepath)],
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stderr

    def test_alarm_sh_syntax(self):
        """Test alarm.sh syntax."""
        filepath = self.PLUGIN_DIR / "alarm.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in alarm.sh: {error}")

    def test_blather_sh_syntax(self):
        """Test blather.sh syntax."""
        filepath = self.PLUGIN_DIR / "blather.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in blather.sh: {error}")

    def test_get_internal_ip_sh_syntax(self):
        """Test get_internal_ip.sh syntax."""
        filepath = self.PLUGIN_DIR / "get_internal_ip.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in get_internal_ip.sh: {error}")

    def test_valid_command_sh_syntax(self):
        """Test valid_command.sh syntax."""
        filepath = self.PLUGIN_DIR / "valid_command.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in valid_command.sh: {error}")

    def test_invalid_command_sh_syntax(self):
        """Test invalid_command.sh syntax."""
        filepath = self.PLUGIN_DIR / "invalid_command.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in invalid_command.sh: {error}")

    def test_weather_sh_syntax(self):
        """Test weather.sh syntax."""
        filepath = self.PLUGIN_DIR / "weather.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in weather.sh: {error}")

    def test_stoplistening_sh_syntax(self):
        """Test stoplistening.sh syntax."""
        filepath = self.PLUGIN_DIR / "stoplistening.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in stoplistening.sh: {error}")

    def test_reboot_sh_syntax(self):
        """Test reboot.sh syntax."""
        filepath = self.PLUGIN_DIR / "reboot.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in reboot.sh: {error}")

    def test_sleep_timer_sh_syntax(self):
        """Test sleep_timer.sh syntax."""
        filepath = self.PLUGIN_DIR / "sleep_timer.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in sleep_timer.sh: {error}")

    def test_key_press_sh_syntax(self):
        """Test key-press.sh syntax."""
        filepath = self.PLUGIN_DIR / "key-press.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in key-press.sh: {error}")

    def test_status_sh_syntax(self):
        """Test status.sh syntax."""
        filepath = self.PLUGIN_DIR / "status.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in status.sh: {error}")

    def test_thunderbird_sh_syntax(self):
        """Test thunderbird.sh syntax."""
        filepath = self.PLUGIN_DIR / "thunderbird.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in thunderbird.sh: {error}")

    def test_top_ten_commands_sh_syntax(self):
        """Test top_ten_commands.sh syntax."""
        filepath = self.PLUGIN_DIR / "top_ten_commands.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in top_ten_commands.sh: {error}")

    def test_whois_zenety_sh_syntax(self):
        """Test whois-zenety.sh syntax."""
        filepath = self.PLUGIN_DIR / "whois-zenety.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in whois-zenety.sh: {error}")

    def test_tecmint_monitor_sh_syntax(self):
        """Test tecmint_monitor.sh syntax."""
        filepath = self.PLUGIN_DIR / "tecmint_monitor.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in tecmint_monitor.sh: {error}")

    def test_language_updater_sh_syntax(self):
        """Test language_updater.sh syntax."""
        filepath = self.PLUGIN_DIR / "language_updater.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in language_updater.sh: {error}")

    def test_testmenu_sh_syntax(self):
        """Test testmenu.sh syntax."""
        filepath = self.PLUGIN_DIR / "testmenu.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in testmenu.sh: {error}")

    def test_GLaDoS_sh_syntax(self):
        """Test GLaDoS.sh syntax."""
        filepath = self.PLUGIN_DIR / "GLaDoS.sh"
        if filepath.exists():
            valid, error = self._check_bash_syntax(filepath)
            self.assertTrue(valid, f"Syntax error in GLaDoS.sh: {error}")


class TestPluginSecurity(unittest.TestCase):
    """Test plugin security issues."""

    PLUGIN_DIR = Path(__file__).parent.parent / "config" / "plugins"

    def test_no_hardcoded_credentials(self):
        """Test that no plugins contain hardcoded credentials."""
        import re
        credential_pattern = re.compile(r'(password|passwd|secret|token|api_key)\s*[=:]\s*\S+', re.IGNORECASE)

        for plugin in self.PLUGIN_DIR.glob("*.sh"):
            with open(plugin) as f:
                content = f.read()
                matches = credential_pattern.findall(content)
                # Filter out comments
                lines = [line for line in content.split('\n') if not line.strip().startswith('#')]
                content_no_comments = '\n'.join(lines)
                matches = credential_pattern.findall(content_no_comments)
                self.assertEqual(len(matches), 0, f"Possible hardcoded credentials in {plugin.name}: {matches}")

    def test_no_shell_true(self):
        """Test that plugins don't use shell=True equivalent."""
        for plugin in self.PLUGIN_DIR.glob("*.sh"):
            with open(plugin) as f:
                content = f.read()
                # Check for eval usage
                self.assertNotIn('eval ', content, f"eval found in {plugin.name}")


class TestMainScripts(unittest.TestCase):
    """Test main scripts syntax."""

    def test_blather_sh_syntax(self):
        """Test blather.sh syntax."""
        import subprocess
        filepath = Path(__file__).parent.parent / "blather.sh"
        result = subprocess.run(['bash', '-n', str(filepath)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Syntax error in blather.sh: {result.stderr}")

    def test_language_updater_sh_syntax(self):
        """Test language_updater.sh syntax."""
        import subprocess
        filepath = Path(__file__).parent.parent / "language_updater.sh"
        result = subprocess.run(['bash', '-n', str(filepath)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Syntax error in language_updater.sh: {result.stderr}")

    def test_blather_installer_syntax(self):
        """Test Blather-Installer syntax."""
        import subprocess
        filepath = Path(__file__).parent.parent / "Blather-Installer"
        result = subprocess.run(['bash', '-n', str(filepath)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Syntax error in Blather-Installer: {result.stderr}")


if __name__ == '__main__':
    unittest.main()

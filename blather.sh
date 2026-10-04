#!/bin/bash
# Blather launcher — start Blather met de juiste omgeving.
# Detecteert automatisch de installatiepad (repo, ~/blather, of /usr/local).

set -euo pipefail

# Bepaal het blather-directory: huidige map, ~/blather, of /usr/local
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SCRIPT_DIR/Blather.py" ]; then
    BLATHER_DIR="$SCRIPT_DIR"
elif [ -f "$HOME/blather/Blather.py" ]; then
    BLATHER_DIR="$HOME/blather"
elif [ -f "/usr/local/blather/Blather.py" ]; then
    BLATHER_DIR="/usr/local/blather"
else
    echo "ERROR: Blather.py not found in $SCRIPT_DIR, ~/blather, or /usr/local/blather" >&2
    exit 1
fi

# GStreamer 1.x paden (0.10 is verouderd)
export GST_PLUGIN_PATH="${GST_PLUGIN_PATH:-/usr/lib/gstreamer-1.0}"

# Standaard TTS stem (overschrijfbaar via VOICE env var)
export VOICE="${VOICE:-/usr/bin/flite}"

# Config- en pluginpaden
export PLUGINS="${PLUGINS:-$BLATHER_DIR/config/plugins}"
export CONFIGDIR="${CONFIGDIR:-$BLATHER_DIR/config}"
export CLIP="${CLIP:-$HOME/.local/share/clipit/history}"

# X11/Xdotool shortcuts
export KEYPRESS="${KEYPRESS:-xdotool key}"
export KEYHOLD="${KEYHOLD:-xdotool keydown}"
export KEYTYPE="${KEYTYPE:-xdotool type}"
export MMOVE="${MMOVE:-xdotool mousemove}"
export CLICK="${CLICK:-xdotool click}"

# Applicaties
export BROWSER="${BROWSER:-firefox}"
export CHBROWSER="${CHBROWSER:-google-chrome}"
export CRMBROWSER="${CRMBROWSER:-chromium-browser}"
export EDITOR="${EDITOR:-geany}"
export FM="${FM:-pcmanfm}"

echo "Starting Blather from $BLATHER_DIR..."
exec python3 "$BLATHER_DIR/Blather.py" "$@"

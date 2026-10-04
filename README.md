# blather


## Development Visualization

<video src="https://raw.githubusercontent.com/itsdarklikehell/blather/master/gource.mp4" controls width="100%"></video>

*Gource visualization showing the repository's commit history. See the [Gource workflow](.github/workflows/gource.yml) for details.*


<img src="https://img.shields.io/github/stars/itsdarklikehell/blather?style=flat-square&color=blue" alt="Stars">
<img src="https://img.shields.io/github/forks/itsdarklikehell/blather?style=flat-square&color=green" alt="Forks">
<img src="https://img.shields.io/github/license/itsdarklikehell/blather?style=flat-square" alt="License">
<img src="https://img.shields.io/github/actions/workflow/status/itsdarklikehell/blather/ci.yml?branch=main&label=CI&style=flat-square" alt="CI Status">

Blather is a speech recognizer that will run commands when a user speaks preset sentences. It uses PocketSphinx for speech recognition and GStreamer 1.0 for audio processing.

## Installatie

### Vereisten

1. Python 3.6+
2. GStreamer 1.0 + plugins (base, good, bad, ugly)
3. PocketSphinx (Python bindings via `pocketsphinx` pip package)
4. PyYAML (for config file parsing)
5. GTK 3 or PySide6 (for GUI, optional)

### Installatie

```bash
# Debian/Ubuntu
sudo apt-get install pocketsphinx python3-yaml python3-gi python3-gi-cairo \
  gir1.2-gtk-3.0 xdotool wmctrl xclip espeak

git clone https://github.com/itsdarklikehell/blather.git
cd blather

# Installeer dependencies (Debian/Ubuntu)
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gstreamer-1.0 \
    gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
    gstreamer1.0-tools python3-yaml pocketsphinx

# Optioneel: GTK 3 of PySide6 voor GUI
sudo apt-get install python3-gi-cairo gir1.2-gtk-3.0  # GTK 3
# of
pip3 install PySide6  # Qt

# Start Blather
python3 Blather.py
```

### Configuratie

Blather leest configuratie uit `~/.config/blather/`:

- `options.yaml` — Algemene opties (continuous mode, history, microphone)
- `commands.conf` — Spraakcommando's en acties
- `sentences.corpus` — Taalmodel corpus (automatisch gegenereerd)
- `language/` — Taalmodel bestanden (lm, dic)

## Gebruik

```bash
# Start Blather
python3 Blather.py

# Met GTK GUI
python3 Blather.py --interface gtk

# Met Qt GUI
python3 Blather.py --interface qt

# Configure voice commands in commands.conf
# Example:
# "turn on lights": "light on"
# "turn off lights": "light off"
```

### Configuratie

- `config/commands.conf` — spraakcommando's (KEY:value formaat)
- `config/options.yaml` — opties (continuous, history, microphone, interface)
- `config/language/` — dictionary (.dic) en language model (.lm)
- `config/data/` — tekstbestanden voor voice responses
- `config/plugins/` — shell plugins voor custom acties

### Commando's

Commando's worden gedefinieerd in `config/commands.conf`:

```
# Wat je zegt: uit te voeren commando
HELLO: echo "Hello World" | espeak
OPEN FIREFOX: firefox &
```

Gebruik `$VOICE`, `$KEYPRESS`, `$KEYTYPE`, `$CLICK`, `$BROWSER` etc. voor desktop automatie.

## Bijdragers

- [itsdarklikehell](https://github.com/itsdarklikehell) — Onderhouder

## Licentie

GPLv3 — zie [LICENSE](LICENSE) voor details.

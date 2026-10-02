# blather


## Development Visualization

<video src="https://raw.githubusercontent.com/itsdarklikehell/blather/master/gource.mp4" controls width="100%"></video>

*Gource visualization showing the repository's commit history. See the [Gource workflow](.github/workflows/gource.yml) for details.*


<img src="https://img.shields.io/github/stars/itsdarklikehell/blather?style=flat-square&color=blue" alt="Stars">
<img src="https://img.shields.io/github/forks/itsdarklikehell/blather?style=flat-square&color=green" alt="Forks">
<img src="https://img.shields.io/github/license/itsdarklikehell/blather?style=flat-square" alt="License">
<img src="https://img.shields.io/github/actions/workflow/status/itsdarklikehell/blather/ci.yml?branch=main&label=CI&style=flat-square" alt="CI Status">

Blather is a speech recognizer that will run commands when a user speaks preset sentences.

## Installatie

### Vereisten

1. pocketsphinx
2. gstreamer-1.0 (and whatever plugin has pocketsphinx support)
3. gstreamer-1.0 base plugins (required for alsa)
4. python3-gi (only required for the Gtk based UI)
5. pyside6 (only required for the Qt based UI)
6. python3-yaml (only required for reading the config file)
7. xdotool, wmctrl, xclip (for desktop automation commands)

### Installatie

```bash
# Debian/Ubuntu
sudo apt-get install pocketsphinx python3-yaml python3-gi python3-gi-cairo \
  gir1.2-gtk-3.0 xdotool wmctrl xclip espeak

git clone https://github.com/itsdarklikehell/blather.git
cd blather
```

## Gebruik

```bash
# Start Blather (headless, continuous listen)
python3 Blather.py

# Start met GTK UI
python3 Blather.py -i g

# Start met Qt UI
python3 Blather.py -i q

# Start met continuous listen
python3 Blather.py -c

# Microfoon selecteren (nummer uit `arecord -l`)
python3 Blather.py -m 1
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

MIT — zie [LICENSE](LICENSE) voor details.

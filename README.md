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

1. Download and run Blather-Installer (it will install dependencies and clone this git and set up configuration)
2. pocketsphinx
3. gstreamer-0.10 (and what ever plugin has pocket sphinx support)
4. gstreamer-0.10 base plugins (required for alsa)
5. pyside (only required for the Qt based UI)
6. pygtk (only required for the Gtk based UI)
7. pyyaml (only required for reading the config file)

### Installatie

```bash
git clone https://github.com/itsdarklikehell/blather.git
cd blather
# Run the installer
./install.sh
```

## Gebruik

```bash
# Start Blather
python blather.py

# Configure voice commands in config.yaml
# Example:
# commands:
#   "turn on lights": "light on"
#   "turn off lights": "light off"
```

## Bijdragers

- [itsdarklikehell](https://github.com/itsdarklikehell) — Onderhouder

## Licentie

MIT — zie [LICENSE](LICENSE) voor details.

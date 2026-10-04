# Blather

Speech recognition with a GUI interface, using GStreamer and pocketsphinx.

## Features

- GTK and Qt interfaces
- Continuous listening mode
- Command execution based on recognized speech
- History tracking
- Configurable via YAML

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
# GTK interface
python3 Blather.py -g

# Qt interface
python3 Blather.py -q

# Continuous listening
python3 Blather.py -g -c
```

## Configuration

See `config/options.yaml` for available options.

## License

GPLv3

# Blather

Speech recognition with a GUI interface, using GStreamer and pocketsphinx.

## Features

- GTK and Qt interfaces
- Continuous listening mode
- Command execution based on recognized speech
- History tracking
- Configurable via YAML
- System tray icon (GTK)

## Installation

### From source

```bash
git clone https://github.com/itsdarklikehell/blather.git
cd blather
pip3 install -r requirements.txt
```

### Dependencies

- Python 3.9+
- GStreamer 1.0
- pocketsphinx
- PyYAML
- PyGObject (for GTK)
- PySide6 (for Qt)

## Usage

```bash
# GTK interface
python3 Blather.py -g

# Qt interface
python3 Blather.py -q

# Continuous listening
python3 Blather.py -g -c

# With history
python3 Blather.py -g -H 20

# With custom microphone
python3 Blather.py -g -m 1
```

## Configuration

See `config/options.yaml` for available options.

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `continuous` | bool | true | Start in continuous listening mode |
| `history` | int | 20 | Number of commands to store in history |
| `microphone` | int | 1 | Audio input card to use |
| `interface` | str | - | Force interface: 'q' for Qt, 'g' for GTK |
| `valid_sentence_command` | str | - | Command to run when valid sentence detected |
| `invalid_sentence_command` | str | - | Command to run when invalid sentence detected |
| `pass_words` | bool | false | Pass recognized words as arguments |

## Development

### Running tests

```bash
python -m pytest tests/ -v
```

### Linting

```bash
flake8 *.py
black --check *.py
isort --check-only *.py
```

### Security scanning

```bash
bandit -r *.py
```

## Project Structure

```
.
├── Blather.py          # Main application
├── GtkUI.py            # GTK interface
├── GtkTrayUI.py        # GTK system tray interface
├── QtUI.py             # Qt interface
├── Recognizer.py       # Speech recognition
├── blather.sh          # Launcher script
├── config/             # Configuration files
│   ├── options.yaml    # Default options
│   ├── commands.conf   # Command mappings
│   ├── plugins/        # Shell plugins
│   └── data/           # Data files
├── tests/              # Test suite
└── .github/            # GitHub workflows
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

GPLv3 - See [LICENSE](LICENSE) for details.

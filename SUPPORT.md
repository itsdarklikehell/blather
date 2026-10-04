# Support

## Documentatie

- [README](README.md) — Installatie en gebruik
- [CONTRIBUTING](CONTRIBUTING.md) — Hoe bij te dragen

## Hulp zoeken

1. Check de [README](README.md) voor veelvoorkomende problemen
2. Zoek in [bestaande issues](https://github.com/itsdarklikehell/blather/issues)
3. Open een [nieuw issue](https://github.com/itsdarklikehell/blather/issues/new/choose) als je vraag niet beantwoord is

## Veelvoorkomende problemen

### Geen audio output
Controleer of je microfoon is geconfigureerd en GStreamer er toegang toe heeft:
```bash
gst-device-monitor-1.0
```

### PocketSphinx niet gevonden
Installeer de Python bindings:
```bash
pip3 install pocketsphinx
```

### Import errors
Installeer alle dependencies:
```bash
pip3 install -r requirements.txt
```

### GStreamer errors
Installeer GStreamer plugins:
```bash
sudo apt-get install gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
```

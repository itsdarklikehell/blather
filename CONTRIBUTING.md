# Contributing to Blather

Bedankt voor je interesse om bij te dragen!

## Hoe te bijdragen

1. Fork de repository
2. Maak een feature branch (`git checkout -b feature/amazing-feature`)
3. Maak je wijzigingen
4. Test lokaal:
   ```bash
   shellcheck *.sh config/plugins/*.sh
   python3 -m py_compile *.py
   ```
5. Commit je wijzigingen (`git commit -m 'Add amazing feature'`)
6. Push naar de branch (`git push origin feature/amazing-feature`)
7. Open een Pull Request

## Code standaarden

### Shell scripts
- Gebruik `set -euo pipefail`
- Volg [ShellCheck](https://www.shellcheck.net/) richtlijnen
- Gebruik `#!/bin/bash` shebang

### Python
- Volg PEP 8
- Gebruik type hints waar mogelijk
- Voeg docstrings toe aan nieuwe functies

## Pull Requests

- Beschrijf wat je PR doet en waarom
- Referentie gerelateerde issues
- Houd PRs gefocust op één wijziging

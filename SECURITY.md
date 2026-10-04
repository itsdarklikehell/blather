# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

Als je een veiligheidslek vindt, open dan een [security advisory](https://github.com/itsdarklikehell/blather/security/advisories/new).

Voeg de volgende informatie toe:
- Type kwetsbaarheid
- Impact
- Stappen om te reproduceren
- Mogelijke fix (indien bekend)

We reageren binnen 48 uur op security issues.

## Scope

Blather voert shell-commando's uit op basis van spraakherkenning. Houd rekening met:
- Commando's in `config/commands.conf` worden uitgevoerd met shell privileges
- Plugins in `config/plugins/` worden uitgevoerd als shell scripts
- De microfooninput wordt lokaal verwerkt, niet naar externe servers gestuurd

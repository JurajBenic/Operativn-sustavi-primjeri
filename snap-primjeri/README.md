# Snap Primjeri

Ovaj direktorij sadrži primjere pakiranja i distribucije aplikacija pomoću Snapcraft alata na Linux operativnim sustavima.

## Sadržaj

- **jednostavna-terminal-aplikacija/**
  - Primjer terminalske Python aplikacije pakirane kao Snap.
  - Pokreće se iz terminala nakon instalacije Snapa.

- **web-aplikacija/**
  - Web aplikacija bazirana na Flask-u.
  - Pakirana kao Snap, pokreće se kao servis i dostupna je na localhostu.

- **webapp-service/**
  - Flask web aplikacija konfigurirana kao Snap servis.
  - Automatski se pokreće nakon instalacije i dostupna je na mreži.

- **gui-aplikacija/**
  - Primjeri GUI aplikacija (Flet/Flutter za Python) pakiranih kao Snap.
  - Pokreću se s podrškom za desktop okruženje (X11/Wayland).


## Pokretanje Snap aplikacija

1. Izgradite Snap paket u željenom direktoriju:
   ```bash
   snapcraft pack
   ```
2. Instalirajte Snap paket:
   ```bash
   sudo snap install <ime_paketa>_<verzija>_amd64.snap --devmode
   ```
3. Pokrenite aplikaciju:
   ```bash
   <ime_paketa>
   ```

## Napomene
- Svaki poddirektorij sadrži vlastiti `README.md` s detaljnim uputama za instalaciju i korištenje.
- Snapcraft omogućuje jednostavno pakiranje Python, Flask, PyQt i Flet aplikacija za Linux.
- Za objavu na Snap Store potrebno je kreirati Snapcraft račun.

## Dokumentacija
- [Snapcraft službena dokumentacija](https://snapcraft.io/docs)
- [Primjeri Snap paketa](https://github.com/snapcore/snapcraft)

---
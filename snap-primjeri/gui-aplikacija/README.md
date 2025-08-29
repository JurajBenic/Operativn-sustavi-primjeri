# Solitaire Flet

Ova aplikacija je Solitaire igra napisana u Pythonu koristeći Flet (Flutter za Python) i pakirana kao Snap paket.

## Značajke
- Pokretanje na Linux sustavima putem Snap paketa
- Nema potrebe za dodatnom instalacijom Python ovisnosti

## Instalacija

### Preduvjeti
- Snapd instaliran na sustavu
- X11 ili Wayland okruženje za prikaz GUI-a

### Koraci
1. Klonirajte repozitorij:
   ```bash
   git clone <URL>
   cd snap-primjeri/gui-aplikacija
   ```
2. Izgradite Snap paket:
   ```bash
   snapcraft pack
   ```
3. Instalirajte Snap paket:
   ```bash
   sudo snap install solitaire-flet_1.0_amd64.snap --devmode
   ```

## Pokretanje aplikacije

Pokrenite aplikaciju naredbom:
```bash
solitaire-flet
```

## Razvoj

### Lokalno pokretanje
1. Instalirajte ovisnosti:
   ```bash
   pip install -r solitaire-final/requirements.txt
   ```
2. Pokrenite aplikaciju:
   ```bash
   python3 solitaire-final/main.py
   ```

### Prilagodba
- Izvorni kod aplikacije nalazi se u `solitaire-final/`.
- Wrapper skripta `solitaire.sh` pokreće aplikaciju iz Snapa.
- Ovisnosti se definiraju u `requirements.txt`.
- Snapcraft konfiguracija je u `snapcraft.yaml`.

## Troubleshooting
- Ako dobijete poruku o nedostatku datoteka, provjerite da su `main.py` i sve potrebne datoteke kopirane u Snap paket (putem `organize` u `snapcraft.yaml`).
- Ako se pojave poruke vezane uz direktorije (`touch: cannot touch ...`), osigurajte da aplikacija kreira direktorije prije pisanja datoteka.
- Upozorenja iz ATK, IBUS ili Flutter enginea obično ne utječu na rad aplikacije.


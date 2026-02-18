# Tkinter Fullscreen Aplikacija

Ova aplikacija je jednostavna GUI aplikacija napisana u Pythonu koristeći Tkinter i pakirana kao Snap paket.

## Značajke
- Pokretanje na Linux sustavima putem Snap paketa
- Fullscreen prikaz s mogućnošću izlaza pritiskom na ESC
- Jednostavna interakcija s gumbovima i popup prozorima
- Nema potrebe za dodatnom instalacijom Python ovisnosti

## Instalacija

### Preduvjeti
- Snapd instaliran na sustavu
- X11 ili Wayland okruženje za prikaz GUI-a

### Koraci
1. Klonirajte repozitorij:
   ```bash
   git clone <URL>
   cd snap-primjeri/tkinter-app
   ```
2. Izgradite Snap paket:
   ```bash
   snapcraft pack
   ```
3. Instalirajte Snap paket:
   ```bash
   sudo snap install tkinter-app_1.0_amd64.snap --devmode
   ```

## Pokretanje aplikacije

Pokrenite aplikaciju naredbom:
```bash
tkinter-app
```

### Upravljanje aplikacijom
- **ESC** - Izlaz iz aplikacije i izlaz iz fullscreen moda
- **Otvori Popup** - Gumb koji otvara popup prozor s porukom

## Razvoj

### Lokalno pokretanje
1. Instalirajte ovisnosti:
   ```bash
   pip install -r app/requirements.txt
   sudo apt install python3-tk  # Za Linux
   ```
2. Pokrenite aplikaciju:
   ```bash
   python3 app/main.py
   ```

### Struktura aplikacije
- **app/main.py** - Glavna datoteka aplikacije s GUI kodom
- **app/__init__.py** - Python paket inicijalizacija
- **app/requirements.txt** - Python ovisnosti
- **launcher.sh** - Wrapper skripta koja pokreće aplikaciju iz Snapa
- **snapcraft.yaml** - Snapcraft konfiguracija za pakiranje

### Prilagodba
- Izvorni kod aplikacije nalazi se u `app/`.
- Wrapper skripta `launcher.sh` pokreće aplikaciju iz Snapa.
- Ovisnosti se definiraju u `app/requirements.txt`.
- Snapcraft konfiguracija je u `snapcraft.yaml`.
- Za dodavanje Python biblioteka, dodajte ih u `app/requirements.txt` i u `build-packages` sekciju u `snapcraft.yaml`.

## Troubleshooting
- Ako dobijete poruku o nedostatku Tkinter biblioteke, instalirajte je: `sudo apt install python3-tk`
- Ako se pojave poruke vezane uz X11 ili Wayland, osigurajte da koristite X11 ili Wayland window manager
- Upozorenja iz Tkinter enginea obično ne utječu na rad aplikacije
- Ako se aplikacija ne pokreće iz Snapa, provjerite da su sva potrebna plugs postavljena u `snapcraft.yaml` (desktop, x11, wayland)

## Više informacija
- [Snapcraft Dokumentacija](https://snapcraft.io/docs)
- [Tkinter Dokumentacija](https://docs.python.org/3/library/tkinter.html)
- [Snap Confinement Modovi](https://snapcraft.io/docs/snap-confinement)

# Ubuntu Core - GUI Kompleksna Aplikacija (Super Mario + Ubuntu Frame)

Ovaj dokument opisuje kako pokrenuti kompleksniju GUI aplikaciju na Ubuntu Core sustavu koristeći Snap i Ubuntu Frame.

Primjer aplikacije u ovom direktoriju je Super Mario igra pakirana kao strict snap i pokrenuta preko Wayland stacka (`ubuntu-frame` + `mesa-2404`).

Igrica je preuzeta s:
- https://github.com/mx0c/super-mario-python

## Opis projekta

Cilj primjera je pokazati:
- paketiranje veće pygame aplikacije s više asseta (slike, zvukovi, level JSON datoteke),
- rad aplikacije kao snap daemon servisa,
- prikaz preko Ubuntu Frame compositora na Ubuntu Core uređaju,
- pravilno čitanje i spremanje korisničkih postavki u writable snap direktorij.

## Struktura direktorija

- `super-mario/super-mario-python/` - izvorni kod igre (Python, assets, levels)
- `super-mario/snap/snapcraft.yaml` - snap konfiguracija
- `super-mario/wayland-launch/` - helper skripte za Wayland runtime
- `gui-app.json` / `gui-app.model` - model datoteke za Ubuntu Core image

## Build snap paketa

Iz `super-mario` direktorija na RPI 5:

```bash
cd ubuntu-core-primjeri/gui-kompleksna-aplikacija/super-mario
snapcraft pack
```

Instalacija na uređaj s Ubuntu:

```bash
sudo snap install --dangerous --devmode ./*.snap
```

## Ubuntu Core image (model)

Za izradu imagea koristi se potpisani model (`gui-app.model`) i lokalni snap za igricu.

Primjer:

```bash
ubuntu-image snap --allow-snapd-kernel-mismatch gui-app.model --snap <putanja-do-super-mario.snap>
```

## Spajanje potrebnih sučelja (plugs)

```bash
snap connect pygame-frame-demo:wayland ubuntu-frame:wayland
snap connect pygame-frame-demo:opengl
snap connect pygame-frame-demo:gpu-2404 mesa-2404:gpu-2404
```

## Pokretanje i logovi

Pokretanje/restart:

```bash
sudo snap set ubuntu-frame daemon=true
snap restart ubuntu-frame
snap restart pygame-frame-demo
```

Praćenje logova:

```bash
snap logs -f pygame-frame-demo
snap logs -f ubuntu-frame
```

Provjera statusa servisa:

```bash
snap services pygame-frame-demo
snap services ubuntu-frame
```

## Fullscreen rad igre

Igra je konfigurirana da radi fullscreen:
- koristi `pygame.FULLSCREEN`
- koristi `pygame.SCALED` gdje backend to podržava
- fallback je standardni fullscreen ako `SCALED` nije dostupan

To omogućuje da originalni game canvas ostane 640x480, a prikaz se ispravno skaluje na ekran uređaja.

## Što je `SNAP_USER_DATA`, gdje se koristi i zašto

`SNAP_USER_DATA` je environment varijabla koju **automatski postavlja snapd** kada aplikaciju pokrećeš kao snap.

Predstavlja direktorij za korisničke podatke koji je:
- writable
- izoliran po snapu i korisniku
- siguran za konfiguracije, cache i runtime datoteke koje aplikacija mijenja

### Zašto je potrebno koristiti `SNAP_USER_DATA`

U strict snapu je `$SNAP` read-only.  
To znači da zapis u putanje poput `./settings.json` unutar snap paketa završava greškom:

- `OSError: [Errno 30] Read-only file system`

Zato se postavke moraju spremati u writable lokaciju, npr.:
- `$SNAP_USER_DATA/settings.json`

### Gdje se koristi u ovom projektu

U datoteci:
- `super-mario/super-mario-python/classes/Menu.py`

Logika:
- čita `SNAP_USER_DATA`
- ako postoji, kreira/koristi `settings.json` u tom direktoriju
- ako ne postoji (npr. lokalno pokretanje bez snapa), koristi fallback `./settings.json`

Tipične vrijednosti:
- `/home/<korisnik>/snap/<snap-ime>/current` (classic sustavi)
- `/root/snap/<snap-ime>/current` (daemon kao root na Ubuntu Core)

## Tipične greške i rješenja

### 1. `Failed to create XKB context`

Uzrok:
- nedostupni XKB podaci u confined runtimeu

Rješenje:
- uključiti `xkb-data` u snap
- postaviti `XKB_CONFIG_ROOT`
- osigurati layout bind na `/usr/share/X11/xkb`

### 2. `FileNotFoundError: ./sprites/Mario.json`

Uzrok:
- krivi working directory i/ili nepotpuno kopirani assets u `$SNAP/app`

Rješenje:
- koristiti `source: super-mario-python` u `snapcraft.yaml`
- kopirati cijeli sadržaj projekta u `$SNAP/app`
- postaviti `os.chdir(...)` na direktorij aplikacije prije importa modula

### 3. `Read-only file system: './settings.json'`

Uzrok:
- pokušaj pisanja u read-only `$SNAP`

Rješenje:
- spremanje postavki u `$SNAP_USER_DATA/settings.json`

### 4. `ValueError: array must match surface dimensions`

Uzrok:
- blur površina fiksirana na 640x480, a stvarna rezolucija je drugačija

Rješenje:
- koristiti `screen.get_size()` i dinamične dimenzije u pause/blur kodu


## Napomena o arhitekturama

Projekt je ciljan primarno za `arm64` (Raspberry Pi).
Ako buildaš i druge arhitekture, provjeri dostupnost Python wheelova za sve ovisnosti (posebno `scipy`).

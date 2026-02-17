# Qt6 GUI snap (Ubuntu Core)

Ovaj projekt sadrži jednostavnu Qt6 aplikaciju u Pythonu (PySide6) i pripadajuću
Snapcraft konfiguraciju za pokretanje na Ubuntu Core (arm64/Raspberry Pi).

`snap/` i `wayland-launch/` preuzeti su iz repozitorija:
https://github.com/canonical/iot-example-graphical-snap (branch: 24/Qt6-example)

## Struktura

- app/ — Python aplikacija (main.py) i requirements.txt
- snap/ — Snapcraft konfiguracija i hook skripte
- wayland-launch/ — pomoćne skripte za Wayland okruženje

## Važna napomena o line ending‑u (LF)

**Sve .sh skripte moraju imati LF završetke linija (ne CRLF). CRLF uzrokuje
greške pri izvršavanju hookova (npr. “cannot snap-exec”).**

## Build (arm64)

Za ispravnu arm64 binarnu strukturu, build mora biti pokrenut na arm64
uređaju (Raspberry Pi) naredbom:
```bash
snapcraft pack --build-for=arm64
```
### Alternativa: remote build

Moguće je koristiti `snapcraft remote-build`, ali tada repozitorij mora biti
javan, jer Launchpad preuzima izvorni kod.

## Instalacija (na Ubuntu Core)

snap install qt6-gui_0.1_arm64.snap --dangerous

## Objašnjenje skripti (.sh)

### snap/hooks/install

- Postavlja početnu konfiguraciju opcije `daemon` putem `snapctl`.
- Ako je uređaj “classic”, postavlja `daemon=false`; u suprotnom `daemon=true`.
- Služi za inicijalno ponašanje servisa prilikom instalacije snap‑a.

### snap/hooks/configure

- Čita vrijednost `daemon`.
- Ako je `true`, uključuje i pokreće servis; ako je `false`, zaustavlja i
	isključuje servis.
- Validira vrijednost (dozvoljeno: true|false).
- `$SNAP_INSTANCE_NAME` je naziv instance snap‑a (koristi se za ciljanje servisa
  i naredbi za taj snap).

### snap/hooks/post-refresh

- Nakon osvježavanja snap‑a ponavlja logiku iz install hooka.
- Održava konzistentnu konfiguraciju `daemon` nakon refresh‑a.

### wayland-launch/bin/setup.sh

- Pokušava automatski povezati potrebne plugove (opengl, wayland, gpu-2404).
- Ako ne uspije, ispisuje upute za ručno povezivanje.
- Omogućuje lakše pokretanje GUI aplikacije u Wayland okruženju.

### wayland-launch/bin/wayland-launch

- Provjerava jesu li plugovi povezani.
- Čeka da Wayland socket postane dostupan (uz inotifywait).
- Priprema `XDG_RUNTIME_DIR` i postavlja `WAYLAND_DISPLAY`.
- Na kraju pokreće zadanu aplikaciju.

## Objašnjenje snapcraft.yaml

Datoteka je u [snap/snapcraft.yaml](snap/snapcraft.yaml) i definira paketiranje
aplikacije:

- Osnovne postavke: `name`, `version`, `summary`, `description`, `base`,
	`confinement`, `grade`.
- `apps`:
	- `qt6-gui` pokreće Python aplikaciju preko `bin/python3 $SNAP/app/main.py`.
	- `command-chain` koristi `gpu-2404-wrapper` i `wayland-launch` za grafičko
		okruženje.
	- `plugs` sadrži `opengl` i `wayland`.
	- `environment` postavlja Qt/PySide6 putanje i `LD_LIBRARY_PATH`.
	- `daemon` je servisna instanca s istim `command` i `environment`.
- `plugs`:
	- `gpu-2404` content plug za Mesa (grafički stack).
- `environment` (globalno): XDG i XKB putanje za ispravno ponašanje alata.
	- **XDG** ([freedesktop.org](https://www.freedesktop.org/wiki/) standard) definira gdje aplikacije traže i spremaju
		konfiguracije, cache i podatke (npr. `XDG_CONFIG_HOME`, `XDG_CACHE_HOME`,
		`XDG_DATA_DIRS`). U snapu se preusmjerava u $SNAP_USER_* kako bi sve bilo
		izolirano po korisniku i po snapu.
	- **XKB** (X Keyboard Extension) definira layout tipkovnice, mapiranja tipki
		i pravila tipkanja. `XKB_CONFIG_ROOT` pokazuje gdje se nalaze XKB definicije
		kako bi tipkovnica radila ispravno unutar snap okruženja.
- `layout`: mapiranja potrebnih sistemskih putanja (fontovi, ikone, GTK, DRM).
- `parts`:
	- `python-app` koristi `plugin: python`, instalira ovisnosti iz
		`requirements.txt` i postavlja `main.py` u `$SNAP/app`.
	- `setup` ugrađuje Wayland pomoćne skripte i ubacuje potrebne plugove.
	- `gpu-2404` donosi grafičke biblioteke iz `mesa-2404` i čisti višak.
- `platforms`: ograničava build na arm64 (Raspberry Pi).

### YAML sidra i reference (anchors & aliases)

U snapcraft.yaml koriste se YAML sidra (anchors) i reference (aliases) kako bi
se izbjeglo ponavljanje istih blokova:

- `command-chain: &_command-chain` definira listu i daje joj ime (sidro)
	`_command-chain`.
- `command-chain: *_command-chain` kasnije ponovno koristi istu listu
	(alias/reference).

Isto vrijedi za:

- `plugs: &_plugs` → definira skup plugova.
- `plugs: *_plugs` → ponovno koristi isti skup plugova.
- `environment: &_environment` → definira env varijable.
- `environment: *_environment` → ponovno koristi iste env varijable.

Oznaka `&` stvara sidro (anchor), a `*` koristi sidro (alias). To je standard
YAML funkcionalnost i nema posebne veze sa Snapcraftom, osim što se koristi za
uredniji YAML.



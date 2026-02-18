# Jednostavna Terminal Aplikacija

Ova aplikacija je jednostavna terminalska aplikacija napisana u Pythonu. Služi kao primjer za izradu i pakiranje terminal aplikacija pomoću Snapcraft alata.

## Značajke
- Osnovna interakcija putem terminala
- Lako proširiva dodatnim funkcionalnostima

## Instalacija

### Preduvjeti
- Instaliran Snapcraft alat
- Python 3.10 ili noviji

### Koraci
1. Klonirajte repozitorij:
   ```bash
   git clone <URL>
   cd snap-primjeri/jednostavna-terminal-aplikacija
   ```
2. Izgradite snap paket:
   ```bash
   snapcraft pack
   ```
3. Instalirajte snap paket:
   ```bash
   sudo snap install jednostavna-terminal-aplikacija_0.1_amd64.snap --devmode
   ```

## Korištenje
Pokrenite aplikaciju pomoću naredbe:
```bash
jednostavna-terminal-aplikacija
```

## Razvoj

### Postavljanje Razvojnog Okruženja
1. Kreirajte virtualno okruženje:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instalirajte ovisnosti:
   ```bash
   pip install -r requirements.txt
   ```

### Alternativa: Korištenje Conda okruženja
1. Kreirajte Conda okruženje:
   ```bash
   conda create --name myenv python=3.10
   conda activate myenv
   ```
2. Instalirajte ovisnosti:
   ```bash
   pip install -r requirements.txt
   ```

### Pokretanje Aplikacije
Pokrenite aplikaciju lokalno:
```bash
python3 src/app.py
```

### Alternativa: Pokretanje s Conda okruženjem
Pokrenite aplikaciju unutar aktiviranog Conda okruženja:
```bash
conda activate myenv
python src/app.py
```

# Detaljno objašnjenje snapcraft.yaml datoteke

`snapcraft.yaml` je konfiguracijska datoteka koja definira kako se aplikacija pakira kao Snap paket.
U nastavku su dana objašnjenja svih ključnih dijelova za ovaj primjer:

### 1. name
Naziv Snap paketa. Mora biti jedinstven na Snap Store-u.
```yaml
name: jednostavna-terminal-aplikacija
```

### 2. base
Definira osnovni operativni sustav na kojem se paket temelji (npr. `core22` za Ubuntu 22.04, `core24` za Ubuntu 24.04).
```yaml
base: core24
```

### 3. platforms
Definira podržane platforme i arhitekture za koje se snap može izgraditi. Ovo polje zamjenjuje stariji `architectures` za `core24` i novije verzije.

```yaml
platforms:
  amd64:
    build-on: [amd64]
    build-for: [amd64]
  arm64:
    build-on: [amd64, arm64]
    build-for: [arm64]
  armhf:
    build-on: [amd64, armhf]
    build-for: [armhf]
```

**Objašnjenje polja:**
- **platforms**: glavni ključ koji sadrži definicije svih podržanih platformi
- **amd64 / arm64 / armhf**: naziv platforme (arhitektura)
- **build-on**: lista arhitektura na kojima se snap može graditi
  - primjer: `build-on: [amd64, arm64]` znači da se snap za arm64 može graditi na amd64 (cross-compilation) ili na arm64 (native)
- **build-for**: ciljana arhitektura za koju je snap namijenjen
  - `build-for: [arm64]` znači da će rezultat biti snap paket za arm64 arhitekturu

**Primjeri korištenja:**

1. **Native build** (gradnja za istu arhitekturu):
   ```bash
   snapcraft pack
   ```
   Gradi za trenutnu arhitekturu (npr. amd64 ako si na x86_64 računalu).

2. **Cross-compilation** (gradnja za drugu arhitekturu):
   ```bash
   snapcraft pack --build-for=arm64
   ```
   Gradi na amd64 za arm64 (zahtijeva LXD ili remote-build).

3. **Remote build** (gradnja na cloud serverima):
   ```bash
   snapcraft remote-build
   ```
   Gradi za sve definirane platforme na Launchpad serverima.

4. **LXD build sa emulacijom**:
   ```bash
   snapcraft pack --use-lxd --build-for=arm64
   ```
   Koristi LXD i QEMU emulaciju za cross-compilation.

**Napomena:** Cross-compilation zahtijeva da `build-on` lista uključuje trenutnu arhitekturu. Npr. za gradnju arm64 na amd64, arm64 mora imati `build-on: [amd64, arm64]`.

**Razlika između core22 i core24:**
- **core22 i stariji**: koriste `architectures: [amd64, arm64]`
- **core24 i noviji**: koriste `platforms:` s `build-on` i `build-for` definicijama

### 4. version
Verzija aplikacije koja se pakira.
```yaml
version: '0.1'
```

### 5. summary
Kratki opis aplikacije (do 78 znakova).
```yaml
summary: Jednostavna terminalska aplikacija u Pythonu
```

### 6. description
Detaljan opis aplikacije.
```yaml
description: |
  Ova aplikacija demonstrira izradu i pakiranje jednostavne terminalske aplikacije u Pythonu koristeći Snapcraft.
```

### 7. grade
Definira stabilnost paketa (`devel` za razvojnu, `stable` za produkcijsku verziju).
```yaml
grade: devel
```

### 8. confinement
Definira razinu izolacije aplikacije. Postoje tri moda:

- **devmode**: Razvojni mod - aplikacija se pokreće **bez zaštitnog okruženja** (sandboxa) i ima **puni pristup** svim resursima sustava. Koristi se tijekom razvoja jer omogućava brz razvoj bez potrebe za konfiguracijom dozvola, ali s manjom sigurnosti.

- **strict**: Strogi sandboxing - aplikacija je **izoliirana** od ostatka sustava i ima **maksimalnu sigurnost**. Pristupa samo što je eksplicitno dozvoljeno putem `plugs` (npr. network, home, camera). Preporučuje se za **produkcijske** pakete jer koristi najstrože sigurnosne standarde.

- **classic**: Klasični način - aplikacija ima **gotovo puni pristup** sustavu kao normalna instalacija. Kombinacija je devmodea i stricga s manje sandboxinga. Koristi se ako je aplikacija inkompatibilna sa strict modom, ali je rijetko u praksi.

```yaml
confinement: devmode
```

### 9. apps
Definira kako se aplikacija pokreće i koje naredbe postaju dostupne nakon instalacije.
```yaml
apps:
  jednostavna-terminal-aplikacija:
    command: bin/jednostavna-terminal-aplikacija
    # Moguće je dodati environment varijable, plugs itd.
```
- **command**: Putanja do izvršne skripte koja se pokreće kad korisnik upiše naziv aplikacije.

### 10. parts
Definira kako se aplikacija gradi, koje ovisnosti se instaliraju i odakle se uzima izvorni kod.
```yaml
parts:
  jednostavna-terminal-aplikacija:
    plugin: python
    source: .
    # Moguće je dodati requirements, build-packages, stage-packages itd.
```
- **plugin**: Određuje način gradnje (ovdje Python plugin koristi setup.py).
- **source**: Putanja do izvornog koda (najčešće `.` ili `src/`).
- **build-packages**: Paketi potrebni za vrijeme gradnje (npr. gcc, python3-dev).
- **stage-packages**: Paketi koji se uključuju u Snap za vrijeme izvođenja.

### 11. dodatne opcije
Moguće je dodati:
- **environment**: Definiranje varijabli okoline.
- **plugs**: Definiranje pristupa resursima sustava (npr. network, home).

---

Ova struktura omogućuje da se aplikacija izgradi, instalira i pokreće na bilo kojem sustavu koji podržava Snap, uz minimalnu konfiguraciju.


## Povezanost setup.py, snapcraft.yaml i src direktorija

- **setup.py**: Ova datoteka definira Python paket, njegove ovisnosti i način instalacije. Kada se aplikacija instalira (ručno ili putem Snapa), setup.py osigurava da se svi potrebni moduli i skripte pravilno postave.

- **src/**: Ovaj direktorij sadrži izvorni kod aplikacije. Sve Python skripte i moduli koji čine funkcionalnost aplikacije nalaze se ovdje. U setup.py se obično navodi da se paket instalira iz ovog direktorija.

- **snapcraft.yaml**: Ova datoteka definira kako se aplikacija pakira kao Snap paket. Ključna sekcija je `parts`, gdje se koristi Python plugin:

  ```yaml
  parts:
    jednostavna-terminal-aplikacija:
      plugin: python
      source: .
  ```

  Ovdje Snapcraft automatski traži datoteku `setup.py` u navedenom direktoriju (`source: .`). Kroz Python plugin, Snapcraft pokreće instalaciju aplikacije koristeći upute iz `setup.py` (poput ovisnosti, entry pointa i modula). Na taj način, sve što je definirano u `setup.py` (npr. koje se datoteke instaliraju, kako se aplikacija pokreće) automatski se primjenjuje prilikom izgradnje Snap paketa.

  Ukratko: Snapcraft.yaml povezuje izvorni kod (src/) i instalacijske upute (setup.py) te omogućuje da se aplikacija izgradi i distribuira kao Snap paket, spreman za pokretanje na bilo kojem sustavu koji podržava Snap.
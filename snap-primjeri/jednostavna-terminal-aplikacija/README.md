# Jednostavna Terminal Aplikacija

Ova aplikacija je jednostavna terminalska aplikacija napisana u Pythonu. Služi kao primjer za izradu i pakiranje terminalskih aplikacija pomoću Snapcraft alata.

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

## Detaljno objašnjenje snapcraft.yaml datoteke

`snapcraft.yaml` je konfiguracijska datoteka koja definira kako se aplikacija pakira kao Snap paket. Evo objašnjenja svih ključnih dijelova za ovaj primjer:

### 1. name
Naziv Snap paketa. Mora biti jedinstven na Snap Store-u.
```yaml
name: jednostavna-terminal-aplikacija
```

### 2. base
Definira osnovni operativni sustav na kojem se paket temelji (npr. `core22` za Ubuntu 22.04).
```yaml
base: core22
```

### 3. version
Verzija aplikacije koja se pakira.
```yaml
version: '0.1'
```

### 4. summary
Kratki opis aplikacije (do 78 znakova).
```yaml
summary: Jednostavna terminalska aplikacija u Pythonu
```

### 5. description
Detaljan opis aplikacije.
```yaml
description: |
  Ova aplikacija demonstrira izradu i pakiranje jednostavne terminalske aplikacije u Pythonu koristeći Snapcraft.
```

### 6. grade
Definira stabilnost paketa (`devel` za razvojnu, `stable` za produkcijsku verziju).
```yaml
grade: devel
```

### 7. confinement
Definira razinu izolacije aplikacije (`devmode`, `strict`, `classic`).
```yaml
confinement: devmode
```

### 8. apps
Definira kako se aplikacija pokreće i koje naredbe postaju dostupne nakon instalacije.
```yaml
apps:
  jednostavna-terminal-aplikacija:
    command: bin/jednostavna-terminal-aplikacija
    # Moguće je dodati environment varijable, plugs itd.
```
- **command**: Putanja do izvršne skripte koja se pokreće kad korisnik upiše naziv aplikacije.

### 9. parts
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

### 10. dodatne opcije
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
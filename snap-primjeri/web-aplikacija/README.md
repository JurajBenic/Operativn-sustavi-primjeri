# Web Aplikacija

Ovaj Snap paket sadrži jednostavnu Flask aplikaciju koja prikazuje poruku "Hello, World!". Demonstrira kako pakirati i implementirati Python web aplikaciju koristeći Snapcraft.

## Značajke
- Prikazuje poruku "Hello, World!".
- Uključuje osnovnu strukturu mapa za Flask aplikacije.
- Demonstrira korištenje Snapcrafta za pakiranje Python web aplikacija.

## Struktura mapa
```
web-aplikacija/
├── app/
│   ├── app.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   └── templates/
│       └── index.html
├── requirements.txt
├── run-flask.sh
└── snapcraft.yaml
```

## Instalacija

### Preduvjeti
- Snapcraft instaliran na vašem sustavu.
- Python 3.10 ili noviji.

### Koraci
1. Klonirajte repozitorij:
   ```bash
   git clone <repository-url>
   cd snap-primjeri/web-aplikacija
   ```
2. Izgradite Snap paket:
   ```bash
   snapcraft
   ```
3. Instalirajte Snap paket:
   ```bash
   sudo snap install web-aplikacija_0.1_amd64.snap --devmode
   ```

## Korištenje

### Pokretanje aplikacije
Nakon instalacije, aplikaciju možete pokrenuti koristeći:
```bash
web-aplikacija
```

Aplikacija će biti dostupna na `http://localhost:5000`.

## Razvoj

### Postavljanje razvojnog okruženja
1. Kreirajte virtualno okruženje:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instalirajte ovisnosti:
   ```bash
   pip install -r requirements.txt
   ```

### Pokretanje aplikacije lokalno
Pokrenite Flask aplikaciju:
```bash
python app/app.py
```

## Objašnjenje dijela snapcraft.yaml: parts i apps

### parts
Ova sekcija definira kako se aplikacija i dodatne skripte pakiraju u Snap paket.

- **web-aplikacija**:
  - `plugin: python`: Koristi Python plugin za automatsko upravljanje ovisnostima i instalaciju aplikacije.
  - `source: .`: Označava da se izvorni kod aplikacije nalazi u trenutnom direktoriju.
  - `python-requirements: ['requirements.txt']`: Navodi putanju do datoteke s Python ovisnostima koje će biti instalirane.

- **run-flask-script**:
  - `plugin: dump`: Koristi dump plugin za kopiranje dodatnih datoteka u Snap paket.
  - `source: .`: Označava da se skripta i direktorij aplikacije kopiraju iz trenutnog direktorija.
  - `organize`: Definira mapiranje datoteka unutar Snapa:
    - `run-flask.sh: bin/run-flask.sh`: Skripta se kopira u direktorij `bin`.
    - `app: bin/app/`: Direktorij aplikacije se kopira u `bin/app/`.

### apps
Ova sekcija definira kako se aplikacija pokreće i koje dozvole koristi.

- **web-aplikacija**:
  - `command: bin/run-flask.sh`: Definira naredbu koja se pokreće kada korisnik pokrene Snap aplikaciju. Ovdje se pokreće skripta koja starta Flask aplikaciju.
  - `plugs: [network-bind]`: Omogućuje aplikaciji da otvara mrežne portove (npr. za web server).
  - `environment`:
    - `FLASK_APP: $SNAP/bin/app/app.py`: Postavlja varijablu okoline koja definira putanju do Flask aplikacije unutar Snapa.
    - `FLASK_ENV: development`: Postavlja Flask okruženje na razvojni način (za debugiranje).

---

Ova konfiguracija omogućuje da se Python aplikacija i potrebne skripte pravilno instaliraju i pokreću unutar Snap paketa, uz potrebne dozvole i varijable okoline.
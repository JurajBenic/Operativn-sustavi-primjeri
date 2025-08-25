# Webapp Servis

Ovaj Snap paket sadrži jednostavnu Flask aplikaciju koja demonstrira kako pakirati i implementirati Python web aplikaciju kao servis koristeći Snapcraft.

## Značajke
- Prikazuje poruku "Hello, World!".
- Uključuje osnovnu strukturu mapa za Flask aplikacije.
- Demonstrira korištenje Snapcrafta za pakiranje Python web aplikacije kao Snap servisa.

## Struktura mapa
```
webapp-service/
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
   cd snap-primjeri/webapp-service
   ```
2. Izgradite Snap paket:
   ```bash
   snapcraft
   ```
3. Instalirajte Snap paket:
   ```bash
   sudo snap install webapp-service_0.1_amd64.snap --devmode
   ```

## Korištenje
Nakon instalacije, možete pokrenuti Flask aplikaciju koristeći sljedeću naredbu:
```bash
sudo snap start webapp-service
```
Aplikacija će biti dostupna na [http://localhost:5000](http://localhost:5000).

### Zaustavljanje servisa
Za zaustavljanje servisa koristite naredbu:
```bash
sudo snap stop webapp-service
```

### Informacije o servisu
Za prikaz informacija o servisu koristite naredbu:
```bash
snap services webapp-service
```

## Razvoj

### Pokretanje lokalno
Za pokretanje aplikacije lokalno bez Snapa:
1. Idite u direktorij `app/`:
   ```bash
   cd app
   ```
2. Instalirajte ovisnosti:
   ```bash
   pip install -r requirements.txt
   ```
3. Pokrenite Flask aplikaciju:
   ```bash
   python app.py
   ```

### Modifikacija Snap paketa
Za ažuriranje Snap paketa:
1. Napravite promjene u aplikaciji ili `snapcraft.yaml` datoteci.
2. Ponovno izgradite Snap paket:
   ```bash
   snapcraft
   ```
3. Ponovno instalirajte ažurirani paket:
   ```bash
   sudo snap install webapp-service_0.1_amd64.snap --devmode --dangerous
   ```

## Objašnjenje sekcije 'apps' iz snapcraft.yaml

Ova sekcija definira kako se aplikacija pokreće i upravlja kao servis unutar Snap paketa:

- **command: bin/run-flask.sh**
  - Definira skriptu koja se pokreće za startanje Flask aplikacije.

- **daemon: simple**
  - Aplikacija se pokreće kao jednostavan servis (daemon) koji radi u pozadini.

- **restart-condition: always**
  - Servis će se automatski ponovno pokrenuti ako dođe do pada ili greške.

- **plugs: [network-bind]**
  - Omogućuje aplikaciji da otvara mrežne portove (npr. za web server).

- **environment**
  - `FLASK_APP: $SNAP/bin/app/app.py` – Postavlja varijablu okoline koja definira putanju do Flask aplikacije unutar Snapa.
  - `FLASK_ENV: production` – Postavlja Flask okruženje na produkcijski način.

Ova konfiguracija omogućuje da se Flask aplikacija automatski pokreće kao servis, ima pristup mreži i koristi produkcijsko okruženje.

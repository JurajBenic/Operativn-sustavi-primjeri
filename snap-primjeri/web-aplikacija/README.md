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
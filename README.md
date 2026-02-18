# Operativni Sustavi

Ovaj repozitorij sadrži primjere i upute za kolegij **Operativni sustavi** i pokriva različite aspekte modernog razvoja aplikacija i distribuiranja softvera.

## 📋 Sadržaj Repozitorija

### 1. **docker-primjeri/**
   - Primjeri pakiranja i distribucije aplikacija pomoću Docker tehnologije
   - Obuhvaća: web aplikacije (Flask), baze podataka (PostgreSQL), terminal aplikacije, GUI aplikacije
   - Koristi `docker-compose` za orkestaciju nekoliko kontejnera
   - Idealno za učenje containerizacije, imagea i servisa

### 2. **snap-primjeri/**
   - Primjeri pakiranja aplikacija kao Snap paketa za Linux
   - Obuhvaća: terminal aplikacije, web aplikacije (Flask), GUI aplikacije (PyQt/Tkinter)
   - Demonstrira `snapcraft.yaml` konfiguraciju, različite `confinement` modove (devmode, strict, classic)
   - Idealno za učenje Snap ekosustava i sigurnosti aplikacija

### 3. **ubuntu-core-primjeri/**
   - Primjeri rada s Ubuntu Core operativnim sustavom za IoT uređaje
   - Obuhvaća: GUI aplikacije, web aplikacije, minimal Ubuntu Core imagee
   - Demonstrira izradu vlastitih Ubuntu Core imagea za Raspberry Pi
   - Obuhvaća potpisivanje modela, konfiguraciju firmware-a, Multipass virtualizaciju
   - Idealno za učenje IoT razvoja, minimalističkih operativnih sustava i snap ekosustava

---

## 🛠️ Potrebni Alati

### **Windows (PowerShell/CMD)**
- Docker Desktop
- WSL2 s Ubuntu distribucijom
- Snapcraft (kroz WSL2)
- Ubuntu Image Alat (kroz WSL2)
- XLaunch / VcXsrv (X Server za WSL2)
- Raspberry Pi Imager
- Git (Git CLI ili GitHub Desktop)
- Python 3.10+ (ili Conda/Miniconda)

### **Linux (Ubuntu/Debian)**
- Docker i Docker Compose
- Snapcraft
- Ubuntu Image Alat
- Multipass (za virtualizaciju)
- Git
- Python 3.10+ s razvojnim alatima (python3-pip, python3-venv, python3-dev ili Conda/Miniconda)

> Detaljne upute za instalaciju svakog alata dostupne su u odgovarajućim dokumentacijama i službenim web stranicama.

## 🚀 Kako Početi

### **Za Docker primjere:**
```bash
cd docker-primjeri/
cd <poddirektorij-primjera>/
docker-compose up
```

### **Za Snap primjere:**
```bash
cd snap-primjeri/
cd <poddirektorij-primjera>/
snapcraft pack
sudo snap install <paket>_<verzija>_amd64.snap --devmode
<paket>  # Pokrenite aplikaciju
```

### **Za Ubuntu Core primjere:**
```bash
cd ubuntu-core-primjeri/
# Pratite detaljne upute u pojedinom README.md za svaki primjer
```

---

## 📚 Dokumentacija

- [Docker Dokumentacija](https://docs.docker.com/)
- [Snapcraft Dokumentacija](https://snapcraft.io/docs)
- [Ubuntu Core Dokumentacija](https://ubuntu.com/core/docs)
- [Multipass Dokumentacija](https://multipass.run/)

---

## 📝 Napomene

- Svaki poddirektorij sadrži vlastiti `README.md` s detaljnim uputama za instalaciju i korištenje
- Za rad sa Snap primjerima na Windowsima trebate WSL2 s Ubuntu distribucijom
- Za Ubuntu Core primjere trebate `snapcraft` i `ubuntu-image` alate instalirane
- Za objavu na Snap Store trebate kreirati Snapcraft račun i prijaviti se lokalno

---

## 📂 Struktura Direktorija

```
Operativni_sustavi_primjeri/
├── docker-primjeri/
│   ├── baza-podataka/
│   ├── gui-aplikacija/
│   ├── jednostavna-terminal-aplikacija/
│   └── web-aplikacija/
├── snap-primjeri/
│   ├── jednostavna-terminal-aplikacija/
│   ├── web-aplikacija/
│   ├── webapp-service/
│   ├── gui-aplikacija/
│   └── tkinter-app/
├── ubuntu-core-primjeri/
│   ├── gui-aplikacija/
│   ├── gui-kompleksna-aplikacija/
│   ├── jednostavna-terminal-apliakcija/
│   ├── minimal-ubuntu-image/
│   └── web-aplikacija/
└── README.md
```



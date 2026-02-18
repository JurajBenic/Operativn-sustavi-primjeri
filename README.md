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

## 🛠️ Instalacija Potrebnih Alata

Ovisno o operativnom sustavu koji koristite, trebate instalirati sljedeće alate:

### **Windows (PowerShell/CMD)**

#### **1. Docker Desktop**
Potreban za rad sa Docker primjerima.
```powershell
# Preuzimanje instalatora
# Posjetite: https://www.docker.com/products/docker-desktop/
# Pokrenite instalator i pratite upute
# Provjerite instalaciju:
docker --version
docker run hello-world
```

#### **2. Snapcraft (Windows Subsystem for Linux - WSL2)**
Potreban za rad sa Snap primjerima (zahtijeva WSL2 s Ubuntu distribucijom).
```powershell
# Prvo instalirajte WSL2
wsl --install -d Ubuntu

# U WSL2 Ubuntu terminalu:
sudo apt update
sudo apt install snapcraft -y

# Instalirajte ubuntu-image alat (za Ubuntu Core primjere):
sudo snap install ubuntu-image --classic --edge

# Provjerite instalaciju:
snapcraft --version
ubuntu-image --version
```

#### **3. Multipass**
Potreban za virtualizaciju Ubuntu Core imagea na Windowsima.
```powershell
# Preuzimanje instalatora
# Posjetite: https://multipass.run/
# Pokrenite instalator
# Provjerite instalaciju:
multipass version
```

#### **4. Raspberry Pi Imager**
Alatka za pisanje Ubuntu Core i Raspberry Pi OS imagea na SD kartice.
```powershell
# Preuzimanje instalatora:
# https://www.raspberrypi.com/software/
# Pokrenite instalator i pratite upute
```

#### **5. Git (opciono, za kloniranje repozitorija)**
**Opcija A: Git CLI**
```powershell
# Preuzimanje instalatora:
# https://git-scm.com/download/win
# Ili preko Chocolatey:
choco install git

# Provjerite instalaciju:
git --version
```

**Opcija B: GitHub Desktop (GUI)**
```powershell
# Preuzimanje instalatora:
# https://desktop.github.com/
# Pokrenite instalator i pratite upute
# GitHub Desktop pruža grafičko sučelje za rad s Git repozitorijima
```

#### **6. Python 3.10+**
Potreban za pokretanje Python aplikacija.

**Opcija A: Python.org**
```powershell
# Preuzimanje:
# https://www.python.org/downloads/
# Ili preko Chocolatey:
choco install python

# Provjerite instalaciju:
python --version
```

**Opcija B: Conda (Miniconda ili Anaconda)**
```powershell
# Preuzimanje Miniconde (lakša verzija):
# https://docs.conda.io/projects/miniconda/en/latest/
# Pokrenite instalator

# Ili preko Chocolatey:
choco install miniconda3

# Provjerite instalaciju:
conda --version

# Kreirajte okruženje s Python 3.10+:
conda create --name myenv python=3.10
conda activate myenv
```

---

### **Linux (Ubuntu/Debian)**

#### **1. Docker**
```bash
# Instalacija Docker alata
sudo apt update
sudo apt install docker.io -y

# Dodajte korisnika u docker grupu (kako bi se izbjegao sudo)
sudo usermod -aG docker $USER
newgrp docker

# Instalacija Docker Compose
sudo apt install docker-compose -y

# Provjerite instalaciju:
docker --version
docker-compose --version
```

#### **2. Snapcraft**
```bash
# Instalacija Snapcraft-a
sudo apt update
sudo apt install snapcraft -y

# Provjerite instalaciju:
snapcraft --version
```

#### **3. Ubuntu Image Alat (za Ubuntu Core)**
```bash
# Instalacija ubuntu-image alata
sudo snap install ubuntu-image --classic --edge

# Provjerite instalaciju:
ubuntu-image --version
```

#### **4. Multipass (opciono, za virtualizaciju)**
```bash
# Instalacija Multipass-a
sudo snap install multipass --classic

# Provjerite instalaciju:
multipass version
```

#### **5. Git**
```bash
# Instalacija Git-a
sudo apt install git -y

# Provjerite instalaciju:
git --version
```

#### **6. Python 3.10+ (Razvojni alati)**
```bash
# Instalacija Python-a i razvojnih alata
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-dev -y

# Provjerite instalaciju:
python3 --version
pip3 --version
```

#### **7. Snapcraft Credentials (opciono, za objavu na Snap Store)**
```bash
# Prijava na Snapcraft
snapcraft login

# Izvoz credentials-a (ako trebate na drugom stroju)
snapcraft export-login credentials.txt
```

---

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



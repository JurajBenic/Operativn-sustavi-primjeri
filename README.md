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

**Preuzimanje i instalacija:**
```powershell
# Direktno preuzimanje EXE instalatora:
# https://www.docker.com/products/docker-desktop/
# 1. Kliknite na "Download for Windows"
# 2. Pokrenite preuzetu Docker Desktop Installer.exe datoteku
# 3. Pratite upute u instalatoru

# Ili preko Chocolatey:
choco install docker-desktop
```

**Provjera instalacije:**
```powershell
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

#### **3. XLaunch (X Server za WSL2 - opciono)**
Potreban za pokretanje GUI aplikacija u WSL2 na Windows domaćinu.

**Preuzimanje i instalacija:**
```powershell
# Direktno preuzimanje EXE instalatora:
# https://sourceforge.net/projects/vcxsrv/
# 1. Kliknite na "Download" gumb
# 2. Pokrenite preuzetu VcXsrv-XX.XX.X.X.installer.exe datoteku
# 3. Pratite upute u instalatoru

# Ili preko Chocolatey:
choco install vcxsrv
```

**Konfiguracija i pokretanje:**
```powershell
# Nakon instalacije, pokrenite XLaunch iz Start menija
# Konfiguracija: Multiple windows, Start no client, sve ostalo default
# U WSL2 terminalu postavite:
export DISPLAY=$(ip route list default | awk '{print $3}'):0
```

#### **4. Multipass**
Potreban za virtualizaciju Ubuntu Core imagea na Windowsima.

**Preuzimanje i instalacija:**
```powershell
# Direktno preuzimanje EXE instalatora:
# https://multipass.run/
# 1. Kliknite na "Download" i odaberite Windows verziju
# 2. Pokrenite preuzetu multipass-installer-windows.exe datoteku
# 3. Pratite upute u instalatoru

# Ili preko Chocolatey:
choco install multipass
```

**Provjera instalacije:**
```powershell
multipass version
```

#### **4. Raspberry Pi Imager**
Alatka za pisanje Ubuntu Core i Raspberry Pi OS imagea na SD kartice.

**Preuzimanje i instalacija:**
```powershell
# Direktno preuzimanje EXE instalatora:
# https://www.raspberrypi.com/software/
# 1. Kliknite na "Download for Windows"
# 2. Pokrenite preuzetu imager.exe datoteku
# 3. Pratite upute u instalatoru

# Ili preko Chocolatey:
choco install rpi-imager
```

#### **5. Git (opciono, za kloniranje repozitorija)**

**Opcija A: Git CLI (Command Line)**
```powershell
# Direktno preuzimanje EXE instalatora:
# https://git-scm.com/download/win
# 1. Kliknite na "64-bit Git for Windows Setup" (ili 32-bit ako trebate)
# 2. Pokrenite preuzetu Git-X.XX.X-64-bit.exe datoteku
# 3. Pratite upute u instalatoru

# Ili preko Chocolatey:
choco install git

# Provjera instalacije:
git --version
```

**Opcija B: GitHub Desktop (GUI)**
```powershell
# Direktno preuzimanje EXE instalatora:
# https://desktop.github.com/
# 1. Kliknite na "Download for Windows"
# 2. Pokrenite preuzetu GitHubDesktopSetup-x64.exe datoteku
# 3. Pratite upute u instalatoru
# GitHub Desktop pruža grafičko sučelje za rad s Git repozitorijima

# Ili preko Chocolatey:
choco install github-desktop
```

#### **7. Python 3.10+**
Potreban za pokretanje Python aplikacija.

**Opcija A: Python.org**
```powershell
# Direktno preuzimanje EXE instalatora:
# https://www.python.org/downloads/
# 1. Kliknite na "Download Python 3.X.X"
# 2. Pokrenite preuzetu python-3.X.X-amd64.exe datoteku
# 3. VAŽNO: Označite "Add Python 3.X to PATH" tijekom instalacije
# 4. Pratite upute u instalatoru

# Ili preko Chocolatey:
choco install python

# Provjera instalacije:
python --version
```

**Opcija B: Conda (Miniconda ili Anaconda)**
```powershell
# Direktno preuzimanje EXE instalatora (Miniconda - lakša verzija):
# https://docs.conda.io/projects/miniconda/en/latest/
# 1. Preuzmi "Miniconda3 Windows 64-bit"
# 2. Pokrenite Miniconda3-latest-Windows-x86_64.exe datoteku
# 3. Pratite upute u instalatoru

# Ili preko Chocolatey:
choco install miniconda3

# Provjera instalacije:
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



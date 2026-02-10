# Ubuntu Core Primjeri

Ovaj direktorij sadrži primjere i upute za rad s Ubuntu Core i Snapcraft ekosustavom.

## Što je Ubuntu Core?
Ubuntu Core je sigurni, minimalistički operativni sustav za IoT uređaje, baziran na Snap paketima.

## Osnovni koraci

### 1. Kreiranje Ubuntu One računa
Za objavu i upravljanje Snap paketima na Ubuntu Core uređajima, potrebno je imati Ubuntu One račun.

1. Posjetite [Ubuntu One registraciju](https://login.ubuntu.com/).
2. Kliknite na "Create an account".
3. Ispunite tražene podatke (email, lozinka, ime).
4. Potvrdite email adresu klikom na poveznicu u emailu koji ćete primiti.

### 2. Povezivanje credentials-a na razvojni stroj
Za autentifikaciju i objavu Snap paketa, potrebno je povezati Snapcraft s vašim Ubuntu One računom.

1. Instalirajte Snapcraft:
   ```bash
   sudo snap install snapcraft --classic
   ```
2. Izvezite credentials u datoteku (npr. za prijenos na drugi uređaj):
   ```bash
   sudo snapcraft export-login credentials.txt
   ```
3. Za korištenje credentials u shellu, postavite varijablu okoline:
   ```bash
   export SNAPCRAFT_STORE_CREDENTIALS=$(cat credentials.txt)
   ```
4. Ako želite koristiti credentials na drugom stroju, uvezite ih:
   ```bash
   snapcraft import-login credentials.txt
   ```
> **Napomena:** Ovisno o konfiguraciji sustava, možda ćete morati koristiti `sudo` kod izvoza credentials (naredba 2) i kod čitanja datoteke credentials.txt (naredba 3), npr.:
> ```bash
> sudo snapcraft export-login credentials.txt
> export SNAPCRAFT_STORE_CREDENTIALS=$(sudo cat credentials.txt)
> ```

### 3. Dohvaćanje developer account ID-a
Developer account ID potreban je za upravljanje uređajima i objavu paketa.

1. Nakon prijave, pokrenite:
   ```bash
   snapcraft whoami
   ```
2. U izlazu pronađite polje `id:` – to je vaš developer account ID.

### Instalacija alata za izradu imagea
Za izradu vlastitog Ubuntu Core imagea instalirajte alat `ubuntu-image`:
```bash
sudo snap install ubuntu-image --classic --edge
```

## Dokumentacija
- [Ubuntu Core službena dokumentacija](https://ubuntu.com/core/docs)
- [Snapcraft dokumentacija](https://snapcraft.io/docs)
- [Ubuntu One](https://login.ubuntu.com/)

---

# Podešavanje novog Raspberry Pi 5

Prije instalacije Ubuntu Core-a na Raspberry Pi 5, potrebno je ažurirati firmware kako bi Ubuntu Core mogao pravilno prikazati sliku.

## Preporučeni postupak: Ažuriranje firmware-a preko Raspberry Pi OS

1. **Instalirajte Raspberry Pi OS** na SD karticu (možete koristiti Raspberry Pi Imager).

2. **Pokrenite sustav** i prijavite se.

3. **Izvršite ažuriranje sustava i firmware-a:**
   ```bash
   sudo apt update
   sudo apt full-upgrade -y
   sudo rpi-eeprom-update -a
   sudo reboot
   ```

4. Nakon ponovnog pokretanja, Raspberry Pi 5 ima ažurirani firmware koji omogućava Ubuntu Core-u da pravilno prikaže sliku.

5. Sada možete instalirati Ubuntu Core.

## Alternativni pristup: Ručna izmjena konfiguracije
> **Napomena:** Ovaj pristup omogućava samo shell pristup i **ne radi s ubuntu-frame** grafičkim okvirom. Za punu podršku ubuntu-frame-a, preporučuje se ažuriranje firmware-a preko Raspberry Pi OS-a.

Ako ne želite prvo instalirati Raspberry Pi OS, možete ručno prilagoditi grafičku konfiguraciju:

1. Na boot particiji Ubuntu Core-a, otvorite datoteku `config.txt`.

2. Zamijenite liniju:
   ```
   dtoverlay=vc4-fkms-v3d,cma-128
   ```
   s:
   ```
   dtoverlay=vc4-kms-v3d-pi5
   ```


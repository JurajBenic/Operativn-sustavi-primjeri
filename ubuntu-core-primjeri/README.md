# Ubuntu Core Primjeri

Ovaj direktorij sadrži primjere i upute za rad s Ubuntu Core i Snapcraft ekosustavom.

## Što je Ubuntu Core?
Ubuntu Core je sigurni, minimalistički operativni sustav za IoT uređaje, baziran na Snap paketima.

## Osnovni postupci

### 1. Kreiranje Ubuntu One računa
Za objavu i upravljanje Snap paketima na Ubuntu Core uređajima, potrebno je imati Ubuntu One račun.

1. Posjetite [Ubuntu One registraciju](https://login.ubuntu.com/).
2. Kliknite na "Create an account".
3. Ispunite tražene podatke (email, lozinka, ime).
4. Potvrdite email adresu klikom na poveznicu u emailu koji ćete primiti.

### 2. Povezivanje credentials na razvojni stroj
Za autentikaciju i objavu Snap paketa, potrebno je povezati Snapcraft s vašim Ubuntu One računom.

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

### 3. Dohvat developer account ID-a
Developer account ID je potreban za upravljanje uređajima i objavu paketa.

1. Nakon prijave, pokrenite:
   ```bash
   snapcraft whoami
   ```
2. U izlazu pronađite polje `id:` – to je vaš developer account ID.

## Dokumentacija
- [Ubuntu Core službena dokumentacija](https://ubuntu.com/core/docs)
- [Snapcraft dokumentacija](https://snapcraft.io/docs)
- [Ubuntu One](https://login.ubuntu.com/)

---

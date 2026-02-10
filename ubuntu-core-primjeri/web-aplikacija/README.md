# Ubuntu Core - Web Aplikacija

Ovaj dokument opisuje korake za izradu, konfiguraciju i korištenje Ubuntu Core imagea za web aplikacije. Sadržava upute za dva različita pristupa:
- **web-app.json** - Jednostavna web aplikacija (bez grafičkog sučelja)
- **kiosk-web-app.json** - Web aplikacija s grafičkim sučeljem (kiosk način rada)

## Preduvjeti
Prije nego što započnete, provjerite imate li sljedeće:

- Instaliran `ubuntu-image` alat ([upute za instalaciju](../README.md#instalacija-alata-za-izradu-imagea))
- Snapcraft račun i credentials ([upute](../README.md#2-povezivanje-credentials-na-razvojni-stroj))
- Developer account ID ([upute](../README.md#3-dohvat-developer-account-id-a))
- Raspberry Pi 5 ili drugi kompatibilni uređaj
- SD kartica s minimalno 8 GB prostora
- Za kiosk način rada: Monitor s HDMI priključkom
- Za jednostavnu web aplikaciju: Mrežni pristup (SSH ili lokalni terminal)
- Web aplikacija iz Snap primjera mora biti buildana za Raspberry Pi 5 (arm64 arhitektura) [snap-primjeri/webapp-service](../../snap-primjeri/webapp-service/README.md)

---

## 1. Jednostavna Web Aplikacija (web-app.json)

Ovaj pristup instalira Flask web aplikaciju kao snap servis koji radi u pozadini. Pristup aplikaciji moguć je putem web preglednika s drugog uređaja na istoj mreži.

### 1.1. Priprema modela

1. Otvorite datoteku `web-app.json`.

2. Zamijenite placeholdere s vašim podacima:
   ```json
   "authority-id": "<vas developer account id>",
   "brand-id": "<vas brand id>",
   ```
   
   Koristite `snapcraft whoami` za dohvat vašeg developer ID-a.

3. Ažurirajte timestamp na trenutno vrijeme:
   ```bash
   date -Iseconds --utc
   ```
   Kopirajte rezultat u polje `timestamp`.

4. Provjerite putanju do snap datoteke:
   ```json
   {
       "name": "webapp-service",
       "type": "app",
       "file": "webapp-service_0.1_arm64.snap"
   }
   ```
   Snap aplikaciju dodajete prilikom generiranja Ubuntu Core imagea koristeći opciju `--snap`:
   ```bash
   ubuntu-image snap --allow-snapd-kernel-mismatch jednostavna-terminal-apliakcija.model --snap path/to/your-snap-file.snap
   ```
   Zamijenite `path/to/your-snap-file.snap` s točnom putanjom do vaše snap datoteke.

### 1.2. Potpisivanje i generiranje imagea

1. **Provjerite postojeće ključeve:**
   ```bash
   snapcraft list-keys
   ```

2. **Ako nemate ključ, kreirajte novi:**
   ```bash
   snapcraft create-key moj-kljuc
   ```
   Zapamtite lozinku!

3. **Registrirajte ključ:**
   ```bash
   snapcraft register-key moj-kljuc
   ```

4. **Potpišite model:**
   ```bash
   snap sign -k moj-kljuc web-app.json > web-app.model
   ```

5. **Generirajte Ubuntu Core image:**
   ```bash
   ubuntu-image snap --allow-snapd-kernel-mismatch web-app.model --snap ../../snap-primjeri/webapp-service/webapp-service_0.1_arm64.snap
   ```

   Rezultat je `pi.img` datoteka spremna za zapisivanje na SD karticu.

### 1.3. Zapisivanje imagea na SD karticu

**Linux:**
```bash
sudo dd if=pc.img of=/dev/sdX bs=4M status=progress conv=fsync
```
Zamijenite `/dev/sdX` s nazivom vaše SD kartice.

**Windows/macOS:**
- Koristite Raspberry Pi Imager (https://www.raspberrypi.com/software/)
- Koristite balenaEtcher (https://www.balena.io/etcher/)

⚠️ **UPOZORENJE:** Provjerite naziv uređaja prije zapisivanja!

### 1.4. Početna konfiguracija i pokretanje

1. **Umetnite SD karticu** u Raspberry Pi 5.

2. **Povežite uređaj:**
   - Mrežni kabel (preporučeno za prvu konfiguraciju)
   - Monitor i tipkovnica (opcionalno)

3. **Uključite uređaj** i pratite upute za inicijalnu konfiguraciju:
   - Odaberite Wi-Fi mrežu (ako koristite bežičnu mrežu)
   - Unesite SSH javni ključ (ili kreirajte novi na Ubuntu One računu)
   - Pričekajte završetak inicijalizacije

4. **Spojite se putem SSH-a:**
   ```bash
   ssh <ubuntu-one-username>@<ip-adresa-uređaja>
   ```

5. **Provjerite status servisa:**
   ```bash
   snap services webapp-service
   ```

6. **Pristupite web aplikaciji:**
   - Otvorite web preglednik na drugom uređaju u istoj mreži
   - Unesite: `http://<ip-adresa-raspberry-pi>:5000`

### 1.5. Upravljanje servisom

**Zaustavljanje:**
```bash
sudo snap stop webapp-service
```

**Pokretanje:**
```bash
sudo snap start webapp-service
```

**Restart:**
```bash
sudo snap restart webapp-service
```

**Praćenje logova:**
```bash
sudo snap logs webapp-service -f
```

---

## 2. Kiosk Web Aplikacija (kiosk-web-app.json)

Ovaj pristup kreira kiosk sustav gdje se web aplikacija prikazuje na ekranu u punom zaslonu. Koristi se za digitalne info table, kiosk terminale, i slične primjene.

### 2.1. Struktura kiosk-web-app.json modela

Model `kiosk-web-app.json` proširuje osnovni model s dodatnim snap paketima za grafičko sučelje:

```json
{
    "type": "model",
    "series": "16",
    "model": "ubuntu-core-24-pi-arm64",
    "architecture": "arm64",
    "authority-id": "<vas developer account id>",
    "brand-id": "<vas brand id>",
    "timestamp": "2026-02-06T12:26:17+00:00",
    "base": "core24",
    "grade": "dangerous",
    "snaps": [...]
}
```

### 2.2. Snaps uključeni u kiosk-web-app.json

Osim baznih snap paketa (pi, pi-kernel, core24, snapd, console-conf), kiosk model uključuje:

#### Grafičke komponente (Ubuntu Frame stack):

```json
{
    "name": "mesa-2404",
    "type": "app",
    "default-channel": "latest/stable",
    "id": "HyhSEBPv3vHsW6uOHkQR384NgI7S6zpj"
}
```
- **mesa-2404**: OpenGL/Vulkan driveri za grafičku akceleraciju (baziran na core24)

```json
{
    "name": "ubuntu-frame",
    "type": "app",
    "default-channel": "24/stable",
    "id": "BPZbvWzvoMTrpec4goCXlckLe2IhfthK"
}
```
- **ubuntu-frame**: Wayland compositor koji omogućava prikaz grafičkih aplikacija (novi stack za core24)

#### WebKit stack za prikaz web sadržaja:

```json
{
    "name": "core22",
    "type": "base",
    "default-channel": "latest/stable",
    "id": "amcUKQILKXHHTlmSa7NMdnXSx02dNeeT"
}
```
- **core22**: Dodatna baza potrebna za WPE WebKit koji još nije portiran na core24

```json
{
    "name": "mesa-core22",
    "type": "app",
    "default-channel": "latest/stable",
    "id": "UijXdFgvIKp9ZZ6P4ijPAJHWZtSKgWm"
}
```
- **mesa-core22**: Mesa driveri za core22 (kompatibilnost s WPE WebKit-om)

```json
{
    "name": "wpe-webkit-mir-kiosk",
    "type": "app",
    "default-channel": "22/stable",
    "id": "01sV9tv4UTUQTU3jYsAF1gJ5qv7ZqGls"
}
```
- **wpe-webkit-mir-kiosk**: Kiosk preglednik baziran na WPE WebKit engine-u (iscrtava web stranice u punom zaslonu)

#### Vaša web aplikacija:

```json
{
    "name": "webapp-service",
    "type": "app",
    "file": "webapp-service_0.1_arm64.snap"
}
```
- **webapp-service**: Flask servis koji poslužuje web sadržaj

### 2.3. Kako kiosk stack radi zajedno

```
┌─────────────────────────────────────────┐
│         webapp-service (Flask)          │  ← Vaša aplikacija (port 5000)
│         http://localhost:5000           │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│     wpe-webkit-mir-kiosk (Browser)      │  ← Prikazuje web stranicu
│      Puni zaslon, bez okvira UI         │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│         ubuntu-frame (Compositor)       │  ← Upravlja grafikom (Wayland)
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│      mesa-2404 (Graphics drivers)       │  ← OpenGL/Vulkan akceleracija
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│         Hardware (Raspberry Pi 5)       │
│              HDMI → Monitor             │
└─────────────────────────────────────────┘
```

### 2.4. Priprema modela

1. Otvorite datoteku `kiosk-web-app.json`.

2. Zamijenite placeholdere s vašim podacima:
   ```json
   "authority-id": "<vas developer account id>",
   "brand-id": "<vas brand id>",
   ```

3. Ažurirajte timestamp:
   ```bash
   date -Iseconds --utc
   ```

4. Provjerite putanju do webapp-service snap datoteke:
   ```json
   {
       "name": "webapp-service",
       "type": "app",
       "file": "webapp-service_0.1_arm64.snap"
   }
   ```

### 2.5. Potpisivanje i generiranje imagea

1. **Potpišite model:**
   ```bash
   snap sign -k moj-kljuc kiosk-web-app.json > kiosk-web-app.model
   ```

2. **Generirajte Ubuntu Core image:**
   ```bash
   ubuntu-image snap --allow-snapd-kernel-mismatch kiosk-web-app.model --snap ../../snap-primjeri/webapp-service/webapp-service_0.1_arm64.snap
   ```

### 2.6. Zapisivanje imagea i pokretanje

Postupak je isti kao za jednostavnu web aplikaciju (pogledajte sekciju 1.5).

### 2.7. Početna konfiguracija kiosk moda

1. **Umetnite SD karticu** i uključite Raspberry Pi 5 s **spojenim monitorom**.

2. **Pratite inicijalnu konfiguraciju** na ekranu ili putem SSH-a.

3. **Provjerite je li ubuntu-frame pokrenut:**
   ```bash
   snap services ubuntu-frame
   ```

4. **Automatsko pokretanje ubuntu-frame-a prilikom boot-a sustava**
   ```bash
   sudo snap set ubuntu-frame daemon=true
   ```


5. **Konfigurirajte wpe-webkit-mir-kiosk** da prikazuje vašu aplikaciju i da se automatski pokrene:
   ```bash
   sudo snap set wpe-webkit-mir-kiosk url=http://localhost:5000
   snap set wpe-webkit-mir-kiosk daemon=true
   ```

5. **Pokrenite ili restartujte kiosk:**
   ```bash
   sudo snap restart wpe-webkit-mir-kiosk
   ```

6. **Monitor bi trebao prikazati** vašu Flask aplikaciju u punom zaslonu!



### 2.8. Napredna konfiguracija kiosk-a
Dodatne opcije za konfiguraciju Ubuntu Frame možete pronaći u službenoj dokumentaciji: [Ubuntu Frame Configuration Options](https://canonical.com/mir/docs/ubuntu-frame-configuration-options)

**Primjer rotacija ekrana:**
```bash
sudo snap set ubuntu-frame display='
layouts:
  default:
    cards:
    - card-id: 0
      HDMI-A-1:
        orientation: right
'
sudo snap restart ubuntu-frame
```

### 2.9. Otklanjanje problema (Troubleshooting)

**Prazan ekran / Nije prikazan web sadržaj:**
```bash
# Provjerite dali je webapp-service aktivan
sudo snap services webapp-service

# Provjerite logove webapp-service
sudo snap logs webapp-service -f

# Provjerite dali je ubuntu-frame pokrenut
sudo snap services ubuntu-frame

# Provjerite konfiguraciju wpe-webkit-mir-kiosk
snap get wpe-webkit-mir-kiosk

# Resetirajte sve servise
sudo snap restart webapp-service
sudo snap restart ubuntu-frame
sudo snap restart wpe-webkit-mir-kiosk
```

**Web aplikacija ne odgovara:**
```bash
# Testiranje Flask servisa putem curl
curl http://localhost:5000

# Praćenje HTTP zahtjeva
sudo snap logs webapp-service -f
```

---

## 3. Usporedba pristupa

| Značajka | web-app.json | kiosk-web-app.json |
|----------|--------------|---------------------|
| **Grafičko sučelje** | Ne | Da (puni zaslon) |
| **Monitor potreban** | Ne | Da |
| **Pristup aplikaciji** | Putem web preglednika s drugog uređaja | Prikazano na monitoru |
| **Veličina imagea** | ~500 MB | ~1.5 GB |
| **Dodatni snap paketi** | 6 | 11 (+ grafički stack) |
| **Primjena** | Headless servisi, API serveri | Digitalne info table, kiosk terminali |
| **Složenost konfiguracije** | Jednostavna | Umjerena (konfiguracija grafike) |

---

## 4. Automatsko ažuriranje

Snap paketi se automatski ažuriraju prema konfiguraciji:
```bash
# Provjera postavki refresh
snap refresh --time

# Ručno ažuriranje
sudo snap refresh webapp-service
```

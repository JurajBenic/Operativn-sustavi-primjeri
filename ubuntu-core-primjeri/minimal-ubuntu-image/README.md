# Minimalni Ubuntu Core Image s Multipassom

Ovaj dokument opisuje korake za izradu i pokretanje minimalnog Ubuntu Core imagea koristeći Multipass.

## Preduvjeti
- Instaliran Multipass ([upute za instalaciju](https://multipass.run/))
- Snapcraft račun i credentials (ako želite vlastiti image)

## Koraci

### 1. Preuzimanje službenog Ubuntu Core modela

Za izradu minimalnog Ubuntu Core imagea najjednostavnije je koristiti službeni model (JSON konfiguraciju) koju je pripremio Snapcore tim. Model definira osnovne komponente (gadget, kernel, core snap) i arhitekturu uređaja.

Primjer preuzimanja modela za Raspberry Pi (arm64):
```bash
wget -O minimalni-model.json https://raw.githubusercontent.com/snapcore/models/master/ubuntu-core-24-pi-arm64.json
```

Napomena: Naziv modela (JSON datoteke) može biti proizvoljan i mijenja se po želji korisnika. U ovom primjeru koristi se naziv `minimalni-model.json`.

Ova datoteka (`minimalni-model.json`) sadrži sve potrebne informacije za izradu Ubuntu Core imagea za određeni uređaj. Modeli za druge uređaje i arhitekture dostupni su na službenom repozitoriju:
- https://github.com/snapcore/models

**Što smo napravili?**
- Preuzeli smo službeni model koji definira kako će izgledati naš Ubuntu Core image.
- Model sadrži popis snap paketa (gadget, kernel, core), arhitekturu i ostale parametre potrebne za build.
- Ovaj model koristimo kao ulaznu datoteku za alat `ubuntu-image` koji generira .img datoteku spremnu za pokretanje na uređaju ili u virtualnom okruženju (Multipass).


### 2. Objašnjenje strukture minimalni-model.json datoteke

Datoteka `minimalni-model.json` je model koji definira kako će izgledati Ubuntu Core image. Sadrži nekoliko ključnih polja:

- **type**: Vrsta modela, obično "model".
- **series**: Verzija Ubuntu Core serije (npr. 22 ili 24).
- **authority-id**: ID developera koji potpisuje image (vaš developer account ID).
- **brand-id**: ID branda (može biti isti kao authority-id ili ID vašeg branda).
- **model**: Naziv modela (npr. "minimal-pc" ili "custom-pi").
- **grade**: "signed" za produkcijski image, "dangerous" za testni image bez potpisa.
- **architectures**: Popis podržanih arhitektura (npr. "amd64", "arm64").
- **snaps**: Popis snap paketa koji će biti uključeni u image.

Primjer strukture:
```json
{
  "type": "model",
  "series": 24,
  "authority-id": "<vaš developer account id>",
  "brand-id": "<vaš brand id>",
  "model": "minimal-pc",
  "grade": "signed",
  "architectures": ["amd64"],
  "snaps": [ ... ]
}
```

**Napomena:**
- Svaka promjena u modelu zahtijeva ponovno generiranje imagea.
- Za produkcijski image koristite "signed" i potpišite model s vašim računom.
- Za testiranje možete koristiti "dangerous" bez potpisa.




### 3. Prilagodba modela za vlastiti račun

Nakon preuzimanja službenog modela, potrebno je prilagoditi polja `authority-id` i `brand-id` u datoteci `minimalni-model.json`.

Službeni model koristi vrijednosti:
```json
"authority-id": "canonical",
"brand-id": "canonical",
```

**Što treba napraviti?**
- Zamijenite `authority-id` s vašim developer account ID-om (dobivenim naredbom `snapcraft whoami`)
- Zamijenite `brand-id` s vašim brand ID-om (može biti isti kao developer account ID ili ID vašeg branda na Snap Store-u)

Primjer:
```json
"authority-id": "<vaš developer account id>",
"brand-id": "<vaš brand id>",
```

**Zašto?**
- Time model postaje personaliziran i omogućuje izradu imagea koji je potpisan vašim računom, a ne Canonicalovim.
- Bez ove izmjene, nećete moći potpisati i koristiti vlastiti image na uređajima.



### 4. Dodavanje snap paketa u model

U datoteci `minimalni-model.json` nalazi se sekcija `snaps` koja definira popis snap paketa koji će biti uključeni u Ubuntu Core image.

Primjer sekcije:
```json
"snaps": [
  {
    "name": "pi",
    "type": "gadget",
    "default-channel": "24/stable",
    "id": "YbGa9O3dAXl88YLI6Y1bGG74pwBxZyKg"
  },
  {
    "name": "pi-kernel",
    "type": "kernel",
    "default-channel": "24/stable",
    "id": "jeIuP6tfFrvAdic8DMWqHmoaoukAPNbJ"
  },
  ...
]
```

**Što su snaps?**
- Snap paketi su aplikacije ili komponente (kernel, gadget, core) koje se instaliraju u Ubuntu Core image.
- Gadget snap sadrži konfiguraciju hardvera, kernel snap sadrži jezgru, a core snap sadrži osnovni runtime.
- Možete dodati vlastite aplikacije ili servise kao snap pakete.

**Atributi za svaki snap objekt:**
- `name`: Ime snap paketa (obavezno).
- `file`: Putanja do lokalnog snap paketa (opcionalno, koristi se za lokalne snapse).
- `channel`: Kanal s kojeg se snap povlači (npr. "stable", "beta", "edge").
- `id`: Jedinstveni ID snap paketa (koristi se za precizno određivanje snapa).
- `type`: Vrsta snapa (npr. "kernel", "gadget", "core", "app").
- `base`: Baza snapa (npr. "core22"), koristi se za aplikacijske snapse.
- `default-profiles`: Profili koji se automatski primjenjuju (napredno, rijetko korišteno).


**Kako dodati novi snap?**
1. Dodajte novi objekt u popis `snaps` u modelu:

```json
{
  "name": "moja-aplikacija",
  "channel": "stable",
  "file": "putanja/do/snapa.snap",
  "id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "type": "app",
  "base": "core22"
}
```



### 5. Potpisivanje modela

Za izradu produkcijskog Ubuntu Core imagea potrebno je potpisati model s vašim ključem.

**Kako provjeriti imate li već Snapcraft ključ:**
- Pokrenite naredbu:
    ```bash
    snapcraft list-keys
    ```
- Prikazat će se popis dostupnih ključeva. Ako je vaš ključ naveden, možete ga koristiti.

**Kako generirati ključ za potpisivanje modela (ako ne postoji):**
1. Pokrenite Snapcraft naredbu za generiranje ključa:
   ```bash
   snapcraft create-key <naziv-kljuca>
   ```

- Prilikom kreiranja Snapcraft ključa od vas će biti zatraženo da postavite lozinku (passphrase).
- Lozinka štiti vaš privatni ključ i potrebna je svaki put kad potpisujete model ili snapse.
- Obavezno zapamtite ili sigurno pohranite lozinku – bez nje nećete moći koristiti ključ za potpisivanje.
- Ako zaboravite lozinku, morat ćete generirati novi ključ i ponovno ga registrirati.

**Kako registrirati ključ na Snapcraft račun:**
- Ako ste generirali novi ključ, registrirajte ga naredbom:
    ```bash
    snapcraft register-key <naziv-kljuca>
    ```
- Time se ključ povezuje s vašim Snapcraft računom i može se koristiti za potpisivanje modela.


**Kada i kako promijeniti timestamp u JSON datoteci:**
- Timestamp u modelu mora biti postavljen na vrijeme i datum koji je nakon kreiranja vašeg ključa za potpisivanje! 
- To znači da trebate urediti polje `timestamp` u minimalni-model.json i postaviti ga na trenutno vrijeme (nakon što ste generirali ključ).
  ```json
  "timestamp": "2025-08-29T12:00:00Z"
  ```
- Za dobivanje trenutnog vremena u ISO 8601 formatu (npr. `"2025-08-29T12:00:00Z"`) koristite naredbu:
    ```bash
    date -Iseconds --utc
    ```
- Kopirajte rezultat i zalijepite ga u polje `timestamp` u vašem modelu.



**Kako potpisati model:**
1. Potpisivanje se radi `snap` naredbom:
   ```bash
   snap sign -k <naziv-kljuca> minimalni-model.json > minimalni-model.model
   ```
2. Rezultat potpisivanja je datoteka `minimalni-model.model` koja sadrži potpisanu model assertion. Ovu datoteku sada možete koristiti za izradu Ubuntu Core imagea.

### 6. Generiranje Ubuntu Core imagea

```bash
ubuntu-image snap --allow-snapd-kernel-mismatch minimalni-model.model 
```

Ova naredba generira `.img` datoteku koju možete koristiti za pokretanje u Multipass-u ili na fizičkom uređaju.

**Napomena:** Zamijenite `minimalni-model.model` s nazivom vaše potpisane model datoteke.

### 6.1. Kreiranje image na SD kartici

Nakon generiranja `.img` datoteke, zapišite ju na SD karticu za pokretanje na fizičkom uređaju (npr. Raspberry Pi).

**Alati za zapisivanje image-a:**

**Linux:**
- `dd` naredba: `sudo dd if=pc.img of=/dev/sdX bs=4M status=progress conv=fsync`
- Raspberry Pi Imager
- balenaEtcher

**Windows:**
- Raspberry Pi Imager (https://www.raspberrypi.com/software/)
- balenaEtcher (https://www.balena.io/etcher/)
- Rufus

**macOS:**
- `dd` naredba ili Raspberry Pi Imager / balenaEtcher

**⚠️ UPOZORENJE:** Prije zapisivanja provjerite naziv uređaja SD kartice kako ne biste prepisali podatke na hard disku!

### 7. Konfiguracija IP adrese i spajanje putem SSH-a

Nakon što ste uspješno zapisali Ubuntu Core image na SD karticu i pokrenuli uređaj (npr. Raspberry Pi), potrebno je konfigurirati mrežne postavke kako biste se mogli spojiti na uređaj putem SSH-a.

Nakon uspješnog spajanja putem SSH-a, možete nastaviti s daljnjom konfiguracijom ili instalacijom dodatnih snap paketa.

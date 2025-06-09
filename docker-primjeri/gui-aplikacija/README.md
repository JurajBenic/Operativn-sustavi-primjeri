# GUI Aplikacija (PyQt6)

Ovaj direktorij sadrži GUI aplikaciju baziranu na PyQt6, koja se pokreće korištenjem Docker-a.

## Sadržaj

- **Dockerfile** – Konfiguracijska datoteka za izgradnju Docker slike.
- **README.md** – Dokumentacija za pokretanje aplikacije na Linux i Windows operativnim sustavima.

## Pokretanje na Linux OS-u

1. **Izgradite Docker sliku:**
   ```bash
   docker build -t gui-aplikacija .
   ```

2. **Pokrenite aplikaciju:**
   ```bash
   docker run -it --rm -e DISPLAY=$DISPLAY gui-aplikacija
   ```

3. **Provjerite X11:**
   - Osigurajte da je X11 server pokrenut na vašem Linux sustavu.
   - Provjerite da je `DISPLAY` varijabla ispravno postavljena.

### Kako postaviti $DISPLAY varijablu na Linux-u

1. **Provjerite trenutnu vrijednost $DISPLAY:**
   ```bash
   echo $DISPLAY
   ```
   Obično će vrijednost biti nešto poput `:0` ili `localhost:10.0`.

2. **Postavite $DISPLAY varijablu:**
   Ako `$DISPLAY` nije postavljen ili želite promijeniti njegovu vrijednost, koristite:
   ```bash
   export DISPLAY=:0
   ```
   Ovo postavlja `$DISPLAY` na prvi ekran (defaultni ekran).

3. **Provjerite X11 server:**
   - Osigurajte da je X11 server pokrenut na vašem sustavu.
   - Na Ubuntu-u, možete pokrenuti X11 server pomoću:
     ```bash
     sudo service lightdm start
     ```
   - Ako koristite SSH s X11 forwardingom, pokrenite:
     ```bash
     ssh -X user@remote_host
     ```

4. **Testirajte GUI aplikaciju:**
   Pokrenite GUI aplikaciju unutar terminala i provjerite prikazuje li se na ekranu:
   ```bash
   xeyes
   ```
   Ako se aplikacija pokrene i prikaže, `$DISPLAY` je ispravno postavljen.

5. **Postavljanje $DISPLAY u Docker-u:**
   Ako koristite Docker, proslijedite `$DISPLAY` varijablu prilikom pokretanja kontejnera:
   ```bash
   docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix gui-aplikacija
   ```

Ovo omogućuje GUI aplikaciji unutar Docker kontejnera da koristi vaš X11 server za prikaz.

## Pokretanje na Windows OS-u

1. **Instalirajte VcXsrv Windows X Server:**
   - Preuzmite i instalirajte [VcXsrv](https://sourceforge.net/projects/vcxsrv/).

2. **Pokrenite VcXsrv:**
   - Pokrenite VcXsrv s opcijom "Disable access control".

3. **Izgradite Docker sliku:**
   ```powershell
   docker build -t gui-aplikacija .
   ```

4. **Pokrenite aplikaciju:**
   ```powershell
   docker run -it --rm -e DISPLAY=host.docker.internal:0 gui-aplikacija
   ```

5. **Provjerite:**
   - Osigurajte da je VcXsrv pokrenut i da aplikacija koristi ispravan `DISPLAY`.

## Napomene

- Aplikacija koristi PyQt6 i zahtijeva X11 server za prikaz GUI-a.
- Na Windows sustavu, koristite VcXsrv za X11 forwarding.
- Na Linux sustavu, osigurajte da je X11 server pokrenut i da `DISPLAY` varijabla pokazuje na ispravan ekran.

---
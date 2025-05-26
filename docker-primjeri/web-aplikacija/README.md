# Web Aplikacija (Flask)

Ovaj direktorij sadrži Flask web aplikaciju, koja se pokreće korištenjem Docker Compose.

## Sadržaj

- **flask-app/** – Sadrži kod Flask aplikacije, uključujući `app.py`, Dockerfile, te mape `static` i `templates`.
- **docker-compose.yml** – Konfiguracijska datoteka za pokretanje Flask aplikacije kao Docker servisa.
- **secrets/** – Sadrži tajne datoteke (npr. `pgadmin_default_password.txt`).

## Pokretanje

1. Otvori PowerShell u direktoriju `docker-primjeri\web-aplikacija`.
2. Pokreni servise:
   ```powershell
   docker-compose up -d
   ```
3. Aplikacija će biti dostupna na [http://localhost:15000](http://localhost:15000).

## Konfiguracija

- Parametri okoline se definiraju u `.env` datoteci.
- Podaci za vezu s bazom se preuzimaju iz varijabli definiranih u `.env` datoteci.

## Razvoj

- Za lokalno testiranje, pokrenite Flask aplikaciju direktno unutar kontejnera.
- Za dodavanje novih značajki, uredite datoteke unutar `flask-app/app/` direktorija.

## Napomene

- Flask aplikacija i baza podataka koriste zajedničku mrežu **shared-net** kako bi se omogućila međusobna komunikacija.
- Prije pokretanja servisa, osigurajte da je mreža kreirana:
  ```powershell
  docker network create shared-net
  ```
- Provjerite da `.env` datoteka sadrži ispravne parametre za vezu s bazom podataka:
  ```env
  POSTGRES_HOST=baza-podataka
  POSTGRES_PORT=5432
  ```

- Za više informacija o Docker Compose konfiguraciji, pogledajte [dokumentaciju za Docker Compose](https://docs.docker.com/compose/).

---

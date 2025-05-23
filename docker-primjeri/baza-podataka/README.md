# Baza Podataka (Primjer s Docker Compose)

Ovaj direktorij sadrži primjer korištenja Docker Compose za pokretanje baze podataka u Docker kontejneru.

## Sadržaj

- `docker-compose.yaml` – Konfiguracijska datoteka za pokretanje baze podataka kao servisa.

## Opis `docker-compose.yaml`

Ova datoteka definira servise potrebne za pokretanje baze podataka. Tipično uključuje:

- **image**: Određuje koju bazu podataka koristi (npr. `mysql`, `postgres`, `mariadb` itd.).
- **environment**: Postavlja varijable okoline kao što su korisničko ime, lozinka i naziv baze.
- **ports**: Mapira portove kontejnera na portove host računala, omogućujući pristup bazi izvana.
- **volumes**: Omogućuje trajno spremanje podataka baze izvan kontejnera.

Primjer (za MySQL):
```yaml
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: mydb
      MYSQL_USER: user
      MYSQL_PASSWORD: pass
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

## Pokretanje baze podataka

1. Iz direktorija `baza-podataka` pokrenite:
   ```powershell
   docker-compose up -d
   ```
2. Baza podataka bit će dostupna na portu navedenom u `docker-compose.yaml` (npr. 3306 za MySQL).

## Napomena

- Prilagodite varijable okoline prema vlastitim potrebama.
- Za više informacija o podržanim opcijama pogledajte [dokumentaciju za Docker Compose](https://docs.docker.com/compose/).

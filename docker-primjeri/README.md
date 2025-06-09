# Docker Primjeri

Ovaj direktorij sadrži primjere korištenja Docker-a za različite aplikacije i servise.

## Sadržaj

- **baza-podataka/**
  - Primjer konfiguracije baze podataka koristeći Docker Compose.
  - Koristi PostgreSQL kao bazu podataka.

- **jednostavna-terminal-aplikacija/**
  - Terminalska aplikacija za transformaciju teksta.
  - Pokreće se unutar Docker kontejnera.

- **web-aplikacija/**
  - Web aplikacija bazirana na Flask-u.
  - Koristi PostgreSQL bazu podataka i Docker Compose za orkestraciju.

- **gui-aplikacija/**
  - GUI aplikacija bazirana na PyQt6.
  - Pokreće se unutar Docker kontejnera s podrškom za X11.

## Pokretanje

Za pokretanje pojedinih aplikacija, pogledajte README datoteke unutar odgovarajućih direktorija.

## Napomene

- Osigurajte da je Docker instaliran na vašem sustavu.
- Za aplikacije koje koriste mrežu, osigurajte da je mreža kreirana:
  ```powershell
  docker network create shared-net
  ```
- Za GUI aplikacije, osigurajte da je X11 server pokrenut (na Linux-u) ili koristite VcXsrv na Windows-u.

---
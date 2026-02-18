# Jednostavna Terminal Aplikacija (Python + Docker)

Ovaj projekt prikazuje kako pokrenuti jednostavnu Python terminal aplikaciju za transformaciju teksta koristeći Docker i Docker Compose.

## Sadržaj

- `python-terminal-app/app.py` – Python skripta za transformaciju teksta s podrškom za argumente komandne linije.
- `python-terminal-app/requirements.txt` – popis Python ovisnosti.
- `python-terminal-app/Dockerfile` – Dockerfile za izgradnju slike.
- `docker-compose.yml` – Docker Compose konfiguracija za pokretanje servisa.

## Pokretanje

1. **Izgradite i pokrenite servis:**
   ```powershell
   docker-compose up -d
   ```

2. **Spojite se na terminal kontejnera:**
   ```powershell
   docker exec -it python-terminal-app sh
   ```

3. **Pokrenite aplikaciju unutar kontejnera:**
   ```powershell
   python app.py "Vaš tekst ovdje" --upper --reverse
   ```

## Primjeri korištenja

- Pretvori tekst u velika slova:
  ```powershell
  python app.py "Hello World" --upper
  ```
- Obrni tekst:
  ```powershell
  python app.py "Hello World" --reverse
  ```
- Broj riječi (koristi textstat):
  ```powershell
  python app.py "Hello World" --wordcount
  ```

## Napomena

- Za dodatne opcije pogledajte `--help`:
  ```powershell
  python app.py --help
  ```

## Ovisnosti

- [textstat](https://pypi.org/project/textstat/) (instalira se automatski kroz Dockerfile)

---

# Ubuntu Core - Jednostavna Terminal Aplikacija

Ovaj dokument opisuje korake za izradu, konfiguraciju i korištenje Ubuntu Core imagea za jednostavnu terminalsku aplikaciju.

## Opis projekta
Ubuntu Core je minimalna verzija Ubuntu operativnog sustava dizajnirana za IoT uređaje i embedded sustave. Ovaj projekt koristi Ubuntu Core za pokretanje jednostavne terminalske aplikacije na uređajima poput Raspberry Pi-a.

## Preduvjeti
Prije nego što započnete, provjerite imate li sljedeće:

- Instaliran `ubuntu-image` alat
- Raspberry Pi ili drugi kompatibilni uređaj
- SD kartica s minimalno 4 GB prostora
- Monitor, tipkovnica i mrežni kabel (za početnu konfiguraciju uređaja)
- Jednostavna terminal aplikacija iz Snap primjera mora biti buildana za Raspberry Pi 5 (arm64 arhitektura) ([upute i opis aplikacije](../../snap-primjeri/jednostavna-terminal-aplikacija/README.md))

## Generiranje Ubuntu Core imagea

1. Pripremite model datoteku (npr. `jednostavna-terminal-apliakcija.json`) koja definira komponente Ubuntu Core imagea.

2. Potpišite model datoteku koristeći Snapcraft ključ:
   ```bash
   snap sign -k <naziv-kljuca> jednostavna-terminal-apliakcija.json > jednostavna-terminal-apliakcija.model
   ```

3. Generirajte Ubuntu Core image koristeći potpisani model. Ako želite uključiti vlastitu snap aplikaciju u image, provjerite je li definirana u model datoteci unutar sekcije `snaps`. Primjer unosa za vlastitu snap aplikaciju:
   ```json
   "snaps": [
     {
       "name": "jednostavna-terminal-apliakcija",
       "type": "app",
       "default-channel": "stable",
       "file": "path/to/your-snap-file.snap"
     }
   ]
   ```
   Nakon što ste osigurali da je vaša snap aplikacija uključena u model datoteku, pokrenite sljedeću naredbu za generiranje imagea:
   ```bash
   ubuntu-image snap --allow-snapd-kernel-mismatch jednostavna-terminal-apliakcija.model
   ```

   **Alternativa:** Umjesto izmjene model datoteke, snap aplikaciju možete dodati izravno prilikom generiranja Ubuntu Core imagea koristeći opciju `--snap`:
   ```bash
   ubuntu-image snap --allow-snapd-kernel-mismatch jednostavna-terminal-apliakcija.model --snap path/to/your-snap-file.snap
   ```
   Zamijenite `path/to/your-snap-file.snap` s točnom putanjom do vaše snap datoteke.

4. Rezultat će biti `.img` datoteka spremna za zapisivanje na SD karticu.

## Zapisivanje imagea na SD karticu

1. Pronađite naziv uređaja SD kartice na vašem sustavu.
2. Zapišite `.img` datoteku na SD karticu koristeći odgovarajući alat.
3. Alternativno, koristite alate poput Raspberry Pi Imager-a ili balenaEtcher-a za zapisivanje imagea na SD karticu.

## Pokretanje na uređaju

1. Umetnite SD karticu u uređaj.
2. Spojite uređaj na monitor i tipkovnicu.
3. Uključite uređaj i pratite upute na ekranu za inicijalnu konfiguraciju.
4. Spojite se preko ssh-a na uređaj.
5. Pokrenite snap aplikaciju "jednostavna-terminal-apliakcija" s opcijom za pomoć:
   ```bash
   jednostavna-terminal-apliakcija -h
   ```

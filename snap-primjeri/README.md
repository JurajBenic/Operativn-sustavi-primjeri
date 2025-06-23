# Snap Primjeri

Ovaj direktorij sadrži primjere za kreiranje Snap paketa.

## Potrebni Programi

Za kreiranje Snap paketa, potrebno je instalirati sljedeće programe:

1. **Snapcraft**
   - Instalirajte Snapcraft alat za kreiranje Snap paketa:
     ```bash
     sudo snap install snapcraft --classic
     ```

2. **Multipass** (opcionalno)
   - Multipass se koristi za pokretanje virtualnih mašina koje Snapcraft koristi za izgradnju paketa:
     ```bash
     sudo snap install multipass
     ```

3. **LXD** (alternativa Multipass-u)
   - LXD se može koristiti umjesto Multipass-a:
     ```bash
     sudo snap install lxd
     ```

## Kreiranje Snap Paketa

1. **Postavite Snapcraft projekt:**
   - Kreirajte datoteku `snapcraft.yaml` u korijenskom direktoriju projekta.

2. **Izgradite Snap paket:**
   ```bash
   snapcraft
   ```

3. **Testirajte Snap paket:**
   - Instalirajte izgrađeni Snap paket:
     ```bash
     sudo snap install <ime-paketa>.snap --dangerous
     ```

4. **Objavite Snap paket:**
   - Objavite paket na Snap Store-u koristeći Snapcraft.

## Napomene

- Snapcraft zahtijeva Ubuntu ili sličan Linux sustav za izgradnju Snap paketa.
- Multipass ili LXD su potrebni za izolirano okruženje izgradnje.

---
# Raspberry Pi "Universal" gadget snap

Ovaj sadržaj je preuzet s Git repozitorija:
https://github.com/snapcore/pi-gadget

Promjene u odnosu na original:
- Particije su povećane u [gadget.yaml](gadget.yaml) (volumes -> pi -> structure).

Povećane particije i svrha:
- ubuntu-seed (system-seed, vfat, size: 2200M) — sadrži seed snapove i početne boot datoteke.
- ubuntu-boot (system-boot, vfat, size: 1500M) — boot datoteke i kernel.
- ubuntu-save (system-save, ext4, size: 32M) — podatci za oporavak i state.
- ubuntu-data (system-data, ext4, size: 1500M) — korisnički podaci i instalirani snapovi.

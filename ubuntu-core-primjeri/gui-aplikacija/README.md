# GUI aplikacija (Ubuntu Core + Ubuntu Frame)

Ovaj direktorij sadrži primjer Qt6 GUI aplikacije i pripadajuću infrastrukturu
za Ubuntu Core na Raspberry Pi.

## Zašto koristimo vlastiti Pi gadget

Pi gadget koristimo kako bismo povećali particije i prilagodili boot
konfiguraciju za Ubuntu Core na Raspberry Pi. Više detalja je u
[pi-gadget/README.md](pi-gadget/README.md). To je nužno kako bi sustav imao:

- ispravno particioniranje (seed/boot/save/data),
- dovoljno prostora za snapove i podatke,
- kompatibilno bootanje na ciljnom hardveru.

## Zašto koristimo Qt6 GUI app

Qt6 GUI app služi kao primjer grafičke aplikacije u Snap formatu. Pokreće se
na Waylandu preko Ubuntu Frame, što je standardni grafički kiosk/embedded
stack na Ubuntu Core.
Za više detalja vidi [qt6-gui/README.md](qt6-gui/README.md)

## Izrada img datoteke

Za izradu Ubuntu Core image‑a koristi se `ubuntu-image` i model iz
[gui-app.json](gui-app.json):

```
ubuntu-image snap --allow-snapd-kernel-mismatch gui-app.model --snap pi_24-3_rpi-amd64.snap --snap qt6-gui_0.1_arm64.snap
```

## Pokretanje aplikacije na Ubuntu Core
Nakon što se uređaj podigne, ulogiraj se preko SSH i konfiguriraj:
```
ssh korisnik@IP_uredaja
```

### Spajanje qt6-gui s Ubuntu Frame
Poveži potrebne plugove:
```
snap connect qt6-gui:wayland ubuntu-frame:wayland
snap connect qt6-gui:opengl
snap connect qt6-gui:gpu-2404 mesa-2404:gpu-2404
```

### Autostart
```
snap set qt6-gui daemon=true
snap set ubuntu-frame daemon=true
```

## Journal (logovi)

Logove snap servisa možeš provjeriti preko `journalctl`:

```
sudo journalctl -u snap.qt6-gui.daemon -f
sudo journalctl -u snap.ubuntu-frame.daemon -f
```

# Debug

1) Instaliraj Ubuntu Core na Raspberry Pi (arm64).
2) Buildaj snap na arm64 (Raspberry Pi) kako bi snap bio ispravne arhitekture; najbolje je koristiti Raspberry Pi OS.
3) Prebaci snap na uređaj preko `scp`:

```
scp qt6-gui_0.1_arm64.snap korisnik@IP_uredaja:/home/korsnik/
```

4) Instaliraj snap na uređaju:

```
snap install /home/korsnik/qt6-gui_0.1_arm64.snap --dangerous
```

Ovo omogućuje brzo testiranje na pravom Ubuntu Core okruženju.

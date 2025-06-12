# Jednostavna Terminal Aplikacija

Ova aplikacija je jednostavna terminalska aplikacija napisana u Pythonu. Služi kao primjer za izradu i pakiranje terminalskih aplikacija pomoću Snapcraft alata.

## Značajke
- Osnovna interakcija putem terminala
- Lako proširiva dodatnim funkcionalnostima

## Instalacija

### Preduvjeti
- Instaliran Snapcraft alat
- Python 3.10 ili noviji

### Koraci
1. Klonirajte repozitorij:
   ```bash
   git clone <URL>
   cd snap-primjeri/jednostavna-terminal-aplikacija
   ```
2. Izgradite snap paket:
   ```bash
   snapcraft
   ```
3. Instalirajte snap paket:
   ```bash
   sudo snap install jednostavna-terminal-aplikacija_0.1_amd64.snap --devmode
   ```

## Korištenje
Pokrenite aplikaciju pomoću naredbe:
```bash
jednostavna-terminal-aplikacija
```

## Razvoj

### Postavljanje Razvojnog Okruženja
1. Kreirajte virtualno okruženje:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instalirajte ovisnosti:
   ```bash
   pip install -r requirements.txt
   ```

### Alternativa: Korištenje Conda okruženja
1. Kreirajte Conda okruženje:
   ```bash
   conda create --name myenv python=3.10
   conda activate myenv
   ```
2. Instalirajte ovisnosti:
   ```bash
   pip install -r requirements.txt
   ```

### Pokretanje Aplikacije
Pokrenite aplikaciju lokalno:
```bash
python3 src/app.py
```

### Alternativa: Pokretanje s Conda okruženjem
Pokrenite aplikaciju unutar aktiviranog Conda okruženja:
```bash
conda activate myenv
python src/app.py
```

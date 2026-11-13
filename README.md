# Programmering – kode fra undervisningen 🚀

Her ligger all koden vi har skrevet sammen i timene (live-koding). Mappene er nummerert
i den rekkefølgen det er lurt å gå gjennom dem – hvert tema bygger på det forrige.

Koden er skrevet *live* i klasserommet. Det betyr at den ikke alltid er «perfekt»:
noen steder er det kommentert ut kode, og noen steder er det feil med vilje (eller ved et uhell 😅).
Prøv å finne og forstå dem – det er god trening!

---

## Innhold

| # | Mappe | Tema | Filer |
|---|-------|------|-------|
| 1 | [`01_grunnleggende`](01_grunnleggende) | Variabler, `if`, funksjoner, lister og ordbøker | `hello_world.py`, `funksjoner.py`, `lister.py` |
| 2 | [`02_moduler`](02_moduler) | Importere moduler (`random`, `math`) og lage egne | `forsteModul.py`, `main.py`, `romskipModul…py` |
| 3 | [`03_filer_og_feilhandtering`](03_filer_og_feilhandtering) | Lese og skrive filer, kjøre fra terminalen, `try`/`except` | `romskip_enkel.py`, `romskip_med_funksjoner.py`, `planetData.py`, `galakseData.py` |
| 4 | [`04_objektorientert_programmering`](04_objektorientert_programmering) | Klasser, objekter og arv | `uten_oop.py`, `forste_klasse.py` |
| 5 | [`05_testing`](05_testing) | Automatisk testing med `pytest` | `romfart.py`, `test_romfart.py` |

---

## 1. Grunnleggende

Gå gjennom filene i denne rekkefølgen:

### `hello_world.py`
- Lage en variabel: `answer_of_life = 41`
- En enkel `if`-setning

💡 *Oppgave:* Se på `if 43:` – hva skjer egentlig her? Hvorfor skrives «Correct» ut uansett?
Hvordan skulle det vært skrevet hvis vi ville sjekke verdien til variabelen?

### `funksjoner.py`
- Lage egne funksjoner med `def` og parametere
- Forskjellen på å `print`-e og å `return`-e en verdi
- `if` / `elif` / `else` inne i en funksjon (`vurder_temperatur`)

💡 *Oppgave:* `beregn_avstand` returnerer alltid `67`. Hva er feil, og hvordan fikser du det?

### `lister.py`
- Lage en liste og legge til/fjerne elementer: `append`, `insert`, `remove`, `pop`
- Endre et element: `solsytem[2] = "Terra"`
- `len()` og `for`-løkker, også med `enumerate`
- Tupler: `(3, 10, 19)`
- Ordbøker (dictionary): `mars["antMaaner"]`

---

## 2. Moduler

### `forsteModul.py`
Bruke ferdige moduler fra Python:
```python
from random import randint, choice
from math import sqrt
```

### `romskipModulSomRegnerUtDrivstoffOgAvstand.py` + `main.py`
Lage vår *egen* modul og importere den i en annen fil:
```python
import romskipModulSomRegnerUtDrivstoffOgAvstand as r
print(r.beregn_drivstoff(1999, 100))
```
Kjør `main.py` – ikke modulfilen.

---

## 3. Filer og feilhåndtering

Gå gjennom filene i denne rekkefølgen:

### `romskip_enkel.py` – lese fra fil
Leser drivstoffnivået fra `drivstoff.txt`.
- `open()`, `read()` og `close()`
- Gjøre tekst om til tall med `int()`
- Bestemme hva som skjer med `if`/`else`

### `romskip_med_funksjoner.py` – samme program, ryddet opp
- Samme program som over, men delt opp i funksjoner (`les_drivstoff`, `vurder_drivstoff`)
- Kjørt fra terminalen:
  ```bash
  cd 03_filer_og_feilhandtering
  python romskip_med_funksjoner.py
  ```

💡 *Prøv:* Endre tallet i `drivstoff.txt` og kjør begge programmene på nytt.

### `planetData.py` – skrive til fil
- Skrive til fil (`"w"` = overskriv, `"a"` = legg til) og lese fra fil (`"r"`)
- `with open(...) as fil:` – lukker filen automatisk
- Lese en fil linje for linje med `.strip()`

### `galakseData.py` – feilhåndtering
- `try` / `except FileNotFoundError` – når filen ikke finnes
- `try` / `except ValueError` / `else` – når brukeren ikke skriver et gyldig tall

💡 *Oppgave:* Filbanene i `planetData.py` og `galakseData.py` peker på en mappe som heter
`filOperasjoner/`. Finnes den? Hva må du endre for at programmene skal fungere?
Og hva er galt med `print(fil.read)`?

---

## 4. Objektorientert programmering (OOP)

### `uten_oop.py`
Slik blir det når vi har mange personer *uten* klasser – mange løse variabler.

### `forste_klasse.py`
Samme idé *med* klasser:
- `class Menneske` med `__init__` og `self`
- Metoder: `presenter()`, `bliEldre()`, `jobb()`
- **Arv:** `Laerer`, `Pilot` og `Elev` arver fra `Menneske`
- `super().__init__(...)` for å gjenbruke konstruktøren
- Overstyre metoder (`jobb()` gjør noe forskjellig for hver klasse)
- Gå gjennom en liste med objekter og kalle samme metode på alle

---

## 5. Testing

`romfart.py` inneholder funksjonene, `test_romfart.py` inneholder testene.

- `assert` – sjekke at noe er sant
- `@pytest.mark.parametrize` – kjøre samme test med mange forskjellige verdier
- `pytest.raises(ValueError)` – teste at en feil faktisk blir kastet
- `pytest.approx` – sammenligne desimaltall (`0.1 + 0.2` er ikke helt `0.3`!)

Kjør testene slik:
```bash
pip install pytest
cd 05_testing
pytest
```

---

## Slik kjører du koden

1. Åpne mappen i VS Code.
2. Åpne terminalen (*Terminal → New Terminal*).
3. **Gå inn i mappen til temaet først** – flere av programmene leser filer (som `drivstoff.txt`)
   eller importerer andre filer, og finner dem bare hvis du står i riktig mappe:
   ```bash
   cd 03_filer_og_feilhandtering
   python romskip_enkel.py
   ```

## Tips
- Les koden **før** du kjører den – prøv å gjette hva som skrives ut.
- Endre litt på koden og se hva som skjer. Du kan ikke ødelegge noe!
- Får du en feilmelding? Les den nederste linjen først – der står det som oftest hva som er galt.

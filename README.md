# BTS4210-1_26H-Data-Mining-and-Analytics

Kode til BTS4210 ved USN. Notater, pensum og framgangsmåte ligger i vaulten:
`~/Documents/Master_brain/03_courses/2026-H/BTS4210-1_26H-Data-Mining-and-Analytics/`.
Dette repoet inneholder kode, ikke prosa.

## Hvem har skrevet hva

**Ikke alt her er mitt.** Det er hele poenget med mappedelingen: 1. september fikk jeg
LEOs løsning på to forkursoppgaver, og fram til 15. september var den limt inn i mine
egne filer uten at noe sa fra. Da leste repoet som om jeg hadde løst dem.

| Mappe | Opphav | Hva det er |
|---|---|---|
| `min/forkurs/` | **meg** | Kapittel 9 hos Haugen — numpy og filer, oppgave 9.1–9.10 |
| `min/forkurs-pandas/` | **meg** | Kapittel 10 hos Haugen — Pandas, oppgave 10.1–10.8 |
| `min/oblig-00/` | **meg** | Oblig#0. `data/` er utdelt, koden blir min |
| `samling/` | meg, etter LEOs skjerm | Skrevet av i timen mens han kodet foran klassen |
| `laerer/` | Lars Erik Opdal (LEO) | Utdelte filer og løsninger, urørt |

Skillet mellom `min/` og `samling/` er ikke pedantisk. Å taste av en skjerm er ikke det
samme som å løse noe selv, men det er heller ikke en utdelt fil — og begge deler er verdt å
ha. En tredje bøtte var billigere enn å tvinge sju filer inn et sted de ikke hørte hjemme.

**Regelen for `laerer/`:** filene der er slik de ble delt ut. Endrer jeg noe, skal det stå
som en kommentar i fila. Samme regel som i BTS4410-repoet.

## Headeren sier det samme

Mappa svarer på hvem som eier koden. Headeren svarer på hva *denne* fila er:

```
Opphav   : min egen | avskrift i timen | LEO (Lars Erik Opdal), urørt | BLANDET
Status   : hva som faktisk er gjort
Original : sti til LEOs fil, når min er en kopi eller en variant
```

`@author`-feltet fra Spyder er fjernet. Det sto `mine` på **alle** filer her, også de to som
inneholdt LEOs kode, fordi Spyder stempler inn det lokale brukernavnet når fila lages. Det
er det første du ser når du åpner ei fil, og det var feil. LEOs egne filer kom med
`@author: lopda` — det var beviset som avgjorde opphavet.

## To filer er blandet med vilje

`min/forkurs/09_03-…py` og `min/forkurs/09_09-kanonkule.py` inneholder **begge** LEOs kode.
De er ikke delt opp, etter eget valg: originalen ligger uansett i `laerer/forkurs/`, så
ingenting går tapt ved å la kopien bli stående — men headeren sier hvilken blokk som er hvem
sin, og peker på originalen.

- `09_03` har mitt eget utkast utkommentert øverst. Det stopper på en parentesfeil i
  `np.savetxt` — alle argumentene er pakket i én tuppel, som gir `SyntaxError`. Feilen står
  urettet med vilje.
- `09_09` har ingenting fra meg. Plassholderen `min egen løsning:` nederst er tom.

## To ting i `laerer/` er fasit, ikke oppgavestoff

`laerer/forkurs/` inneholder **løsninger**, ikke bare utdelt materiale:

- `oppg9_5.py` — LEOs løsning på 9.5, en oppgave jeg ikke har rørt. To løsninger i én fil.
- `oppg9_9._2026V2py.py` — LEOs løsning på 9.9.
- `dager.xlsx` — LEOs *resultat* av oppgave 10.7, ikke inndata. Kolonnen `Temp` har
  verdiene 2, 5, 3, 4, 8 med index `dag1`–`dag5`, som er nøyaktig det oppgaven ber om.
  Oppgaven sier fila skal hete `temp_april.xlsx`; hans heter noe annet.

**Les dem etter at du har prøvd selv, ikke før.**

## To ting kan ikke kjøres

| Fil | Problem |
|---|---|
| `laerer/forkurs/oppg9_5.py` | `dyrebestand.txt` finnes ikke lokalt |
| `laerer/samling-01/Del1_matplotlib.py` | `somedata.csv` finnes, men **passer ikke koden** |

`somedata.csv` kom inn 2026-09-15. Skriptet gjør `pd.read_csv("./somedata.csv",
index_col="x")`, og det gir `ValueError: Index x invalid`. Fila er semikolonseparert og har
to headerrader — `Column1;Column2;Column3` først, så `x;s;c`. Den leses med
`sep=";", skiprows=1`. Enten er CSV-en eksportert annerledes enn da skriptet ble skrevet,
eller så hører de to ikke sammen. **Ikke rettet** — filene i `laerer/` står som de kom.

## Miljø

```
conda env create -f environment.yml
conda activate bts4210
```

`bts4210` har pandas, numpy, matplotlib, scikit-learn, openpyxl og JupyterLab. Start
JupyterLab fra selve miljøet — base har ingen kernel registrert for `bts4210`:

```
/opt/anaconda3/envs/bts4210/bin/jupyter lab
```

Skriptene leser og skriver i arbeidskatalogen, så **kjør dem fra sin egen mappe**.

Datafilene til Oblig#0 ligger i `min/oblig-00/data/` — 16 MB, committet med vilje så ZIP-en
til innlevering kan bygges på nytt og dataene overlever at Canvas-lenka forsvinner.
Skilletegnene er blandet: `nor_population2022.csv` er semikolonseparert og trenger
`sep=";"`, resten er komma. `laerer/data/nor_population2024.csv` er **ikke** en del av
oppgaven — den er nyere data med annen struktur (`år` mot `ar`, og Østfold mot Viken etter
fylkesreformen), og ligger utenfor leveransen med vilje.
Genererte utdata er gitignorert på filnavn, ikke på sti, nettopp fordi mappene ble lagt om.

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
| `min/oblig0_289412/` | **meg** | Oblig#0, innleveringsmappa. `data/` er utdelt, koden er min |
| `min/Øvelse_1_statistikk/` | **meg** | Øvelse 1, samling 2. Løst som fem `.py` framfor i notebooken; `Data/tips.csv` er kopi av den utdelte, samme `shasum` |
| `min/samling/` | meg, etter forelesers skjerm | Skrevet av i timen mens foreleser kodet foran klassen |
| `laerer/` | LEO og Singstad, se regelen nedenfor | Utdelte filer og løsninger, urørt |
| `laerer/samling-02/` | Bjørn-Jostein Singstad (`Bsingstad`) | Statistikk-notebooks og data, samling 2, urørt |

Skillet mellom egen løsning og avskrift er ikke pedantisk. Å taste av en skjerm er ikke det
samme som å løse noe selv, men det er heller ikke en utdelt fil. Fram til 28. september lå
`samling/` derfor som en tredje bøtte ved siden av `min/` og `laerer/`.

Nå ligger den under `min/`, og mappegrensen svarer bare på ett spørsmål: ble fila delt ut,
eller ikke. Nyansen er ikke tapt — alle sju filene i `min/samling/` har
`Opphav : avskrift i timen` i headeren. Den leses nå per fil i stedet for per mappe.

**Regelen for `laerer/`:** filene der er slik de ble delt ut, uansett hvem som delte dem ut.
`forkurs/`, `data/` og `samling-01/` er LEOs; `samling-02/` er Singstads. Endrer jeg noe, skal
det stå som en kommentar i fila. Samme regel som i BTS4410-repoet.

Notebookene i `samling-02/` har **ingen `Opphav:`-header**, i motsetning til `.py`-filene i
`samling-01/`. Det er et bevisst avvik: en header i en `.ipynb` betyr en ny markdown-celle,
altså en endring av fila. Lar jeg dem være byte-identiske med GitHub, kan opphavet *bevises*
i stedet for å påstås:

```
BASE=https://raw.githubusercontent.com/Bsingstad/BTS4210-H-ST2026/main/Samling_2_dag_1
curl -sf "$BASE/kode/02_utvalg.ipynb" | shasum
shasum laerer/samling-02/kode/02_utvalg.ipynb
```

Samme sum = urørt. Filene er lastet ned enkeltvis med `curl` 2026-09-28, ikke klonet — en
klone la sin egen `.git` inni dette repoet og gjorde at mine egne filer lå usporet i en repo
jeg ikke eide.

## Headeren sier det samme

Mappa svarer på hvem som eier koden. Headeren svarer på hva *denne* fila er:

```
Opphav   : min egen | avskrift i timen | <foreleser>, urørt | BLANDET
           <foreleser> er LEO (Lars Erik Opdal) eller Singstad (Bjørn-Jostein Singstad)
Status   : hva som faktisk er gjort
Original : sti til forelesers fil, når min er en kopi eller en variant
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

`bts4210` har pandas, numpy, matplotlib, scipy, scikit-learn, seaborn, statsmodels,
openpyxl, Spyder og JupyterLab — lista står i `environment.yml`, som er kilden. Start
JupyterLab fra selve miljøet — base har ingen kernel registrert for `bts4210`:

```
/opt/anaconda3/envs/bts4210/bin/jupyter lab
```

Skriptene leser og skriver i arbeidskatalogen, så **kjør dem fra sin egen mappe**.

Notebookene i `laerer/samling-02/` er ett unntak verdt å kjenne: de leser
`pd.read_csv("../Data/penguins.csv")`, altså **ett nivå opp**. Derfor må `Data/`, `kode/` og
`øvinger/` ligge side om side slik de gjør — flytter jeg en notebook, slutter den å finne
dataene. Lager jeg egen kode under `min/samling/dag-03/`, kan den lese de samme filene på
tvers med `../../../laerer/samling-02/Data/` — **tre** nivåer opp, ikke to, etter at
`samling/` flyttet inn under `min/` 28. september — i stedet for at csv-ene ligger to steder.

Datafilene til Oblig#0 ligger i `min/oblig0_289412/data/` — 16 MB, committet med vilje så
ZIP-en til innlevering kan bygges på nytt og dataene overlever at Canvas-lenka forsvinner.
Skilletegnene er blandet: `nor_population2022.csv` er semikolonseparert og trenger
`sep=";"`, resten er komma. `laerer/data/nor_population2024.csv` er **ikke** en del av
oppgaven — den er nyere data med annen struktur (`år` mot `ar`, og Østfold mot Viken etter
fylkesreformen), og ligger utenfor leveransen med vilje.
Genererte utdata er gitignorert på filnavn, ikke på sti, nettopp fordi mappene ble lagt om.

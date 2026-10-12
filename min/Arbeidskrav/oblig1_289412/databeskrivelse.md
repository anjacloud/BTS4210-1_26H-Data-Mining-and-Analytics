# Databeskrivelse: hjerte_ekg_data.csv

En rad = én besøk på akuttmottaket med minst ett EKG. 

| Kolonne | Beskrivelse |
|---|---|
| `pasient_id` | Anonymisert pasient-ID. Én pasient kan ha flere rader (flere opphold). |
| `opphold_id` | Anonymisert ID for akuttmottak-oppholdet. |
| `age_at_admit` | Alder ved innleggelse (år). |
| `sex` | Kjønn (`Male`/`Female`), kan mangle. |
| `race` | Selvrapportert rase/etnisitet (`Black`/`Hispanic`/`White`/`Other/unknown`), kan mangle. |
| `pr_interval`, `qrs_duration`, `qt_interval`, `qtc_interval` | EKG-intervaller i millisekunder. |
| `vent_rate` | Hjertefrekvens (slag/minutt) avlest fra EKG-et. |
| `has_st_eleva` | ST-elevasjon (0/1). |
| `has_depress` | ST-depresjon (0/1). |
| `has_twave_inver` | Invertert T-bølge (0/1). |
| `has_twave_abnormal` | Unormal T-bølge (0/1). |
| `has_bbb` | Grenblokk (0/1). |
| `has_lvh` | Venstre ventrikkelhypertrofi (0/1). |
| `has_afib` | Atrieflimmer (0/1). |
| `has_pacemaker` | Pacemakerrytme (0/1). |
| `has_prolonged_qt` | Forlenget QT-tid (0/1). |
| `has_rhythm_disturbance` | Generelt rytmeforstyrrelse-flagg (0/1). |
| `has_normal_ecg` | EKG-apparatet vurderte EKG-et som normalt (0/1). |
| `ami_3d` | **Target.** Fikk pasienten diagnosen hjerteinfarkt innen 3 dager etter oppholdet? (0/1) |
| `maxtrop_sameday` | Høyeste målte troponinverdi samme dag (ng/mL) |
| `stent_or_cabg_010_day` | Fikk pasienten stent eller bypassoperasjon innen 10 dager? (0/1) |
| `macetrop_pos_or_death_030` | Positiv troponinprøve eller død innen 30 dager? (0/1) |



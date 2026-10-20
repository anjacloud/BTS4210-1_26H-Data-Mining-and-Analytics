#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeg diskuterte en del med en AI-model hvordan man løser denne oppgaven på best mulig måte 
uten å miste hode og for å lærer mer hvordan en funksjon bare skal ha en oppgave

@author: 
    studentnummer: 289412

"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from scipy import stats
from sklearn.model_selection import GroupShuffleSplit
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LogisticRegression
from sklearn.base import clone
from sklearn.model_selection import StratifiedGroupKFold, cross_validate
from sklearn.metrics import (make_scorer, recall_score, precision_score, roc_curve,
                             roc_auc_score, average_precision_score, confusion_matrix,
                             ConfusionMatrixDisplay, RocCurveDisplay, PrecisionRecallDisplay)
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.dummy import DummyClassifier



FILEPATH = "hjerte_ekg_data.csv"

# sjekker at stien peker på en fil 
def validate_path(filepath): 
    path = Path(filepath)
    # sjekk at filen(path) eksisterer 
    if not path.is_file():  
        # finnes den ikke: vis stien der Python leter
        raise FileNotFoundError(f"File not found: {path.resolve()}")
    return path

# leser filen
def load_file(filepath): 
    # sjekkes mot om filen finnes
    path = validate_path(filepath)
    # gi tilbake DataFrame (tabell med rader og kolonner)
    return pd.read_csv(path) 

# sjekk at kolonnen finnes, hent den uten tomme verdier
def get_column(df, column):
    # sjekk om denne kolonnen vi trenger finnes
    if column not in df.columns:
        raise KeyError(f"Column not found: {column}. Available: {df.columns}")
    # henter kolonnen med navn vi trenger 
    # fjerner tomme verdier
    return df[column].dropna() 

# skriver ut datatype og antall manglende verdier
def check_column(df, column):
    print(f"Kolonne: {column}")
    print(f"Datatype: {df[column].dtype}")
    print(f"Manglende verdier: {df[column].isna().sum()}")

# histogram av verdiene
def plot_histogram(values, title, xlabel=None, ylabel="antall", bins=30,
                   label=None, density=False, alpha=1.0, show=True):
    if xlabel is None:
        xlabel = values.name
    values.plot(kind="hist", bins=bins, edgecolor="black",
                label=label, density=density, alpha=alpha)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # forklaring (legend) bare når gruppen har et navn
    if label is not None:
        plt.legend()
    # show=False: vent med å vise, så neste gruppe tegnes i samme figur
    if show:
        plt.show()  
        
# skriver en skillelinje med oppgavenavn
def section(title):
    print(f"\n{32 * '*'}  {title}  {32 * '*'}\n")

    
""" DEL 1a """

# tell rader 
def count_rows(df):
    # return antall radene
    return len(df.index)

# teller unike verdier i en kolonne
def count_unique(df, column):
    values = get_column(df, column)
    # hver verdi tas med en gang, selv om den står flere ganger
    unique_values = values.unique() 
    # returnerer antall unike verdier
    return len(unique_values) 


""" DEL 1b """
    
# beskriver hele populasjonen
def describe_population(values,xlabel=None):
    print("\n___Populasjon___")
    print(f"\nAntall: {len(values)}")
    print(f"Gjennomsnitt: {values.mean():.2f}")
    print(f"Standardavvik: {values.std(ddof=0):.2f}")
    # sammendrag: antall, snitt, std, min, kvartiler, maks
    print(values.describe())
    # Histogram med 30 søyler
    plot_histogram(values, "Fordeling (populasjon)", xlabel=xlabel)
    
# trekker ett utvalg og regner ut statistikken
def sample_stats(values, n, random_state=42):
    # trekker n tilfeldige verdier
    # replace=False - hver verdi kan trekkes en gang
    # random_state - samme utvalg hver gang
    sample = values.sample(n=n, replace=False, random_state=random_state)
    # gjennomsnitt
    mean = sample.mean()
    # standardavvik i utvalget
    std = sample.std()
    # standardfeil - sier hvor sikkert gjennomsnittet er 
    se = std / np.sqrt(n)
    return sample, mean, std, se

# trekker ett utvalg for hver størrelse i sizes
def run_samples(values, sizes, xlabel=None): 
    for n in sizes:
        if n > len(values):
            print(f"\nFor få rader til n = {n} (har {len(values)}).")
            continue
        # pakkes ut i samme rekkefølge som return i sample_stats
        sample, mean, std, se = sample_stats(values, n)
        print(f"\n___Utvalg n = {n}___")
        print(f"\nUtvalgsgjennomsnitt: {mean:.2f}")
        print(f"Standardavvik (s): {std:.2f}")
        print(f"Standardfeil (SE): {se:.3f}")
        # Histogram med 25 søyler
        plot_histogram(sample, f"Utvalg n = {n}", bins=25, xlabel=xlabel)


""" DEL 1c """

# teller hvor mange verdier av 0 og 1
def class_balance(values):
    # teller hvor mange ganger hver verdi står i kolonnen
    counts = values.value_counts()
    # samme telling men delt på totalen - andel mellom 0 og 1 
    shares = values.value_counts(normalize=True)
    totalt = len(values)
    print(f"\n___Fordeling av {values.name}___\n")
    # går gjennom hver verdi (0 og 1) og skriver ut antall og andel på samme linje
    for verdi in counts.index:
        print(f"{values.name} = {verdi}: {counts[verdi]} av {totalt} ({shares[verdi]:.2%})")
    return counts, shares

def baseline_accuracy(values, guess=0):
    # lager modellens gjetting (prediksjon) for hver rad - samme svar alltid (0=nei)
    predictions = [guess] * len(values)
    # sammenligner fasit (values) med gjetningene og regner ut andelen riktige 
    return accuracy_score(values, predictions)

""" DEL 2 """
LABELS = ("ami_3d = 1", "ami_3d = 0")

# deler en tallkolonne i to grupper etter en 0/1-kolonne
def split_groups(df, value_col, group_col):
    # sjekk at begge kolonnene finnes
    for column in [value_col, group_col]:
        if column not in df.columns:
            raise KeyError(f"Column not found: {column}. Available: {df.columns}")
    # fjern hele rader der en av kolonnene mangler
    # alder og ami_3d hører til samme opphold, så de må fjernes sammen
    data = df[[value_col, group_col]].dropna()
    # velg radene der gruppen er 1 eller 0, og ta bare verdikolonnen
    ja = data.loc[data[group_col] == 1, value_col]
    nei = data.loc[data[group_col] == 0, value_col]
    return ja, nei

# skriver ut n, gjennomsnitt og standardavvik for hver gruppe
def describe_groups(ja, nei, labels=LABELS):
    print("\n___Grupper___\n")
    for navn, values in zip(labels, [ja, nei]):
        print(f"{navn}: n = {len(values)}, "
              f"gjennomsnitt = {values.mean():.2f}, "
              f"standardavvik = {values.std():.2f}")


# Q-Q-plott: sammenligner verdiene med en normalfordeling
def plot_qq(values, title, ylabel="observerte verdier", ax=None):
    show = ax is None
    if ax is None:
        fig, ax = plt.subplots()
    stats.probplot(values, dist="norm", plot=ax)
    ax.set_title(title)
    ax.set_xlabel("teoretiske kvantiler (normalfordeling)")
    ax.set_ylabel(ylabel)
    if show:
        plt.show()

# Shapiro-Wilk på hele gruppen 
def normality_test(values):
    w, p = stats.shapiro(values)
    return w, p, len(values)

# Welch t-test
def welch_test(ja, nei):
    # equal_var=False gjør det til Welch; regner mean(ja) - mean(nei)
    t, p = stats.ttest_ind(ja, nei, equal_var=False)
    return t, p

# Cohens d - samme formel som i undervisningsmaterialet
def cohens_d(a, b):
    n_a, n_b = len(a), len(b)
    s_pooled = np.sqrt(((n_a - 1) * a.var() + (n_b - 1) * b.var()) / (n_a + n_b - 2))
    return (b.mean() - a.mean()) / s_pooled

""" 
Oppgave 3 og 4: koden er skrevet med AI-hjelp, 
delvis bygd på lærerens kode
"""

""" DEL 3 """

TARGET = "qt_interval"

# kolonner som ikke skal være input i regresjonen
DROP_COLS = [
    "pasient_id", "opphold_id",
    "qtc_interval", "has_prolonged_qt",
    "ami_3d", "maxtrop_sameday", "stent_or_cabg_010_day", "macetrop_pos_or_death_030",]

# rydder data for regresjon: fjerner rader uten target, deler i X, y og grupper
def prepare_regression(df, target=TARGET, drop_cols=DROP_COLS):
    check_column(df, target)
    # fjern bare rader der target mangler 
    data = df.dropna(subset=[target])
    print(f"Rader etter fjerning av manglende {target}: {len(data)} av {len(df)}")
    # y = det vi vil predikere, X = alt annet unntatt kolonnene over
    y = data[target]
    X = data.drop(columns=[target] + drop_cols)
    # grupper = pasient_id, brukes i splitten slik at samme pasient ikke havner begge steder
    groups = data["pasient_id"]
    return X, y, groups

# deler i trening og test slik at hver pasient bare havner på én side
def group_split(X, y, groups, test_size=0.25, random_state=42):
    # én tilfeldig deling (n_splits=1), 25 % av pasientene til test
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    # next(...) henter den ene delingen: radnumrene til trening og test
    train_idx, test_idx = next(splitter.split(X, y, groups=groups))
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    # kontroll: ingen pasient i begge settene
    overlap = set(groups.iloc[train_idx]) & set(groups.iloc[test_idx])
    print(f"Trening: {len(X_train)} rader ({len(X_train) / len(X):.1%}), "
          f"test: {len(X_test)} rader ({len(X_test) / len(X):.1%})")
    print(f"Pasienter i både trening og test: {len(overlap)}")
    return X_train, X_test, y_train, y_test

NUM_COLS = ["age_at_admit", "pr_interval", "qrs_duration", "vent_rate",
            "has_st_eleva", "has_depress", "has_twave_inver", "has_twave_abnormal",
            "has_bbb", "has_lvh", "has_afib", "has_pacemaker",
            "has_rhythm_disturbance", "has_normal_ecg"]
CAT_COLS = ["sex", "race"]


# lager pipeline: forbehandling + modell
def build_pipeline(model, num_cols=NUM_COLS, cat_cols=CAT_COLS):
    prep = ColumnTransformer([
        # tall: fyll hull med median, så skaler (snitt 0, std 1)
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), num_cols),
        # tekst: én 0/1-kolonne per kategori, manglende blir egen kategori
        ("kat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ])
    return Pipeline([("prep", prep), ("modell", model)])


# trener en pipeline på trening og regner R^2 og MAE på test 
def evaluate(pipe, X_train, X_test, y_train, y_test):
    # fit: imputer, skalering og modell lærer bare av treningsdata
    pipe.fit(X_train, y_train)
    # predict: bruker det som ble lært på testdata
    y_pred = pipe.predict(X_test)
    return r2_score(y_test, y_pred), mean_absolute_error(y_test, y_pred)

        
""" DEL 4 """

CLF_TARGET = "ami_3d"

# kolonnene oppgaveteksten sier skal ut (4a)
CLF_DROP_COLS = [
    "maxtrop_sameday", "stent_or_cabg_010_day", "macetrop_pos_or_death_030",
    # ID-er: brukes bare til gruppering
    "pasient_id", "opphold_id"]

# her er qt-kolonnene lov som input (de var target/lekkasje i oppgave 3)
CLF_NUM_COLS = NUM_COLS + ["qt_interval", "qtc_interval", "has_prolonged_qt"]

# deler i X, y og grupper for klassifisering
def prepare_classification(df, target=CLF_TARGET, drop_cols=CLF_DROP_COLS):
    check_column(df, target)
    y = df[target]
    X = df.drop(columns=[target] + drop_cols)
    groups = df["pasient_id"]
    return X, y, groups

SCORING = {
    "nøyaktighet": "accuracy",
    # sensitivitet = andel av de syke (1) som blir funnet
    "sensitivitet": "recall",
    # spesifisitet = andel av de friske (0) som blir funnet -> recall for klasse 0
    "spesifisitet": make_scorer(recall_score, pos_label=0),
    # zero_division=0: gir 0 i stedet for advarsel når modellen ikke sier «ja» en eneste gang
    "presisjon": make_scorer(precision_score, zero_division=0),
    "F1": "f1",
    "AUROC": "roc_auc",
    "AUPRC": "average_precision",
}

METRIC = "AUPRC"

# lager 5 x 5 delinger: 5 folds, gjentatt 5 ganger med ny stokking
# gruppert: samme pasient aldri i både trening og validering
# stratifisert: omtrent like mange ja-tilfeller i hver fold
def repeated_group_splits(X, y, groups, n_splits=5, n_repeats=5):
    splits = []
    for repeat in range(n_repeats):
        cv = StratifiedGroupKFold(n_splits=n_splits, shuffle=True, random_state=repeat)
        splits.extend(cv.split(X, y, groups=groups))
    return splits

# kryssvaliderer hver modell på de samme delingene, gir snitt og SD per metrikk
def compare_models(models, X, y, splits, num_cols=CLF_NUM_COLS):
    scores = {}
    rows = {}
    for navn, modell in models.items():
        result = cross_validate(build_pipeline(modell, num_cols=num_cols), X, y,
                                cv=splits, scoring=SCORING)
        # cross_validate gir nøklene "test_<metrikk>", én verdi per fold 
        scores[navn] = {m: result[f"test_{m}"] for m in SCORING}
        rows[navn] = {m: f"{s.mean():.3f} ± {s.std():.3f}" for m, s in scores[navn].items()}
    return pd.DataFrame(rows).T, scores

# korrigert paret t-test (Nadeau-Bengio) 
def korrigert_ttest(a, b, n_test_over_train):
    d = np.asarray(a) - np.asarray(b)
    J = len(d)
    t = d.mean() / np.sqrt((1 / J + n_test_over_train) * d.var(ddof=1))
    return t, 2 * stats.t.sf(abs(t), J - 1), d.mean()

# finner terskelen der sensitiviteten når target_sens, i hver fold - gir snitt og alle
def threshold_for_sensitivity(pipe, X, y, splits, target_sens=0.80):
    thresholds = []
    for train_idx, val_idx in splits:
        # clone: ny, utrent kopi for hver fold, så ingen fold lærer av en annen
        model = clone(pipe).fit(X.iloc[train_idx], y.iloc[train_idx])
        # sannsynlighet for klasse 1 (ami_3d = 1)
        proba = model.predict_proba(X.iloc[val_idx])[:, 1]
        # roc_curve: sensitivitet (tpr) for hver mulig terskel, fra høy terskel til lav
        fpr, tpr, thr = roc_curve(y.iloc[val_idx], proba)
        # første (høyeste) terskel der sensitiviteten er minst 80 %
        thresholds.append(thr[np.argmax(tpr >= target_sens)])
    return np.mean(thresholds), thresholds



# 1a: rader og unike pasienter
def task_1a(df):
    print(f"Antall rader: {count_rows(df)}")
    print(f"Antall unike pasienter: {count_unique(df, 'pasient_id')}")

# 1b: populasjon, utvalg og standardfeil
def task_1b(df):
    check_column(df, "age_at_admit")
    ages = get_column(df, "age_at_admit")
    describe_population(ages, xlabel="alder ved innleggelse (år)")
    run_samples(ages, [30, 1000], xlabel="alder ved innleggelse (år)")

# 1c: klassebalanse og accuracy for «alltid nei»
def task_1c(df, guess=0):
    check_column(df, "ami_3d")
    ami = get_column(df, "ami_3d")
    counts, shares = class_balance(ami)
    navn = {0: "nei", 1: "ja"}
    print(f"Accuracy «alltid {navn[guess]}»: {counts.get(guess, 0)} av {len(ami)} riktige "
          f"({baseline_accuracy(ami, guess=guess):.2%})")

# 2: alder hos de med og uten hjerteinfarkt
def task_2(df, alpha=0.05):
    ja, nei = split_groups(df, "age_at_admit", "ami_3d")
    describe_groups(ja, nei)

    # histogram: begge gruppene i samme figur, felles søylegrenser
    edges = np.histogram_bin_edges(pd.concat([ja, nei]), bins=30)
    plot_histogram(nei, "Alder etter ami_3d", xlabel="alder ved innleggelse (år)",
                   ylabel="tetthet", bins=edges, label=LABELS[1],
                   density=True, alpha=0.5, show=False)
    plot_histogram(ja, "Alder etter ami_3d", xlabel="alder ved innleggelse (år)",
                   ylabel="tetthet", bins=edges, label=LABELS[0],
                   density=True, alpha=0.5)

    # Q-Q-plott side om side
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    plot_qq(ja, "Q-Q-plott, ami_3d = 1", ylabel="alder (år)", ax=axes[0])
    plot_qq(nei, "Q-Q-plott, ami_3d = 0", ylabel="alder (år)", ax=axes[1])
    plt.tight_layout()
    plt.show()

    print("\n___Normalitet (Shapiro-Wilk)___\n")
    for navn, values in zip(LABELS, [ja, nei]):
        w, p, n_test = normality_test(values)
        print(f"{navn} (testet på n = {n_test}): W = {w:.4f}, p = {p:.3g}")

    t, p = welch_test(ja, nei)
    print(f"\nWelch t-test: t = {t:.2f}, p = {p:.3g}")
    print("Forkast H₀" if p < alpha else "Beholder H₀")

    # nei først, ja sist -> d = mean(ja) - mean(nei), samme retning som t
    d = cohens_d(nei, ja)
    print(f"Cohens d (ja minus nei): {d:.2f}")
    
# 3: lineær regresjon av qt_interval, sammenlignet med baseline
def task_3(df):
    X, y, groups = prepare_regression(df)
    X_train, X_test, y_train, y_test = group_split(X, y, groups)
    modeller = {
        "Lineær regresjon": LinearRegression(),
        # baseline: gjetter alltid gjennomsnittet av y_train
        "Baseline (snitt)": DummyRegressor(strategy="mean"),
    }
    print("\n___Resultat på testsettet___\n")
    for navn, modell in modeller.items():
        r2, mae = evaluate(build_pipeline(modell), X_train, X_test, y_train, y_test)
        print(f"{navn:18} R² = {r2:6.3f}   MAE = {mae:5.1f} ms")

# 4a: gruppert 75/25-deling og en pipeline som predikerer ami_3d
def task_4a(df):
    X, y, groups = prepare_classification(df)
    X_train, X_test, y_train, y_test = group_split(X, y, groups)
    print(f"ami_3d = 1 i trening: {y_train.mean():.2%}, i test: {y_test.mean():.2%}")
    pipe = build_pipeline(LogisticRegression(max_iter=1000), num_cols=CLF_NUM_COLS)
    # fit bare på trening - testsettet røres ikke før 4d
    pipe.fit(X_train, y_train)
    print("Pipeline trent:", pipe)
    return X_train, X_test, y_train, y_test, groups
    
# 4b: tre modeller + baseline, repetert gruppert kryssvalidering (5 x 5)
def task_4b(X_train, y_train, groups):
    # bare treningsradenes pasient_id - testsettet er holdt utenfor
    g_train = groups.loc[X_train.index]
    splits = repeated_group_splits(X_train, y_train, g_train)
    print(f"Antall delinger: {len(splits)}")
    # modellene fra lærerens kode: LogReg, RF og gradient boosting
    modeller = {
        "Baseline (alltid nei)": DummyClassifier(strategy="most_frequent"),
        "Logistisk regresjon": LogisticRegression(max_iter=2000),
        "Random forest": RandomForestClassifier(n_estimators=100, random_state=0),
        "Gradient boosting": GradientBoostingClassifier(random_state=0),
    }
    tabell, scores = compare_models(modeller, X_train, y_train, splits)
    print("\n___Kryssvalidering 5 x 5 (snitt ± SD)___\n")
    # to_string: hele tabellen, ellers kutter pandas kolonner med ...
    print(tabell.to_string())

    plt.figure(figsize=(9, 4))
    plt.boxplot([s[METRIC] for s in scores.values()], tick_labels=list(scores.keys()))
    plt.ylabel(f"{METRIC} (25 folds)")
    plt.xticks(rotation=20)
    plt.title(f"25 valideringsskårer per modell ({METRIC})")
    plt.tight_layout()
    plt.show()

    # beste og nest beste på valgt metrikk (baseline tas ikke med)
    snitt = {navn: s[METRIC].mean() for navn, s in scores.items() if
             not navn.startswith("Baseline")}
    rangert = sorted(snitt, key=snitt.get, reverse=True)
    beste, nest = rangert[0], rangert[1]
    # 1/4: 5-fold gir 20 % validering / 80 % trening 
    t, p, dmean = korrigert_ttest(scores[beste][METRIC], scores[nest][METRIC], 1 / 4)
    print(f"\nBeste på {METRIC}: {beste}")
    print(f"{beste} vs {nest}: differanse = {dmean:.3f}, korrigert t = {t:.2f}, p = {p:.3f}")
    return modeller[beste], beste, splits

# 4c: terskel som gir 80 % sensitivitet, snitt over 5 folds
def task_4c(model, navn, X_train, y_train, splits):
    pipe = build_pipeline(model, num_cols=CLF_NUM_COLS)
    # de 5 første delingene = første gjentakelse = én vanlig 5-fold kryssvalidering
    mean_thr, thresholds = threshold_for_sensitivity(pipe, X_train, y_train, splits[:5])
    print(f"Modell: {navn}")
    print("Terskel per fold:", ", ".join(f"{t:.4f}" for t in thresholds))
    print(f"Gjennomsnittlig terskel: {mean_thr:.4f}")
    return mean_thr

# 4d: tren på hele treningssettet, test én gang på testsettet
def task_4d(model, navn, threshold, X_train, X_test, y_train, y_test):
    pipe = build_pipeline(model, num_cols=CLF_NUM_COLS).fit(X_train, y_train)
    proba = pipe.predict_proba(X_test)[:, 1]
    # 1 hvis sannsynligheten er minst terskelen fra 4c, ellers 0
    pred = (proba >= threshold).astype(int)

    # ravel: matrisen [[TN, FP], [FN, TP]] gjort om til fire tall
    tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
    print(f"Modell: {navn}, terskel {threshold:.4f}")
    print(f"TN = {tn}, FP = {fp}, FN = {fn}, TP = {tp}")
    print(f"Sensitivitet: {tp / (tp + fn):.3f}")
    print(f"Spesifisitet: {tn / (tn + fp):.3f}")
    print(f"Presisjon:    {tp / (tp + fp):.3f}")
    print(f"AUROC: {roc_auc_score(y_test, proba):.3f}   AUPRC: {average_precision_score(y_test, proba):.3f}")

    fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
    ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax[0], colorbar=False)
    ax[0].set_title(f"Forvirringsmatrise (terskel {threshold:.3f})")
    ax[0].set_xlabel("predikert ami_3d")
    ax[0].set_ylabel("faktisk ami_3d")
    RocCurveDisplay.from_predictions(y_test, proba, ax=ax[1], name=navn, plot_chance_level=True)
    ax[1].set_title("ROC-kurve (testsett)")
    PrecisionRecallDisplay.from_predictions(y_test, proba, ax=ax[2], name=navn, plot_chance_level=True)
    ax[2].set_title("PRC-kurve (testsett)")
    plt.tight_layout()
    plt.show()
    
    
def main():
    df = load_file(FILEPATH)

    section("1a")
    task_1a(df)
    section("1b")
    task_1b(df)
    section("1c")
    task_1c(df)
    section("2")
    task_2(df)
    section("3")
    task_3(df)
    section("4a")
    X_train, X_test, y_train, y_test, groups = task_4a(df)
    section("4b")
    model, navn, splits = task_4b(X_train, y_train, groups)
    section("4c")
    threshold = task_4c(model, navn, X_train, y_train, splits)
    section("4d")
    task_4d(model, navn, threshold, X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
    




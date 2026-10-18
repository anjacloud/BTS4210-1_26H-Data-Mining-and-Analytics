#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: 
    studentnummer: 289412

"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from scipy import stats



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
# label, density, alpha og show er nye - standardverdiene gir samme plott som i 1b
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

# Cohens d - samme formelen som i undervisningenmateriale
def cohens_d(a, b):
    n_a, n_b = len(a), len(b)
    s_pooled = np.sqrt(((n_a - 1) * a.var() + (n_b - 1) * b.var()) / (n_a + n_b - 2))
    return (b.mean() - a.mean()) / s_pooled



""" en funksjon skal ha en oppgave """


# 1a: rader og unike pasienter
def task_1a(df):
    print(f"Antall rader: {count_rows(df)}")
    print(f"Antall unike patientene: {count_unique(df, 'pasient_id')}")

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


if __name__ == "__main__":
    main()
    




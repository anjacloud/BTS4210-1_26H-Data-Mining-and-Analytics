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
def plot_histogram(values, title, xlabel=None, ylabel="antall", bins=30):
    if xlabel is None:
        xlabel = values.name
    values.plot(kind="hist", bins=bins, edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
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

"""DEl 1c"""

# teller hvor mange verdier av 0 og 1
def class_balance(values):
    # teller hvor mange ganger hver verdi står i kolonnen
    counts = values.value_counts()
    # samme telling men delt på totalen - 
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


def main():
    df = load_file(FILEPATH)
    
    print(f"Number of rows: {count_rows(df)}")
    print(f"Number of unique patients: {count_unique(df, 'pasient_id')}")
    check_column(df, "age_at_admit")
    ages = get_column(df, "age_at_admit")
    describe_population(ages, xlabel="alder ved innleggelse (år)")
    run_samples(ages, [30, 1000], xlabel="alder ved innleggelse (år)")
    print()
    print(32* "*","\n")
    check_column(df, "ami_3d")
    ami = get_column(df, "ami_3d")
    counts, shares = class_balance(ami)
    navn = {0: "nei", 1: "ja"}
    guess=0
    print(f"Accuracy {navn[guess]}: {counts.get(guess, 0)} av {len(ami)} riktige " f"({baseline_accuracy(ami, guess=guess):.2%})")
    


if __name__ == "__main__":
    main()
    




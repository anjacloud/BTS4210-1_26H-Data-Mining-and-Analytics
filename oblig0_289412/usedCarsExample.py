#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:19:59 2026

@author: oblig0_289412

spørsmål: 
* hvorfor taket er satt til 1 000 000, og hva som er meningen at man skal gjøre med de 3 918 bilene som faller utenfor
* om Year-kolonnen er kjent skitten, og om man forventes å rydde i den eller bare oppdage den
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# henter filen fra mappen - ikke fra nettet som koden fra websiden viste
# blir testet om path eksisterer hvis ikke gis en feilmedling
def get_path(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    return path

# leser filen med dtype -> da leses int64 riktig --> men det går greit uten også fra panda 3.0
# bruker read_csv for å lese data fra CSV filer inn i Pandas DataFrame
# tallene skal bli hetltall= int
def read_file(filepath):
    path = get_path(filepath)
    return pd.read_csv(path, dtype={"Mileage": int, "pricesold": int})

filepath = Path("data") / "used_car_sales.csv"
# laster datasettet
data = read_file(filepath)
# viser kolonnenavn - slik ser man hva vi jobber med uten å se hver gang på datasettet
print(data.columns)


def get_mileage_distribution(data): 
    # setter øvre grense for bins (intervaller) - noen biler har ekstremverdier
    max_distance = 1_000_000
    # deler kilometerstand inn i bins
    # np.linespace lager 10 jent fordelte grensepunkter - 9 bins
    return pd.cut(
         data["Mileage"], bins=np.linspace(0, max_distance, 10, endpoint=True)
         )

# kjører funksjonen og lagrer resultatet  
mileage_dist = get_mileage_distribution(data) 

# siden vi valgte en fast maxgrense fallet noen biler utenfor, men det var ikke de testsettene var ut etter
print()
# viser antall biler per kilometerstand-intervall
print(mileage_dist.value_counts())

# grupperer på bilmerke og teller antall bilmerke
def get_group_by_size(data):
    return data.groupby("Make").size()

#retunerer de n=10 mest solgte bilmerkene
def get_top_makes(data, n=10):
    return data["Make"].value_counts().head(n)

# Sanity check
# sjekker om rader har forsvunnet eller blitt telt dobbelt under grupperingen - derfor assert
# assert krasjer bare hvis noe er galt
assert get_group_by_size(data).sum() == len(data)

print()
# viser top 10 bilmerkene etter antall salg
print(get_top_makes(data))

def plot_price_vs_mileage(data):
    # lager en tom figur
    fig, ax = plt.subplots()
    # plotter gjennomsnittspris per kjørelengde
    data.pivot_table("pricesold", index="Mileage", aggfunc="mean").plot(
        ax=ax, marker="x", linestyle="none"
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    return ax

plot_price_vs_mileage(data)
# viser plottet
plt.show()

  
def plot_price_by_sale_year(data):
    fig, ax = plt.subplots(1, 3, sharey=True, figsize=(16, 10))
    tab = data.pivot_table(
    "pricesold", index="Mileage", columns=["yearsold"], aggfunc="mean"
    )
    # itererer over de tre salgsårene
    for i, year in enumerate((2018, 2019, 2020)):
        # plotter ett år per delplot
        tab[year].plot(ax=ax[i], marker="x", linestyle="none")
        ax[i].set_xscale("log")
        ax[i].set_yscale("log") 
    return ax

plot_price_by_sale_year(data)   
plt.show()    

# viser statistikk for årskolonnen - delt opp i min, max, gjennomsnitt osv
# innebygd funksjon in pandas --> .describe()
def cars_age(data):
    return data["Year"].describe()   

print()
print(cars_age(data))
    
   






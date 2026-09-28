#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:27:42 2026

@author: mine

Øvingsoppgaver del 1 ---- Oppgave 5 – Korrelasjon


a) Beregn Pearson-korrelasjon mellom total_bill og tip, og mellom size og tip. Lag scatterplott.
--> Pearson måler bare rettlinjede sammenhenger og er følsom for uteliggere. Se derfor alltid på scatterplottet, ikke bare på tallet.

b) Lag en korrelasjonsmatrise (heatmap) for de numeriske variablene.

c) size og tip korrelerer. Men henger size også sammen med total_bill? Beregn den partielle korrelasjonen mellom size og tip når vi kontrollerer for total_bill (residualmetoden fra forelesningen). Hva er din/deres analyse/konklusjon basert på resultatet?
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats 


sns.set_theme(style="whitegrid")
rng = np.random.default_rng(1)
tips = pd.read_csv("Data/tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100     # driks i prosent av regningen
print(tips.head())
num_rows = len(tips.index)


# --- 1. Beregn korrelasjonene ---
r_bill, p_bill = stats.pearsonr(tips["total_bill"], tips["tip"])  # r og p-verdi for regning og tips
r_size, p_size = stats.pearsonr(tips["size"], tips["tip"])        # r og p-verdi for antall gjester og tips

print(f"total_bill vs tip: r = {r_bill:.2f}, p = {p_bill:.1e}")   # skriver ut første resultat
print(f"size vs tip:       r = {r_size:.2f}, p = {p_size:.1e}")   # skriver ut andre resultat

# --- 2. Scatterplott side om side ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))              # lager to plott ved siden av hverandre

sns.regplot(data=tips, x="total_bill", y="tip", ax=axes[0],  # punkter + regresjonslinje i venstre plott
            scatter_kws={"alpha": 0.5})                      # alpha gjør punktene litt gjennomsiktige
axes[0].set_title(f"total_bill vs tip (r = {r_bill:.2f})")   # tittel med r-verdien

sns.regplot(data=tips, x="size", y="tip", ax=axes[1],        # samme for size i høyre plott
            x_jitter=0.15, scatter_kws={"alpha": 0.5})       # x_jitter sprer punktene litt sideveis så de ikke overlapper
axes[1].set_title(f"size vs tip (r = {r_size:.2f})")         # tittel med r-verdien

plt.tight_layout()                                           # unngår at plottene overlapper
plt.show()   




# --- 1. Velg de numeriske variablene ---
numeric_columns = ["total_bill", "tip", "size", "tip_pct"]   # listen over kolonner vi vil sammenligne
correlation_matrix = tips[numeric_columns].corr()            # Pearson-korrelasjon mellom alle par
print(correlation_matrix.round(2))                           # skriver ut tabellen med 2 desimaler

# --- 2. Skjul den øvre halvdelen (den er et speilbilde av den nedre) ---
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool)) # True i øvre trekant + diagonalen = skjules

# --- 3. Tegn heatmap ---
plt.figure(figsize=(7, 6))                                   # størrelse på figuren
sns.heatmap(correlation_matrix,                              # tabellen som skal fargelegges
            mask=mask,                                       # skjuler øvre halvdel
            annot=True,                                      # skriver tallet i hver rute
            fmt=".2f",                                       # to desimaler
            cmap="coolwarm",                                 # blå = negativ, rød = positiv
            vmin=-1, vmax=1,                                 # fargeskalaen går fra -1 til 1
            square=True,                                     # kvadratiske ruter
            linewidths=0.5)                                  # tynne streker mellom rutene
plt.title("Correlation matrix – tips")                       # tittel
plt.tight_layout()                                           # unngår at tekst kuttes
plt.show()                                                   # viser figuren                                                # viser figuren
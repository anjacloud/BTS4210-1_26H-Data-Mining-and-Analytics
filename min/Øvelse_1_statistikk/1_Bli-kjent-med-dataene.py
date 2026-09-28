#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:48:44 2026

@author: mine

Øvingsoppgaver del 1 ---- Oppgave 1 – Bli kjent med dataene

a) Hvor mange rader og kolonner er det i datasettet? Mangler det verdier?
b) Klassifiser hver variabel som nominal, ordinal, diskret numerisk eller kontinuerlig.
c) Lag en tabell med gjennomsnitt, median og standardavvik for total_bill, tip og tip_pct.
"""
import numpy as np
import pandas as pd
import seaborn as sns
from statistics import mean, median, mode



sns.set_theme(style="whitegrid")
rng = np.random.default_rng(1)
tips = pd.read_csv("Data/tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100     # driks i prosent av regningen
print(tips.head())
num_rows = len(tips.index)

num_rows = len(tips.index)
print(f"Number of rows: {num_rows}")
rows, columns = tips.shape
print(f"\nRows: {rows}, Columns: {columns}\n")


#s jekk ut om det mangler data
print(tips.isna().sum())
# print true or false (om data mangler eller ikke)
print(tips.isnull().values.any())
# info om hele datasettet
print(tips.info())

"""
   total_bill   tip     sex smoker  day    time  size    tip_pct
0       16.99  1.01  Female     No  Sun  Dinner     2   5.944673
1       10.34  1.66    Male     No  Sun  Dinner     3  16.054159
2       21.01  3.50    Male     No  Sun  Dinner     3  16.658734
3       23.68  3.31    Male     No  Sun  Dinner     2  13.978041
4       24.59  3.61  Female     No  Sun  Dinner     4  14.680765

Klassifiser hver variabel som nominal, ordinal, diskret numerisk eller kontinuerlig - se på Master_brain
"""

print(f"Gjennomsnitt av:\ntotal_bill: {mean(tips.total_bill)}\ntip: {mean(tips.tip)}\ntip_pct: {mean(tips.tip_pct)}\n")
print(f"Median av:\ntotal_bill: {median(tips.total_bill)}\ntip: {median(tips.tip)}\ntip_pct: {median(tips.tip_pct)}\n")


print(f"standardavvik: \ntotal_bill: {tips.total_bill.std()}\ntip: {tips.tip.std()}\ntip_pct: {tips.tip_pct.std()}")

"""
statistikk_tabell = tips.agg(["mean", "median", "std"]).round(2)

# 3. Endre radnavnene til norsk (valgfritt)
statistikk_tabell.index = ["Gjennomsnitt", "Median", "Standardavvik"]

# Vis tabellen
print(statistikk_tabell)

---> fehler im system -> vergass "total_bill", "tip", "tip_pct"
"""


statistikk_tabell = (
    tips[["total_bill", "tip", "tip_pct"]]
    .agg(["mean", "median", "std"])
    .round(2)
)

statistikk_tabell.index = ["Gjennomsnitt", "Median", "Standardavvik"]

print(statistikk_tabell)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:27:38 2026

@author: mine


Øvingsoppgaver del 1 ---- Oppgave 3 – Utvalg, standardfeil og konfidensintervall

Anta at de 244 regningene er hele populasjonen.

Trekk ett tilfeldig utvalg på n = 30. Beregn gjennomsnitt, standardfeil og 95 % konfidensintervall for gjennomsnittlig total_bill. Ligger den sanne populasjonsverdien i intervallet?
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

# --- 1. Populasjonen (fasit) ---
population_mean = tips["total_bill"].mean()                  # sant gjennomsnitt av alle 244 regninger (μ)
population_std = tips["total_bill"].std()                    # sant standardavvik for alle regningene

# --- 2. Trekk et tilfeldig utvalg ---
sample_size = 30                                             # antall observasjoner i utvalget (n)
sample = tips["total_bill"].sample(n=30, random_state=42)  # trekker 30 tilfeldige regninger; seed 42 gir samme utvalg hver gang

# --- 3. Beskrivende mål for utvalget ---
n = len(sample)
sample_mean = sample.mean()                                  # gjennomsnittet i utvalget (x̄), vårt estimat av μ
sample_std = sample.std(ddof=1)                              # standardavvik i utvalget (s); ddof=1 deler på n-1
standard_error = sample_std / np.sqrt(n)                     # standardfeil: hvor mye x̄ typisk varierer mellom utvalg

# --- 4. 95 % konfidensintervall ---
confidence_level = 0.95                                      # ønsket konfidensnivå
degrees_of_freedom = sample_size - 1                         # frihetsgrader for t-fordelingen (n-1)
t_critical = stats.t.ppf((1 + confidence_level) / 2, df=degrees_of_freedom)  # t-verdien som kutter av 2,5 % i hver hale (ca. 2,045)
margin_of_error = t_critical * standard_error                # feilmarginen: hvor langt intervallet strekker seg fra x̄
ci_lower = sample_mean - margin_of_error                     # nedre grense for intervallet
ci_upper = sample_mean + margin_of_error                     # øvre grense for intervallet
contains_true_mean = ci_lower <= population_mean <= ci_upper # True hvis μ ligger inne i intervallet

# --- 5. Skriv ut resultatene ---
print(f"Population mean (μ):   {population_mean:.2f}")      # fasiten
print(f"Sample mean (x̄):       {sample_mean:.2f}")          # estimatet fra utvalget
print(f"Sample std (s):        {sample_std:.2f}")           # spredning mellom enkeltregninger
print(f"Standard error (SE):   {standard_error:.2f}")       # spredning i gjennomsnittet
print(f"t critical:            {t_critical:.3f}")           # multiplikatoren for 95 %
print(f"95 % CI:               [{ci_lower:.2f}, {ci_upper:.2f}]")  # selve intervallet
print(f"Contains μ:            {contains_true_mean}")        # traff intervallet fasiten?

# --- 6. Simulering: hvorfor SE = s / √n ---
number_of_samples = 1000                                     # hvor mange utvalg vi trekker
sample_means = [                                             # liste som skal holde 1000 gjennomsnitt
    tips["total_bill"].sample(n=sample_size, random_state=i).mean()  # trekker utvalg nr. i og lagrer gjennomsnittet
    for i in range(number_of_samples)                        # gjentas 1000 ganger med ulik seed
]
print(f"Std of individual bills:  {population_std:.2f}")                     # spredning for enkeltregninger
print(f"Std of 1000 sample means: {np.std(sample_means):.2f}")               # faktisk spredning i gjennomsnittene
print(f"Formula σ / √n:           {population_std / np.sqrt(sample_size):.2f}")  # det formelen forutsier

sns.histplot(sample_means, bins=30)                          # histogram over de 1000 gjennomsnittene
plt.axvline(population_mean, color="red", linestyle="--")    # rød strek ved det sanne gjennomsnittet
plt.title("Distribution of 1000 sample means (n = 30)")      # tittel på plottet
plt.xlabel("Sample mean of total_bill")                      # tekst på x-aksen
plt.show()                                                   # viser plottet

# --- 7. Dekningsgrad: hvor ofte fanger intervallet μ? ---
hits = 0                                                     # teller for intervaller som inneholder μ
for i in range(number_of_samples):                           # går gjennom 1000 nye utvalg
    repeated_sample = tips["total_bill"].sample(n=sample_size, random_state=i)  # trekker utvalg nr. i
    repeated_se = repeated_sample.std(ddof=1) / np.sqrt(sample_size)            # standardfeil for dette utvalget
    lower, upper = stats.t.interval(confidence_level, df=degrees_of_freedom,    # beregner 95 % KI ...
                                    loc=repeated_sample.mean(), scale=repeated_se)  # ... rundt utvalgets snitt
    hits += lower <= population_mean <= upper                # legger til 1 hvis μ er inne i intervallet
coverage = hits / number_of_samples                          # andel intervaller som traff
print(f"Coverage: {coverage:.3f}")   
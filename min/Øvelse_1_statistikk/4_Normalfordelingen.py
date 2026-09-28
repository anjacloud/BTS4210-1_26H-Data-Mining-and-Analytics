#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:27:40 2026

@author: mine


Øvingsoppgaver del 1 ---- Oppgave 4 – Normalfordelingen


a) Tilpass en normalfordeling til tip_pct (bruk gjennomsnitt og standardavvik).
b) Hva er P(tip_pct > 25) under normalfordelingen? Sammenlign med andelen i dataene.
c) Lag QQ-plott og gjør Shapiro–Wilk. Er tip_pct normalfordelt?
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


# --- 1. Estimer parametrene fra dataene ---
tip_pct = tips["tip_pct"]                                    # kolonnen vi skal tilpasse
fitted_mean = tip_pct.mean()                                 # μ-estimat: gjennomsnittet
fitted_std = tip_pct.std(ddof=1)                             # σ-estimat: standardavviket
print(f"Fitted mean (μ): {fitted_mean:.2f}")                 # skriver ut μ
print(f"Fitted std (σ):  {fitted_std:.2f}")                  # skriver ut σ

# --- 2. Lag normalkurven ---
x_values = np.linspace(tip_pct.min(), tip_pct.max(), 300)    # 300 jevnt fordelte punkter over dataområdet
normal_pdf = stats.norm.pdf(x_values, loc=fitted_mean, scale=fitted_std)  # tetthet til N(μ, σ) i hvert punkt

# --- 3. Histogram med normalkurven oppå ---
sns.histplot(tip_pct, bins=30, stat="density", label="Data")  # stat="density" gjør arealet = 1, samme skala som kurven
plt.plot(x_values, normal_pdf, color="red", linewidth=2,      # tegner normalkurven ...
         label=f"N({fitted_mean:.1f}, {fitted_std:.1f}²)")    # ... med μ og σ i forklaringen
plt.title("tip_pct with fitted normal distribution")         # tittel
plt.xlabel("Tip percentage")                                 # x-akse
plt.legend()                                                 # viser forklaringsboksen
plt.show()                                                   # viser plottet

# --- 4. QQ-plott: sjekk hvor godt tilpasningen er ---
stats.probplot(tip_pct, dist="norm", plot=plt)               # sammenligner datakvantiler med normalkvantiler
plt.title("QQ plot of tip_pct")                              # tittel
plt.show()                                                   # punktene skal ligge på linja hvis dataene er normale

# --- 5. Sammenlign med tall ---
print(f"Skewness: {tip_pct.skew():.2f}")                     # 0 = symmetrisk, >0 = høyreskjev
print(f"Kurtosis: {tip_pct.kurt():.2f}")                     # 0 = som normalfordelingen, >0 = tyngre haler





                                    # normalfordelingen

threshold = 25                                               # grensen vi ser på (25 %)

# --- 1. Sannsynlighet under normalfordelingen ---
z_score = (threshold - fitted_mean) / fitted_std             # hvor mange standardavvik 25 ligger over μ
prob_normal = stats.norm.sf(threshold, loc=fitted_mean, scale=fitted_std)  # sf = 1 - cdf = P(X > 25)

# --- 2. Faktisk andel i dataene ---
count_above = (tips["tip_pct"] > threshold).sum()            # antall regninger med tip_pct over 25
share_data = (tips["tip_pct"] > threshold).mean()            # andel: True telles som 1, False som 0

# --- 3. Skriv ut og sammenlign ---
print(f"\nz-score:                {z_score:.2f}")               # ca. 1,46
print(f"P(tip_pct > 25), normal: {prob_normal:.3f}")          # ca. 0,072
print(f"Share in data:          {share_data:.3f} ({count_above} of {len(tips)})")  # ca. 0,041 (10 av 244)
print(f"Ratio normal / data:    {prob_normal / share_data:.2f}\n")  # hvor mye modellen bommer






tip_pct = tips["tip_pct"]                                    # variabelen vi tester

# --- 1. QQ-plott ---
stats.probplot(tip_pct, dist="norm", plot=plt)               # datakvantiler mot teoretiske normalkvantiler
plt.title("QQ plot of tip_pct")                              # tittel
plt.show()                                                   # punktene skal følge linja hvis data er normale

# --- 2. Shapiro-Wilk-test ---
alpha = 0.05                                                 # signifikansnivå
w_statistic, p_value = stats.shapiro(tip_pct)                # H0: dataene er normalfordelte
print(f"W = {w_statistic:.3f}, p = {p_value:.2e}")           # W nær 1 = normalt; liten p = forkast H0
print("Reject normality" if p_value < alpha else "Cannot reject normality")  # konklusjon

# --- 3. Hvilke verdier er det som skiller seg ut? ---
print(tip_pct.sort_values().tail(5).round(1).values)         # de fem største tipsprosentene

# --- 4. Test igjen uten de mest ekstreme verdiene ---
trimmed = tip_pct[tip_pct < tip_pct.quantile(0.99)]          # fjerner øverste 1 % (3 observasjoner)
w_trimmed, p_trimmed = stats.shapiro(trimmed)                # ny test på resten
print(f"Trimmed: n = {len(trimmed)}, W = {w_trimmed:.3f}, p = {p_trimmed:.3f}")  # sammenlign

stats.probplot(trimmed, dist="norm", plot=plt)               # QQ-plott uten uteliggerne
plt.title("QQ plot of tip_pct (top 1 % removed)")            # tittel
plt.show()                                                   # vis plottet
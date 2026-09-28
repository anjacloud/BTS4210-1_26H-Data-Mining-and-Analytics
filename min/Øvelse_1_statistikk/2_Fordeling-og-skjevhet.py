#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:27:36 2026

@author: mine


Oppgave2 - Øvingsoppgaver del 1 ---- Oppgave 2 – Fordeling og skjevhet

a) Lag histogram og boksplott av total_bill.
b) Hva skjer med skjevheten hvis du log-transformerer? Lag samme histogram for np.log(total_bill).
c) Er gjennomsnitt eller median best / mest representativ som den «typiske regningen»? Hvorfor?
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




sns.set_theme(style="whitegrid")
rng = np.random.default_rng(1)
tips = pd.read_csv("Data/tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100     # driks i prosent av regningen
print(tips.head())
num_rows = len(tips.index)

# nochmal sjekken ob dass das richtige ergebnis ist
tips["total_bill"].plot.hist(bins=20, edgecolor="black")
plt.title("bill")
plt.xlabel("")
plt.ylabel("")
plt.show()

# Alle numeriske kolonner samtidig
tips.hist(bins=20, figsize=(10, 8))
plt.tight_layout()
plt.show()


# Histogram av total_bill
sns.histplot(data=tips, x="total_bill", bins=20, kde=True)
plt.title("Fordeling av total_bill")
plt.xlabel("Total regning ($)")
plt.ylabel("Antall")
plt.show()

# Boksplott av total_bill
sns.boxplot(data=tips, x="total_bill")
plt.title("Boksplott av total_bill")
plt.xlabel("Total regning ($)")
plt.show()





# log-transformerer -> Histogram av total_bill
tips["log_total_bill"] = np.log(tips["total_bill"])

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(data=tips, x="total_bill", bins=20, kde=True, ax=axes[0])
axes[0].set_title("total_bill")

sns.histplot(data=tips, x="log_total_bill", bins=20, kde=True, ax=axes[1])
axes[1].set_title("log(total_bill)")

plt.tight_layout()
plt.show()

# Mål skjevheten med tall
print("Skjevhet før: ", tips["total_bill"].skew())
print("Skjevhet etter:", tips["log_total_bill"].skew())
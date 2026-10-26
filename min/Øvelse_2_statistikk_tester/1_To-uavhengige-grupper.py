#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:44:56 2026

@author: mine
Øvingsoppgaver 2: Forskningsmetode og statistiske tester - Oppgave 1: To uavhengige grupper

Datasettene vi skal bruke: tips (restaurantregninger) og exercise (puls hos 30 personer under ulike aktiviteter målt etter 1, 15 og 30 minutter).

For hver test: formuler H₀/Hₐ, sjekk antakelser, rapporter effektstørrelse + konfidensintervall, og konkluder i tekst


Gir røykere høyere driks (i prosent) enn ikke-røykere?

a) Formuler H₀ og Hₐ. Plott fordelingen av tip_pct for de to gruppene.
b) Sjekk normalitet (Shapiro)
c) Gjør Welch t-test og Mann–Whitney U. Beregn Cohens d og 95 % KI for differansen.
d) Konkluder.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.power import TTestIndPower

sns.set_theme(style="whitegrid")
rng = np.random.default_rng(1)
tips = pd.read_csv("../Data/tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100
ex = pd.read_csv("../Data/exercise.csv")

def cohens_d(a, b):
    na, nb = len(a), len(b)
    sp = np.sqrt(((na - 1) * np.var(a, ddof=1) + (nb - 1) * np.var(b, ddof=1)) / (na + nb - 2))
    return (np.mean(a) - np.mean(b)) / sp


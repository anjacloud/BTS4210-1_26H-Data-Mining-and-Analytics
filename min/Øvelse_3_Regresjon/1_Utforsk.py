#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:05:31 2026

@author: mine

Øvingsoppgaver 3 – Regresjon - Oppgave 1 – Utforsk

Datasett: diamonds_5000:

5 000 diamanter med pris (USD) og egenskaper: carat (vekt), cut, color, clarity (kvalitet), depth, table, samt dimensjonene x, y, z.

Mål: predikere price.

a) Plott fordelingen av price (histogram). Vurder om det kan være lurt å logtransformere price`?
b) Lag et scatterplott av carat mot price, og av log(carat) mot log(price). Hva ser du?
c) Lag en korrelasjonsmatrise for de numeriske variablene. Er det noen variabler som er redundante?
"""

import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4"
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, KFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

sns.set_theme(style="whitegrid")
rng = np.random.default_rng(1)
dia = pd.read_csv("Data/diamonds_5000.csv")
print(dia.head())

"""
a
"""

dia["log_price"] = np.log(dia["price"])

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(data=dia, x="price", bins=50, kde=True, ax=axes[0])
axes[0].set_title("price")

sns.histplot(data=dia, x="log_price", bins=50, kde=True, ax=axes[1])
axes[1].set_title("log(price)")

plt.tight_layout()
plt.show()

print("Skjevhet price:    ", round(dia["price"].skew(), 2))
print("Skjevhet log_price:", round(dia["log_price"].skew(), 2))

"""
b
"""
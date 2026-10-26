#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:03:11 2026

@author: mine

Øvingsoppgaver 3 – Regresjon - Oppgave 4 – Pipline, modellvalg og hyperparameter

Datasett: diamonds_5000:

5 000 diamanter med pris (USD) og egenskaper: carat (vekt), cut, color, clarity (kvalitet), depth, table, samt dimensjonene x, y, z.

Mål: predikere price.

Implementer en ColumnTransformer som skalerer de numeriske variablene og one-hot-encode de kategoriske. Bruk y = log(price) som target. Sammenlign med 5-fold kryssvalidering (RMSE på log-skala) på treningsdata: Ridge, Lasso(alpha=0.001, max_iter=20000) og RandomForestRegressor(n_estimators=100, random_state=0). Gjør deretter et grid search (GridSearchCV() for den beste modellen (minst 2 hyperparametere).
"""


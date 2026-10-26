#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:02:59 2026

@author: mine

Øvingsoppgaver 3 – Regresjon - Oppgave 3 – Linear regresjon: original vs logaritmisk skala

Datasett: diamonds_5000:

5 000 diamanter med pris (USD) og egenskaper: carat (vekt), cut, color, clarity (kvalitet), depth, table, samt dimensjonene x, y, z.

Mål: predikere price.

a) Tren LinearRegression på de numeriske variablene for å predikere price. Rapporter testmetrikker.
b) Tren samme modell for å log-normlisere skjevfordelte variabler (også target). Regn prediksjonene tilbake med np.exp og rapporter RMSE/MAE i USD.
c) Hvilken metode er best?
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:03:06 2026

@author: mine

Øvingsoppgaver 3 – Regresjon 5 – Endelig test og feilanalyse

Datasett: diamonds_5000:

5 000 diamanter med pris (USD) og egenskaper: carat (vekt), cut, color, clarity (kvalitet), depth, table, samt dimensjonene x, y, z.

Mål: predikere price.

a) Evaluer den beste modellen på testsettet. Rapporter RMSE, MAE og R2 i USD (regn tilbake med exp) og MAE i forhold til gjennomsnittlig pris.
b) Plott predikert vs. faktisk pris, og residualer vs. predikert pris.
c) Del testsettet i tre karat-grupper (< 0,5 / 0,5–1,0 / > 1,0). Beregn RMSE, MAE og R2 per gruppe. Hvor er modellen dårligst?
"""


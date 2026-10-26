#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:19:45 2026

@author: mine

Øvingsoppgaver 4 – Klassifisering - Oppgave 2 – Første modell


Data Mining & Analytics – Samling 2, dag 2 (ettermiddag)

Datasett: Pima Indians Diabetes Mål: predikere om personen har diabetes (class). Tenk deg at modellen skal brukes til screening. Må derfor vurdere hva som er mest problematisk: overse en syk, eller å kalle inn en frisk til ekstra testing?

a) Erstatt fysiologisk umulige null-verdier med missing. Del i trening/test (75/25, (bruk gjerne stratifisering)).
b) Bygg en pipeline (f.eks imputer --> StandardScaler --> logistisk regresjon) og tren den.
c) Rapporter nøyaktighet, sensitivitet, spesifisitet, presisjon og F1 på testsettet (bruk terskel 0,5) og plott en confusion matrix.

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
from sklearn.model_selection import train_test_split, StratifiedKFold, RepeatedStratifiedKFold, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve, precision_recall_curve, average_precision_score, ConfusionMatrixDisplay
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE

sns.set_theme(style="whitegrid")
rng = np.random.default_rng(1)


data = pd.read_csv("../Data/pima.csv")
data["diabetes"] = (data["class"] == "tested_positive").astype(int)
data = data.drop(columns="class")
data.head()
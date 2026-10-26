#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:19:44 2026

@author: mine

Øvingsoppgaver 4 – Klassifisering - Oppgave 3 – ROC og terskel

Data Mining & Analytics – Samling 2, dag 2 (ettermiddag)

Datasett: Pima Indians Diabetes Mål: predikere om personen har diabetes (class). Tenk deg at modellen skal brukes til screening. Må derfor vurdere hva som er mest problematisk: overse en syk, eller å kalle inn en frisk til ekstra testing?

a) Plott ROC- og PR-kurve for testsettet, og oppgi AUROC og AUPRC-verdi
b) Kravet er nå en sensitivitet ≥ 85 %. Finn terskelen på valideringsdata fra utviklingssettetd, som du så bruker på testsettet.
c) Rapporter metrikkene på testsettet med den nye terskelen. Har dette gitt noen endring i spesifisitet og presisjon?

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

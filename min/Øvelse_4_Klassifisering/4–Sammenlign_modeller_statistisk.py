#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:19:43 2026

@author: mine

Øvingsoppgaver 4 – Klassifisering -  Oppgave 4 – Sammenlign modeller statistisk

Sammenlign fire varianter med repetert stratifisert 5-fold (5 repetisjoner) på treningsdata, med AUROC som metrikk (velg modeller selv, men kan være lurt å ta noen simple modeller så ikke prosessen tar så lang tid):

a) Lag et boksplott med skårene fra alle modellene
b) Er den beste modellen signifikant bedre enn logistisk regresjon? Bruk gjerne både vanlig paret t-test og Nadeau–Bengios korrigerte test (begynn med å gjøre sammenligning mellom beste og dårligste - hvis ikke forskjell, så er det ikke vits å gjøre med resten)
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:05:52 2026

@author: mine
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(0)
X = rng.normal(size=(50, 1))
y = 2 * X.ravel() + rng.normal(scale=0.3, size=50)

df = pd.DataFrame({"x": X.ravel(), "y": y})

model = LinearRegression().fit(X, y)
print("stigningstall:", model.coef_[0].round(3), "(bør være nær 2)")
print(df.describe())

plt.scatter(df["x"], df["y"], s=12)
plt.plot(X, model.predict(X), color="red")
plt.show()
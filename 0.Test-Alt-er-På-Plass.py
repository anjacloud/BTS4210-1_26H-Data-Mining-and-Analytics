#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:51:50 2026

@author: mine
"""

"""
Function - første dagen
test om alt fungerer som det skal

"""


from sklearn.metrics import root_mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

rmse = root_mean_squared_error(y_true, y_pred)
print(rmse)
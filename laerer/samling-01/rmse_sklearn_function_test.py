# -*- coding: utf-8 -*-
"""
RMSE med scikit-learn

Opphav   : LEO (Lars Erik Opdal), urørt
Status   : LEOs original. Står ordrett i notat 1 ved slide 29, med utdata 0.6123724356957945

Created on Sun Aug 30 11:29:45 2026   (Spyder-stempel fra LEOs egen maskin: @author sto som "lopda".
                             Det var beviset på opphav)
"""

from sklearn.metrics import root_mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

rmse = root_mean_squared_error(y_true, y_pred)
print(rmse)
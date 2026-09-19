#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Alt er På Plass — samling 1, dag 1

Opphav   : avskrift i timen
Status   : skrevet av mens LEO kodet foran klassen

Created on Mon Aug 31 12:51:50 2026   (Spyder-stempel. @author er fjernet — det sto "mine"
                             på alle filer, også dem som er LEOs)
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:40:46 2026

@author: mine
"""
"""
import numpy as np
import matplotlib 



#start og stopp dagen for arrayen
x = np.arange(1, 6)


def T(x):
    return 7 - 10*np.cos(2*np.pi/365*x - 5*np.pi/73)
t = T(x)
print(t)



data = np.column_stack((x,t))

np.savetxt(("09_02-temperatur.txt", data, fmt=["%d", "%.4f"]))

"""


import numpy as np
import matplotlib.pyplot as plt

def T(x):
    return 7 - 10*np.cos( ((2*np.pi*x) / 365.0) - (5*np.pi / 73.0) )
x = np.linspace(1,365,365)
vektor = T(x)
plt.plot(x,vektor)
plt.ylabel('Temp i [deg C]')
plt.xlabel('Dag nr. fra/for et år')
plt.savefig('plot_klima.png')
kol = np.array([x,vektor]).T
np.savetxt('datafil_temp.csv', kol, fmt='%.1f', delimiter=':')


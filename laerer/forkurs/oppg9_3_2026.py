# -*- coding: utf-8 -*-
"""
9.3 — Skrive temperaturverdier til fil

Opphav   : LEO (Lars Erik Opdal), urørt
Status   : LEOs original, vist i timen 2026-09-01 kl. 09:51
Kopi     : den samme koden står nederst i ../../min/forkurs/09_03-skrive-temperaturverdier-til-fil.py

Created on Tue Sep  1 09:51:27 2026   (Spyder-stempel fra LEOs egen maskin: @author sto som "lopda".
                             Det var beviset på opphav)
"""


import matplotlib.pyplot as plt
import numpy as np

def T(x):
    return 7 - 10*np.cos( ((2*np.pi*x) / 365.0)  - (5*np.pi / 73.0) ) 

x = np.linspace(1,365,365)
vektor = T(x)

plt.plot(x,vektor)

plt.ylabel('Temp i [deg C]')
plt.xlabel('Dag nr. fra/for et år')


plt.savefig('plot_klima.png')

kol = np.array([x,vektor]).T

np.savetxt('datafil_temp.csv', kol, fmt='%.1f',delimiter=':')


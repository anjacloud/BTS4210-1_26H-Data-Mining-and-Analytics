#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9.3 — Skrive temperaturverdier til fil

Opphav   : BLANDET — mitt utkast øverst (utkommentert), LEOs løsning nederst
Status   : IKKE LØST AV MEG. Utkastet stopper på en parentesfeil i np.savetxt:
         alle argumentene er pakket i én tuppel, som gir SyntaxError
Original : ../../laerer/forkurs/oppg9_3_2026.py — identisk, bortsett fra to mellomrom
Merk     : LEOs kode skriver datafil_temp.csv (kolonseparert), ikke temperatur.txt
         som oppgaven ber om og som 9.4 skal lese
Notat    : Master_brain/…/BTS4210-…/02_assignments/Forkurs-python-numpy/09.03-skrive-temperaturverdier-til-fil.md

Created on Tue Sep  1 09:40:46 2026   (Spyder-stempel. @author er fjernet — det sto "mine"
                             på alle filer, også dem som er LEOs)
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


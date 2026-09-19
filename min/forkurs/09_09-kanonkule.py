#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:49:42 2026

@author: mine
"""

"""
Oppgave 09.09 - løsning fra læreren
"""
import numpy as np
import matplotlib.pyplot as plt
def y_komp(v0y, t):
    g = 9.81
    return v0y*t - 0.5*g*t**2
def x_komp(v0x, t):
    return v0x*t
tid = np.linspace(0, 22, 100)
v0 = 150
vinkel = np.pi/4
vx_init = v0*np.cos(vinkel)
vy_init = v0*np.sin(vinkel)
Xkomp = x_komp(vx_init, tid)
Ykomp = y_komp(vy_init, tid)
#--- ny kode:
M = np.array([Xkomp, Ykomp, tid]).T #Lager ny matrise der data bli transponsert til 3 kolonnere med samsavrende rader..
np.savetxt('kanon_2026.txt', M,fmt='%.1f',delimiter=':')
maks_hoyde_indeks = Ykomp.argmax()
maks_hoyde = Ykomp[maks_hoyde_indeks]
print("Maks høyde er: " , int(maks_hoyde), " meter")
maks_lengde = Xkomp[maks_hoyde_indeks]
print("Maks lengde er: " , int(maks_lengde), " meter")
#leser av 15.11 til plass 68
print("høyden etter t=15s er " , int(Ykomp[68]), " meter")
plt.close('all')
plt.plot(Xkomp, Ykomp)
plt.xlabel('x [m]')
plt.ylabel('y [m]')


"""
min egen løsning:
"""


# -*- coding: utf-8 -*-
"""
Visualisering med Python, del 1

Opphav   : LEO (Lars Erik Opdal), urørt
Status   : LEOs original. Kildekoden bak skjermbildene i notat 3
MANGLER  : somedata.csv finnes ikke lokalt — første blokk kan ikke kjøre

Created on Mon Sep 29 18:47:15 2025   (Spyder-stempel fra LEOs egen maskin: @author sto som "lopda".
                             Det var beviset på opphav)
"""

#%% Data visualisation in Python

import pandas as pd

df = pd.read_csv("./somedata.csv", index_col="x")

print(df)
print(df.tail(10))

#Søylediagram virker dårlig her:
#df.plot(kind="bar")


#Historgram blir også feil..?
#df.plot(kind="hist", stacked=True)

#Bedre:
df.plot()



#%% Visualising with matplotlib

import matplotlib.pyplot as plt
import numpy as np


#Vi lager en sinus kurve:

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

plt.plot(x, y)


fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_title("$sin(x)$")
ax.set_xlabel("x")
ax.set_ylabel("y");


#Vi får et bilde (fig) med to plots ax1 og 2:

fig, (ax1, ax2) = plt.subplots(1, 2)    
ax1.plot(x, np.sin(x))
ax1.set_title("$sin(x)$")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2.plot(x, np.cos(x))
ax2.set_title("$cos(x)$")
ax2.set_xlabel("x")

#Når vi har en funksjon med 2 avhengige variabler f.eks. f(x,y) kan vi lage et 2D plot:
#C = np.outer(np.sin(x), np.cos(x))
#plt.pcolor(x, x, C)
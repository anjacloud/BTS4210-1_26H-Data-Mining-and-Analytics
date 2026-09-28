#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vær på forskjellige steder — samling 1, dag 2

Opphav   : avskrift i timen
Status   : skrevet av mens LEO kodet foran klassen
Data     : bergen.txt, oslo.txt, tromso.txt, trondheim.txt i samme mappe

Created on Tue Sep  1 14:10:56 2026   (Spyder-stempel. @author er fjernet — det sto "mine"
                             på alle filer, også dem som er LEOs)
"""



import pandas as pd

df = pd.read_csv("./bergen.txt", index_col="time")
print(df)
print(df.tail(10))
#Søylediagram virker dårlig her:
#df.plot(kind="bar")
#Historgram blir også feil..?
#df.plot(kind="hist", stacked=True)
#Bedre:
df.plot()

"""
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

"""
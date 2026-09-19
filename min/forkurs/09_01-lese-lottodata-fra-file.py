#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:43:53 2026

@author: mine
"""

import numpy as np

"""
file = open("/Users/mine/Documents/Master_USN_Repo/BTS4210-1_26H-Data-Mining-and-Analytics/_homework/09_01-Lottotall.txt", "r")

content = file.read()
#print(content)
# I did wonder what type it is - it was a string not a integer
print(" type :", type(content).__name__)

#integer_array = np.array([int(i) for i in content])
#print("Integer Array : ")
#print(integer_array, "\n")
file.close()



this under is with help from Claude
"""


STI = "09_01-Lottotall.txt"

print("=" * 60)
print("STEG 1 - les fila.  Du har dette fra for.")
content = open(STI).read()
print("  type :", type(content).__name__)
print("  ser slik ut:", repr(content[:25]), "...")
print("  -> EN lang tekst. Ikke tall.")

print()
print("=" * 60)
print("STEG 2 - del den opp.")
biter = content.split()
print("  type :", type(biter).__name__)
print("  antall:", len(biter))
print("  forste 7:", biter[:7])
print("  -> en LISTE med små tekster. Fortsatt ikke tall.")


print()
print("=" * 60)
print("STEG 3 - gjor hver bit om til et tall.")
tall = [int(b) for b in biter]
print("  forste 7:", tall[:7])
print("  -> nå er de tall. Merk: ingen apostrofer rundt dem lenger.")


print()
print("=" * 60)
print("STEG 4 - legg dem i et NumPy-array.")
lotto = np.array(tall)
print("  dtype:", lotto.dtype, " <- int64 = du er i mal")
print("  shape:", lotto.shape, "  <- 52 rader x 7 tall =", 52 * 7)
print("  forste 7:", lotto[:7])

print()
print("=" * 60)
print("STEG 5 - telle hvor manger 2er vi har")
nr2 = np.count_nonzero(lotto == 2)
print(f"Nummer 2 er med: {nr2} ganger")



"""
Og alt går også bare på 4 linjer - hahahah


lotto.loadtext(STI)
nr2 = np.count_nonzero(lotto == 2)
print(f"Nummer 2 er med: {nr2} ganger - bare litt kortere kodesnut")

"""
print()
print("=== DEN KORTE VERSJONEN ===")
lotto = np.loadtxt(STI, dtype=int)
print("nr2 =", np.count_nonzero(lotto == 2), "(bare veldig mye kortere denne versionen)")
print("shape:", lotto.shape, " dtype:", lotto.dtype)


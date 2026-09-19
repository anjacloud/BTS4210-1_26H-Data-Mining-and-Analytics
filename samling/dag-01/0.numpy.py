#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:19:53 2026

@author: mine
"""

import numpy as np

a = np.array([1,2,3,4])
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(b)
print()


#vanlig python med for-løkke
summen = 0
for num in a:
    print(f"This is the sum: {summen}" )
    summen = num + summen

# vektorisert sum-funktion
c = np.sum(a)
print("summen av alle elementer i a er:", c)


print("This is a:", a[1].dtype)
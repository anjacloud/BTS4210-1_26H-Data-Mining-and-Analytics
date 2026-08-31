#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:28:59 2026

@author: mine
"""

"""
første dagen - teste om man husker loops igjen ;)
"""

fruits = ["banan", "apple", "strawberry", "tomato"]

for fruit in fruits:
    print("The fruit", fruit, "has index", fruits.index(fruit))
    
    

print()
print("*********")


numbers = list(range(14))

for num in numbers:
    squared = num**2
    if num < 10:
        print (num,'---> squared is', squared)
    if num >= 10:
        print(num,'--> squared is', squared)
    
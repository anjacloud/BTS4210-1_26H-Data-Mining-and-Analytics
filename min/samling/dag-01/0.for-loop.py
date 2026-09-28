#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
for loop — samling 1, dag 1

Opphav   : avskrift i timen
Status   : skrevet av mens LEO kodet foran klassen

Created on Mon Aug 31 12:28:59 2026   (Spyder-stempel. @author er fjernet — det sto "mine"
                             på alle filer, også dem som er LEOs)
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
    
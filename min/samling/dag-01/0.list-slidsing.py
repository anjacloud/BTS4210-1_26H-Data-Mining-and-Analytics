#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
list slidsing — samling 1, dag 1

Opphav   : avskrift i timen
Status   : skrevet av mens LEO kodet foran klassen

Created on Mon Aug 31 13:21:34 2026   (Spyder-stempel. @author er fjernet — det sto "mine"
                             på alle filer, også dem som er LEOs)
"""

"""
list slidsing - første dagen

"""

# nums = [numbers for numbers in range(0,101, 5)] --> samme som nedenfor
nums = list(range(100))


print(nums)
print()

print(nums[0:3])
print()

print("fra 4 til slutten av enden:", nums[4:])
print()

print("fra 1 til 5 i 2er step:", nums[1:5:2], "-> tall i mitten blir i denne sammenheng aldri tatt med") 
print()


print("siste elemente:",nums[-1])
print()

nums = list(range(0,100,5))
print(nums)
print(len(nums))
print()

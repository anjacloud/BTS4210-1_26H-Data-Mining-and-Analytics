#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:21:34 2026

@author: mine
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

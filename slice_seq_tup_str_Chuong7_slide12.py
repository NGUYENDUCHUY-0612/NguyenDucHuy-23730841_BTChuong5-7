# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:49:51 2024

@author: ADM
"""

seq = [3,2,'A',8,6,8]
tup = (12,'C',7,9,'Z')
str = 'Hello Python'
print(slice(4)) # Xuất vị trí không xuất giá trị của vị trí đó
print(slice(2,4))# Xuất vị trí không xuất giá trị của vị trí đó
print(slice(1,4,2))# Xuất vị trí không xuất giá trị của vị trí đó

print(seq[slice(4)])#Xuất ra cái giá trị của cái vị trí đó 
print(tup[slice(1,4,2)])#Xuất ra cái giá trị của cái vị trí đó
print(str[slice(2,4)])#Xuất ra cái giá trị của cái vị trí đó

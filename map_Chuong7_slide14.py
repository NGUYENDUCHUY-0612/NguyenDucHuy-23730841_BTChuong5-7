# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:11:19 2024

@author: ADM
"""

def tinh(x):
    return x + 3
num1 = [1,2,3,4,5,6]
num2 = map(tinh, num1)
print(list(num2))
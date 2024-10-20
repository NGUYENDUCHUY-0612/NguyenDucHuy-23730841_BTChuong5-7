# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:49:02 2024

@author: ADM
"""

n = int(input("Nhập số nguyên dương n: "))

giai_thua = 1
if n >= 0:
  for i in range(1, n+1):
    giai_thua *= i
print(n, "! =", giai_thua)
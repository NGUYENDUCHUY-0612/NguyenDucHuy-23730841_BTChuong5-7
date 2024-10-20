# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:19:36 2024

@author: ADM
"""

#Bài 2 
ds = [('Tiền Giang', 63), ('Long An', 62), ('Vĩnh Long', 64), ('Bình Dương',60),('Bình Định',77)]
print(sorted(ds, key=lambda x: x[1]))
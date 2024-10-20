# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:39:59 2024

@author: Nguyễn Đức Huy - 23730841
"""

n = int(input("Nhập vào một số nguyên n: "))

my_dict = {}
i = 1
while i <= n:
    my_dict[i] = i**3
    i += 1

print(my_dict)

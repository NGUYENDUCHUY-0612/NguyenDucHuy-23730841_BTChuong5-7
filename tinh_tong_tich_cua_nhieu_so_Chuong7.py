# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:28:51 2024

@author: Nguyễn Đức Huy - 23730841
"""
def tinh_tong_tich(*args, **kwargs):
    tong = sum(args)
    tich = 1
    for num in args:
        tich *= num
    return tong, tich
tong, tich = tinh_tong_tich(6, 2, 8, 4)
print(f"Tổng: {tong}, Tích: {tich}")

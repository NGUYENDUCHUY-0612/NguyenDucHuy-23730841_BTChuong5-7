# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:58:35 2024

@author: ADM
"""

#Bài 1 - slide - trang 36 (Chương 7)
def tinhtong(*args, **kwargs):
    return sum(args)
def tinh_tich(*args, **kwargs):
    tich = 1
    for i in args:
        tich *= i
    return tich
if __name__=="__main__":
    ds = [1,2,3,4,5]
    print(tinhtong(*ds))
    print(tinh_tich(*ds))
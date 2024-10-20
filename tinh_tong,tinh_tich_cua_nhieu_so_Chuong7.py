# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:13:11 2024

@author: Nguyễn Đức Huy - 23730841
"""
#tính tổng
def tinh_tong(*args):
  tong = 0
  for so in args:
    tong += so
  return tong
print(tinh_tong(1, 2, 3, 4))

#tính tích
def tinh_tich(*args):
  tich = 1
  for so in args:
    tich *= so
  return tich
print(tinh_tich(2, 3, 4)) 

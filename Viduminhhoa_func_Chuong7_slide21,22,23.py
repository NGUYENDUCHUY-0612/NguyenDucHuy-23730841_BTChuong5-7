# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:23:37 2024

@author: Nguyễn Đức Huy - 23730841
"""
def giai_thua(n):
    x = 1 
    for i in range(1, n + 1):
        x = x * i
    return x 
giai_thua(3)


def giai_thua_va_tong(n):
    x = 1 
    y = 0
    for i in range(1, n+1):
        x = x*i
        y = y*i
    return x, y
giai_thua_va_tong(5)

def fib(n):
    a, b = 0, 1
    whilde a < n:
        print(a, end='')
        a, b = b, a+b
    print()
fib(2018)
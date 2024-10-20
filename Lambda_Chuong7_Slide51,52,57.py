# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:38:54 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Ví dụ minh họa Đệ Quy_slide 48
def print_numbers(n):
    if n >= 1:
        print_numbers(n-1)
        print(n)
print_numbers(5)

#Ví dụ minh họa Lambda function _ slide 51, 52
def cong(x = 1, y = 2):
    return x + y 

f = lambda a,b,c: cong(a,b)+ c**2
#f=(lambda a,b,c: cong(a,b) + c**20)(3,6,9)
ket_qua = f(3,6,9)
print(ket_qua)
#print(f)

#Lambda kết hợp với map_slide58
num = [1,3,5,7,9]
new_num = map(lambda x: x + 3, num)
print(list(new_num))
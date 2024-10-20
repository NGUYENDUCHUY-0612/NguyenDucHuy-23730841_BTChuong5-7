# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:18:22 2024

@author: Nguyễn Đức Huy - 23730841
"""

import math
#tính chu vi hình vuông
def tinh_chu_vi_hinh_vuong(canh):
    return 4*canh
print(tinh_chu_vi_hinh_vuong(5))


#tính chu vi hình chữ nhật
def tinh_chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong):
    return 2 * (chieu_dai + chieu_rong)
print(tinh_chu_vi_hinh_chu_nhat(5,7))

#tính chu vi hình tròn 
def tinh_chu_vi_hinh_tron(ban_kinh):
    return 2 * math.pi *ban_kinh
print(tinh_chu_vi_hinh_tron(6))
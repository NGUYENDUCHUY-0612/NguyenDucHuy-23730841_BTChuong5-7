# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:33:56 2024

@author: Nguyễn Đức Huy - 23730841
"""

# Tạo một danh sách rỗng để lưu trữ kết quả
danh_sach_so_chan = []

# Duyệt qua các số từ 2018 đến 2828
for so in range(2018, 2829):
    # Kiểm tra xem số đó có chia hết cho 2 và 5 không
    if so % 2 == 0 and so % 5 == 0:
        # Nếu chia hết cho cả 2 và 5 thì thêm vào danh sách
        danh_sach_so_chan.append(so)

# In ra danh sách kết quả
print(danh_sach_so_chan)
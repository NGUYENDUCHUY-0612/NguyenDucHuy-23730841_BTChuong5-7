# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:38:18 2024

@author: Nguyễn Đức Huy - 23730841

"""
# Khởi tạo biến bắt đầu và danh sách kết quả
so = 2020
danh_sach_chia_het_cho_9 = []

# Vòng lặp while cho đến khi số vượt quá 3838
while so <= 3838:
    # Kiểm tra xem số đó có phải là số chẵn và chia hết cho 9 không
    if so % 2 == 0 and so % 9 == 0:
        danh_sach_chia_het_cho_9.append(so)
    # Tăng số lên 2 để kiểm tra số chẵn tiếp theo
    so += 2

# In kết quả
for so in danh_sach_chia_het_cho_9:
    print(so, end='\t')

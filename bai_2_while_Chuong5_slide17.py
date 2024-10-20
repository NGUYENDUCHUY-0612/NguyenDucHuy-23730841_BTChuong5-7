# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:48:21 2024

@author: ADM
"""

while True:
    so_thuc = input("Nhập vào một số thực trong khoảng -89.9 đến 88.8: ")
    try:
        so_thuc = float(so_thuc)  # Chuyển đổi nhập liệu thành số thực
        if -89.9 <= so_thuc <= 88.8:
            print("Số bạn nhập hợp lệ!")
            break  # Thoát khỏi vòng lặp nếu điều kiện đúng
        else:
            print("Số bạn nhập không hợp lệ. Vui lòng nhập lại!")
    except ValueError:
        print("Giá trị nhập vào không phải là số thực. Vui lòng nhập lại!")
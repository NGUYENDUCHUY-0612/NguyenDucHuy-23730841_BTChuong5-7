# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:30:19 2024

@author: ADM
"""
while True:
    so = input("Nhập vào một số trong khoảng -99 đến 99: ")
    try:
        so = int(so)  # Chuyển đổi nhập liệu thành số nguyên
        if -99 <= so <= 99:
            print("Số bạn nhập hợp lệ!")
            break  # Thoát khỏi vòng lặp nếu điều kiện đúng
        else:
            print("Số bạn nhập không hợp lệ. Vui lòng nhập lại!")
    except ValueError:
        print("Giá trị nhập vào không phải là số. Vui lòng nhập lại!")

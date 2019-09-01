#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 猜数.py
# @Author: smx
# @Date  : 2019/8/15
# @Desc  :

# 之前用遍历的方式，没有考虑到数字之间的规律，复杂度太高！
x, y = list(map(int, input().split()))
if y > x * 2:
    print(0)
elif y <= x * 2 and y > x:
    print(x - y // 2)
else:
    if y % 2 == 0:
        print(y // 2)
    else:
        print((y - 1) // 2)

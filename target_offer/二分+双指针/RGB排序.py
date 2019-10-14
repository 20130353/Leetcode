# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/24/18
# file: RGB排序.py
# description:
'''
    给定字符串包含RGB三种字符,按照RGB的顺序排列字符串
'''


# 定义左边界，右边界，找到需要

def sort_RGB(str):
    R = 0
    while str[R] == 'R' and R < len(str):
        R += 1
    if R >= len(str):
        return str

    j = len(str) - 1
    while str[j] == 'B' and j >= 0:
        j -= 1
    if j <= 0:
        return str

    for G in range(R, j):
        while str[G] != 'G':  # 忽略'G'
            if str[G] == 'R':  # 直接找'R'
                str[R], str[G] = str[G], str[R]
                while str[R] == 'R':  # 直接找 'G'
                    R += 1
                G = max(G, R)
                if G > j:
                    return str
            if str[G] == 'B':  # 直接找'B'
                str[j], str[G] = str[G], str[j]
                while str[j] == 'B':
                    j -= 1
                G = min(G, j)
                if G < R:
                    return str


if __name__ == '__main__':
    str = ['R', 'G', 'B', 'B', 'G', 'R', 'R', 'B', 'R', 'G', 'R', 'B', 'B', 'G']
    new_str = sort_RGB(str)
    print(new_str)

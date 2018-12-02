# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/24/18
# file: RGB排序.py
# description:
'''
    给定字符串包含RGB三种字符,按照RGB的顺序排列字符串
'''


def sort_RGB(str):
    i = 0
    while str[i] == 'R' and i < len(str):
        i += 1

    if i >= len(str):
        return str

    j = len(str) - 1

    while str[j] == 'B' and j >= 0:
        j -= 1
    if j <= 0:
        return str

    for k in range(i, j):
        if k > j:
            return str
        while str[k] != 'G':  # 忽略'G'
            if str[k] == 'R':  # 直接找'R'
                str[i], str[k] = str[k], str[i]
                while str[i] == 'R':  # 直接找 'G'
                    i += 1
                k = max(k, i)
                if k > j:
                    return str
            if str[k] == 'B':  # 直接找'B'
                str[j], str[k] = str[k], str[j]
                while str[j] == 'B':
                    j -= 1
                k = min(k, j)
                if k < i:
                    return str


if __name__ == '__main__':
    str = ['R', 'G', 'B', 'B', 'G', 'R', 'R', 'B', 'R', 'G', 'R', 'B', 'B', 'G']
    new_str = sort_RGB(str)
    print(new_str)

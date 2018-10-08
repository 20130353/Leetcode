# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: fibonacci_find.py
# description:

import numpy as np
def binary_find(data,v):

    low = 0
    high = len(data) - 1
    while(low < high):
        mid = np.int((low+high)/2)

        if data[mid] == v:
            flag = True
            return mid
        if data[mid] < v:
            low = mid
        elif data[mid] > v:
            high = low
    return -1


if __name__ == '__main__':
    data = np.random.rand(10)
    data = sorted(data)
    inx = binary_find(data,data[7])
    print(inx)

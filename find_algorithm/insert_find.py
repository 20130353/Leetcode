# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: insert_find.py
# description:

import numpy as np

def insert_find(data, v):
    low = 0
    high = len(data)-1

    while(low < high):
        mid = np.int(low + (v-data[low])/(data[high]-data[low])*(high-low))
        if data[mid] == v:
            return mid
        if data[mid] < v:
            low = mid
        else:
            high = mid

    return -1

if __name__ == '__main__':
    data = np.random.rand(10)
    data = sorted(data)
    inx = insert_find(data, data[7])
    print(inx)

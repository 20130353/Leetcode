# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: quick_sort.py
# description:

import numpy as np
import copy

# 只有这一种写法是正确的!
def quick_sort(data,low,high):
    if low >= high:
        return data

    low_save = low
    high_save = high
    key = data[low]
    while(low < high):

        while(low < high and data[high] >= key):
            high -= 1
        if low < high:
            data[low] = data[high]

        while(low < high and data[low] < key):
            low += 1
        if low < high:
            data[high] = data[low]

    data[high] = key
    quick_sort(data,low_save,low)
    quick_sort(data,low+1,high_save)
    return data

if __name__ == '__main__':
    data = [1,4,5,6,3,2,7,9,0]
    data = quick_sort(data,0,len(data)-1)
    print(data)
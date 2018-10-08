# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: quick_sort.py
# description:

import numpy as np
import copy


# why low != right
# when low = right, the element of data[left] would be changed twice, one time for low and another for high
def quick_sort(data,left,right):
    if left >= right:
        return data

    low = left
    high = right

    key = data[low] # save the key
    while(low < high):

        try:
            # because data[low] has been saved before and data[low] could be landed
            # find first element with lower value than key
            while(data[high] >= key and low < high):
                high -= 1
            data[low] = data[high]

        except Exception:
            print('low',low)
            print('high',high)

        try:
            # find first element with bigger value than key
            while(data[low] <= key and low < high):
                low += 1
            data[high] = data[low]
        except Exception:
            print('low',low)
            print('high',high)

    data[low] = key
    print('===================')
    print('left',left)
    print('right',right)
    print('key',key)
    print(data)
    quick_sort(data,left,low - 1)
    quick_sort(data,low + 1,right)
    return data


if __name__ == '__main__':
    data = np.random.rand(10)
    data = quick_sort(data,0,len(data)-1)
    print(data)
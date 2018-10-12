# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/11/18
# file: 调整数组顺序使奇数位于偶数前面.py
# description:

'''
  [1,4,5,6,7,3,2]
    调整成
  [1,5,7,3,4,6,2]
'''
import numpy as np

def adjust(data):
    if data == None or len(data) == 0:
        return

    if len(np.unique(data)) == 1:
        return data

    i = 0
    j = len(data) - 1
    while(i < j):
        while(data[i] % 2 != 0):
            i += 1
        while(data[j] % 2 == 0):
            j -= 1
        if i < j:
            data[i],data[j] = data[j],data[i]
    return data

if __name__ == '__main__':

    data = [1,4,5,6,7,3,2]
    print(adjust(data))

    data = []
    print(adjust(data))

    data = [1]
    print(adjust(data))

    data = [1,1,1,1,1,1]
    print(adjust(data))

    data = [1,1,1,1,1,2,2,2,2,2]
    print(adjust(data))

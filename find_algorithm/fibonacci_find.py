# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: fibonacci_find.py
# description:

import numpy as np

def create_fibonacc():
    a = [0,1]
    for i in range(2,20):
        a.append(a[i-1]+a[i-1])
    return a

def fibonacc_find(data,v):

    low = 0
    high = len(data)-1

    F = create_fibonacc()

    # find the clostest number
    k = 1
    while(high > F[k]-1):
        k +=1

    # make up the data array
    for _ in range(len(data),F[k]-1):
        data.append(data[len(data)-1])

    while(low < high):
        mid = np.int(low + F[k-1]-1)
        if data[mid] == v:
            return mid
        if data[mid] < v:
            low = mid
            k -= 2
        else:
            high = mid
            k -=1

    return -1

if __name__ == '__main__':
    data = np.random.rand(10)
    data = sorted(data)
    inx = fibonacc_find(data,data[7])
    print(inx)

# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: fibonacci_find.py
# description:

import numpy as np

def create_fa():
    res = [1, 1]
    for i in range(1, 20):
        res = res[i - 1] + res[i - 2]
    return res


def fa_find(arr, n, val):
    F = create_fa()

    low, high = 0, n - 1
    k = 0
    while high > F[k] - 1:
        k += 1

    arr = arr + [arr[-1]] * (F[k] - 1 - n)

    while low < high:
        mid = low + F[k - 1] - 1
        #这里有两种情况， 1：可能是补全的值 2：可能是正常值， 用位置n-1做个判断
        if arr[mid] == val:
            if mid < n:
                return mid
            else:
                return n-1
        elif arr[mid] < val:
            low = mid
            k -= 2
        else:
            high = mid - 1
            k -= 1
    return -1


if __name__ == '__main__':
    data = np.random.rand(10)
    data = sorted(data)
    inx = fibonacc_find(data,data[7])
    print(inx)

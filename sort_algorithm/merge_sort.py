# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: merge_sort.py
# description:
import numpy as np

def merge(left,right):
    i,j = 0,0
    res = []
    while(i < len(left) and j < len(right)):
        # only compare one time
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    # if here be res.append(left[i:])
    # result would be res=[xx,xx,[xx]]
    # because the left elements of left or right array would be list
    if i < len(left):
        res += left[i:]
    if j < len(right):
        res += right[j:]
    return res

def merge_sort(data):
    if len(data) == 1:
        return data
    mid = np.int(len(data)/2)
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left,right)


if __name__ == '__main__':
    data = np.random.rand(10)
    data = merge_sort(list(data))
    print(data)
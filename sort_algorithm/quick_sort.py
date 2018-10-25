# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: quick_sort.py
# description:

import numpy as np
import copy

# 递归操作
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

# 非递归操作
def quick_sort_stack(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr

    stack = []
    stack.append(len(arr)-1) # 添加high
    stack.append(0) # 添加low
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)

def partition(arr, low, high):
    # 分区操作，返回基准线下标
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]
    # 此时start = end
    arr[low] = key # low 此时是在中间的位置
    return low



if __name__ == '__main__':
    data = [1,4,5,6,3,2,7,9,0]
    data = quick_sort(data,0,len(data)-1)
    print(data)
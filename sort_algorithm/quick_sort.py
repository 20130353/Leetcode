# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: quick_sort.py
# description:

import numpy as np
import copy


# 递归操作
def quick_sort(arr, low, high):
    if low >= high:
        return arr
    low_save = low
    high_save = high
    mid = partition(arr, low, high)
    quick_sort(arr, low_save, mid - 1)
    quick_sort(arr, mid + 1, high_save)
    return arr


# 非递归操作
def quick_sort_stack(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr

    stack = []
    stack.append((0, len(arr) - 1))  # 添加high
    while stack:
        l, r = stack.pop()
        mid = partition(arr, l, r)
        if l < mid - 1:
            stack.append((mid - 1, 1))
        if r > mid + 1:
            stack.append(r, mid + 1)


def partition(arr, low, high):
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        if low < high:
            arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        if low < high:
            arr[high] = arr[low]
    arr[low] = key
    return low


if __name__ == '__main__':
    data = [1, 4, 5, 6, 3, 2, 7, 9, 0]
    data = quick_sort(data, 0, len(data) - 1)
    print(data)

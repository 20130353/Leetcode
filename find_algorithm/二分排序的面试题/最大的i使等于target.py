# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/25/18
# file: 最大的i使等于target.py
# description:


def find(data, target):
    if len(data) <= 0:
        return -1
    low,high = 0, len(data)-1
    while low < high:
        # 同时在这里 多 加 1, 因为如果不加1 会出现死循环的状态
        mid = int((low + high + 1)/2)
        # mid = low + (high - low) >> 2 在python中不可以这么做...为什么?
        if data[mid] > target:
            high = mid - 1
        else:
            # data[mid] >= target
            # 这边可能会出现等于的情况
            # 如果D[mid] == target的话 low 就会一直不变
            # 所以low的作用的是一直守着第一个等于target的mid位置
            # 在等于的时候不变
            low = mid
    if data[low] != target:
        return -1
    else:
        return low

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,8,8,8,9]
    i = find(data,8)
    print(i)
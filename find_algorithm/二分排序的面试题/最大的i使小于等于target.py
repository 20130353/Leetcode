# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/25/18
# file: 最大的i使小于等于target.py
# description:
'''
    给定数组,找一个最大的i使其小于等于target
'''

def find(data, target):
    if len(data) <= 0:
        return -1
    low,high = 0, len(data)-1
    while low < high:
        mid = int((low + high)/2)
        # mid = low + (high - low) >> 2 在python中不可以这么做...为什么?
        if data[mid] < target:
            low = mid + 1
        else:
            # data[mid] >= target
            # 这边可能会出现等于的情况
            # 如果D[mid] == target的话 high 就会一直不变
            # 所以high的作用的是一直守着第一个等于target的mid位置
            # 直到low > high 所以,low 就是一个第一个等于target的位置
            high = mid #
    if data[low] != target:
        return -1
    else:
        return low

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,8,8,8,9]
    i = find(data,8)
    print(i)
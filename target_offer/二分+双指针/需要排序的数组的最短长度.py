# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/24/18
# file: 需要排序的数组的最短长度.py
# description:

'''
    给定与ige数组,确定需要排序的区域长度
'''

from numpy import argmin,argmax
import math
def fun(data):
    if len(data) <= 0 or data == None:
        return 0,0

    min_pos = 0
    for i in range(len(data)):
        if argmin(data[i:]) != 0:
            min_pos = i
            break
    if min_pos == len(data) - 1:
        return 0,0

    max_pos = 0
    for j in range(len(data)-1,0,-1):
        if argmax(data[:j+1]) != len(data[:j+1])-1:
            max_pos = j
            break
    return min_pos,max_pos


if __name__ == '__main__':
    data = []
    data = [1,5,4,3,2,6,7]
    # data = [1,2,3]
    # data = [5,4,3,2,1,10,7,8,9]

    num = fun(data)
    print(num)
# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: bubble_sort.py
# description:

import numpy as np
import random
import copy
# native bubble_sort
def bubble_sort(data):

    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]<data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

# if data is order then stop the sort
def bubble_sort_1(data):

    flag = True
    for i in range(len(data)):
        if flag == False:
            return data
        flag = False
        for j in range(i+1,len(data)):
            if data[i]<data[j]:
                flag = True
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

# if data is order then stop the sort
# the order data is not needed to compare
def bubble_sort_2(data):

    flag = True
    for i in range(len(data)):
        if flag == False:
            return data
        flag = False
        for j in range(i+1,len(data)):
            if data[i]<data[j]:
                flag = True
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data



if __name__ == '__main__':

    data = np.random.rand(10)

    sort_data = bubble_sort(copy.deepcopy(data))
    print(sort_data)

    sort_data = bubble_sort_1(copy.deepcopy(data))
    print(sort_data)

    sort_data = bubble_sort_2(copy.deepcopy(data))
    print(sort_data)
# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: shell_sort.py
# description:

import numpy as np
import copy

# native bubble_sort
def shell_sort(data):
    # 希尔排序
    count = len(data)
    step = 2
    group = np.int(count / step)
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count: # group each
                # k is j in insert sort
                k = j - group
                key = data[j]
                while k >= 0:
                    if data[k] > key:
                        data[k + group] = data[k]
                        data[k] = key
                    k -= group
                j += group #each group has one element
        group = np.int(group / step)
    return data


def shell_sort_1(data):
    step = np.int(len(data)/2)# each group has two elements
    while(step):
        for i in range(step):
            j = i + step # start element + step =
            while j < len(data): #promise element of
                key = data[j]
                k = j - step # element before the data[j]
                while k >= 0:
                    if data[k] > key:
                        data[k + step] = data[k]
                        data[k] = key
                    k -= step
                j +=step
        step = np.int(step/2)
    return data

if __name__ == '__main__':

    data = np.random.rand(10)

    sort_data = shell_sort(copy.deepcopy(data))
    print(sort_data)


    sort_data = shell_sort_1(copy.deepcopy(data))
    print(sort_data)

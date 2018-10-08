# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: insert_sort.py
# description:

import numpy as np
import copy


# native bubble_sort
def insert_sort(data):
    new_data = []
    for i in range(len(data)):

        if len(new_data) == 0:
            new_data.append(data[i])
            continue

        flag = False
        for j in range(len(new_data)):
            if data[i] < new_data[j]:
                new_data = list(new_data[:j]) + [data[i]] + list(new_data[j:])
                flag = True
                break

        if flag == False:
            new_data.append(data[i])

    return new_data


def insert_sort_1(data):
    # 插入排序
    count = len(data)
    for i in range(1, count):
        key = data[i]
        j = i - 1
        # walk forward
        while j >= 0:
            if data[j] > key:
                data[j + 1] = data[j]
                data[j] = key
            j -= 1
    return data


if __name__ == '__main__':

    data = np.random.rand(10)

    sort_data = insert_sort(copy.deepcopy(data))
    print(sort_data)

    sort_data = insert_sort_1(copy.deepcopy(data))
    print(sort_data)
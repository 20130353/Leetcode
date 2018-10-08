# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: heap_sort.py
# description:


import numpy as np
import copy

# data in python is object and could be modified anywhere
# heap sort looks like the quick sort
def build_heap(data,size):
    for i in range(np.int(size/2),0,-1):
        adjust_heap(data,i,size)

def adjust_heap(data, i, size):
    # define the indices of child nodes
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    max = i
    if i < size/2:
        # select maximum node of two child nodes
        if left_child < size and data[left_child] > data[max]:
            max = left_child
        if right_child < size and data[right_child] > data[max]:
            max = right_child
        if max != i:
            data[max],data[i] = data[i],data[max]
            adjust_heap(data,max,size)

def heap_sort(data):
    build_heap(data,len(data))
    for i in range(len(data)-1,0,-1):
        data[i],data[0] = data[0],data[i] # take off the min value from the heap
        adjust_heap(data,0,i) # adjust heap into order heap


if __name__ == '__main__':
    data = np.random.rand(10)
    heap_sort(data)
    print(data)
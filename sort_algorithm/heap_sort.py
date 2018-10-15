# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: heap_sort.py
# description:


import numpy as np
import copy

# 初始数据是随机数据,要把所有数据调整调整成最大堆
# 调整堆只要调整所有的父节点,使父节点是最大值就好
def build_heap(data):
    last_father = np.int(len(data)/2)
    for i in range(last_father,-1,-1):
        adjust_heap(data,i,len(data))

# # 从底部将最大值上浮到父节点
# # 树调整的过程是递归的,因为左右孩子节点的值会影响父节点的值.
# # 调整的时候,当前的节点以及当前的所有父节点会经历一次最大值向上的排序
#
# 递归方式
def adjust_heap(data, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    max = i
    if left < size and data[max] < data[left]:
        max = left
    if right < size and data[max] < data[right]:
        max = right
    if max != i:
        data[max], data[i] = data[i], data[max]
        adjust_heap(data, max, size)  # 从当前节点向上调整
    return

# 非递归算法
# def adjust_heap(data,i,size):
#
#     while(1):
#         left = 2 * i + 1
#         right = 2 * i + 2
#         max = i
#         if left < size and data[max] < data[left]:
#             max = left
#         if right < size and data[max] < data[right]:
#             max = right
#         if max != i:
#             data[max], data[i] = data[i], data[max]
#             i = max
#         else:
#             break

# # 堆排序的过程就是不断把堆顶元素拿走,调整剩下堆的过程.
def heap_sort(data):
    build_heap(data)
    for i in range(len(data)-1,0,-1):
        data[0],data[i] = data[i],data[0]
        adjust_heap(data,0,i)

if __name__ == '__main__':
    data = [1,3,4,6,7,2,8]
    heap_sort(data)
    print(data)


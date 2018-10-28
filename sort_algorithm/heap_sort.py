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
    # 构造堆是底部的孩子节点开始的
    # 从孩子节点开始向上浮动最大值
    for i in range(last_father,-1,-1):
        adjust_heap(data,i,len(data))

# 构造和调整的过程完全相反,构造是从底部开始调整,因为整棵树都是乱序的.
# 调整就是从根节点开始,因为之前整棵树都是有序的,但是新加进来的节点不符合要求,只要把新进来的节点下沉到合适的位置
# 构造和调整的关系是构造每个节点时就从当前节点开始调整堆
# 递归方式
def adjust_heap(data, i, size):

    # 从根节点开始排,一直到底部孩子节点
    # max最后的结果是孩子节点
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
        # data[0]是最大元素, data[i]是当前的最小元素
        data[0],data[i] = data[i],data[0]
        adjust_heap(data,0,i)

if __name__ == '__main__':
    data = [1,3,4,6,7,2,8]
    heap_sort(data)
    print(data)


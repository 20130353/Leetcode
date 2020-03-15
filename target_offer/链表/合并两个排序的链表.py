# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/12/18
# file: 合并两个排序的链表.py
# description:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_node(T, data):
    if T == None:
        return Node(data)
    else:
        T.next = insert_node(T.next, data)
    return T


def merge_list(T1, T2):
    if T1 == None and T2 == None:
        return

    if T1 == None:
        return T2

    if T2 == None:
        return T1

    T = None
    while (T1 != None and T2 != None):
        if T1.data <= T2.data:
            T = insert_node(T, T1.data)
            T1 = T1.next
        else:
            T = insert_node(T, T2.data)
            T2 = T2.next
    if T1 != None:
        while (T1 != None):
            T = insert_node(T, T1.data)
            T1 = T1.next
    if T2 != None:
        while (T2 != None):
            T = insert_node(T, T2.data)
            T2 = T2.next
    return T


if __name__ == '__main__':

    # data1 = [1,3,5,7]
    # data2 = [2,4,6]

    # data1 = []
    # data2 = []
    #
    # data1 = []
    # data2 = [1,2,3]
    #
    # data1 = [5,6,7]
    # data2 = [1,2,3]
    # #

    data1 = [5, 5, 5, 5, 5, 6, 7]
    data2 = [1, 2, 3, 5, 5, 5]

    T1 = None
    for each in data1:
        T1 = insert_node(T1, each)

    T2 = None
    for each in data2:
        T2 = insert_node(T2, each)

    T = merge_list(T1, T2)
    while (T):
        print(T.data, end=' ')
        T = T.next

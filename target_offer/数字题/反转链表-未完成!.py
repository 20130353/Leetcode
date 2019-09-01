# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/12/18
# file: 反转链表-未完成!.py
# description:

'''
    定义一个函数,输入一个链表的头节点,反转该链表并输出反转后的链表的头节点
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def build_node(T,data):
    if T == None:
        return Node(data)
    else:
        return build_node(T.next,data)

der reverse_list():

    return


if __name__ == '__main__':
    data = []

    # data = [1]
    #
    # data = [1,2,3,4]

    T = None
    for each in data:
        T = build_node(T,each)




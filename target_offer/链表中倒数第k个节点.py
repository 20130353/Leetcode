# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/12/18
# file: 链表中倒数第k个节点.py
# description:

'''
    输入一个链表,输出该链表中倒数第k个节点
    eg:
    1,2,3,4,5,6, 链表的倒数第3个节点是4
    如果先遍历到尾节点,然后在重复数到n-k+1个节点的方法太笨了,不推荐使用
    所以使用多余的一个节点记住之前的位置

    相关题目有输出中间节点和链表是否是循环链表
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def out_reciprocal_node(T,k):
    if T == None or T.next == None or k <= 0:
        return T
    count = 1
    node_k = None
    while(T.next != None):
        if count == 1:
            node_k = T
        if count >= k and node_k != None:
            node_k = node_k.next
        T = T.next
        count += 1
    return node_k

def build_tree(T,data):
    if T == None:
        T = Node(data)
    else:
        T.next = build_tree(T.next,data)
    return T

if __name__ == '__main__':

    data = [1,2,3,4,5,6]
    T = None
    for each in data:
        T = build_tree(T,each)

    reciprocal_node = out_reciprocal_node(T,10)
    if reciprocal_node != None:
        print(reciprocal_node.data)
    else:
        print('None')
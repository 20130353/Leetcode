# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 按之字形打印二叉树.py
# description:

'''
     按照之字形打印二叉树就是在奇数层从左向右打印,在偶数层从右向左打印
     只要记录当前层是奇数还是偶数
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def zhi_print(T):

    count = 0
    queue = [T]
    while(len(queue)):
        count += 1
        res = []
        size = len(queue)
        while(size):
            top = queue[0]
            del queue[0]
            res.append(top.data)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
            size -= 1

        if count & 1 == 0: # 偶数
            for each in res[::-1]:
                print(each,end='\t')
            print('\n')
        else:
            for each in res:
                print(each,end='\t')
            print('\n')
    return

if __name__ == '__main__':
    root = Node(1)
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    Node6 = Node(6)
    Node7 = Node(7)
    root.left = Node2
    root.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Node3.left = Node6
    Node3.right = Node7

    zhi_print(root)

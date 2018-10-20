# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: 二叉树的深度.py
# description:

'''
    求二叉树的深度有两种解法:
    递归: 返回左右节点的最大深度 + 当前深度1
    非递归: 用二叉树的层次遍历,返回深度
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def deepth(T):
    if T == None:
        return 0
    else:
        return max(deepth(T.left),deepth(T.right)) + 1


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


    max_deepth = deepth(root)
    print(max_deepth)
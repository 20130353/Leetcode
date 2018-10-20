# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 对称的二叉树.py
# description:
'''
    对称的二叉树就是判断二叉树是否和二叉树的镜像相同,如果相同就是对称二叉树,如果不相同就不是对称二叉树
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def judge(T):
    if T == None:
        return False
    else:
        return judge_tree(T,T)


def judge_tree(T1,T2):
    if T1 == None and T2 == None:
        return True
    if T1 == None or T2 == None:
        return False
    if T1.data != T2.data:
        return False

    res1 = judge_tree(T1.left,T2.right)
    res2 = judge_tree(T1.right,T2.left)
    return res1 and res2

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
    #
    # res = judge_tree(root,root)
    # if res:
    #     print('Yes')
    # else:
    #     print('No')

    # root = Node(10)
    # Node11 = Node(11)
    # root.left = Node11
    # root.right = Node11

    res = judge(root)
    if res:
        print('Yes')
    else:
        print('No')



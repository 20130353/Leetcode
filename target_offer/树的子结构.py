# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/12/18
# file: 树的子结构.py
# description:

'''
    输入两个二叉树A和B,判断B是不是A的子结构
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

def search_root(T,data):

    if T == None:
        return False
    if T.data == data:
        return T,None


    return

def AhasB(A,B):
    if B == None:
        return True
    if A == None:
        return False
    if A.data != B.data:
        return False
    return AhasB(A.lchild,B.lchild) and AhasB(A.rchild,B.rchild)

def judge(A,B):
    result = False
    if A != None and B!= None:
        if A.data == B.data:
            result = AhasB(A,B)
        if result == False:
            result = judge(A.lchild,B)
        if result == False:
            result = judge(A.rchild,B)
    return result

if __name__ == '__main__':

    pRoot1 = Node(8)
    pRoot2 = Node(8)
    pRoot3 = Node(7)
    pRoot4 = Node(9)
    pRoot5 = Node(2)
    pRoot6 = Node(4)
    pRoot7 = Node(7)
    pRoot1.lchild = pRoot2
    pRoot1.rchild = pRoot3
    pRoot2.lchild = pRoot4
    pRoot2.rchild = pRoot5
    pRoot5.lchild = pRoot6
    pRoot5.rchild = pRoot7

    pRoot8 = Node(8)
    pRoot9 = Node(9)
    pRoot10 = Node(2)
    pRoot8.lchild = pRoot9
    pRoot8.rchild = pRoot10

    print(judge(pRoot1,pRoot8))
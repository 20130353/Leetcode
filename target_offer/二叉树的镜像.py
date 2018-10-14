# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 二叉树的镜像.py
# description:


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

def mirroring(T):
    if T == None:
        return

    T.lchild = mirroring(T.lchild)
    T.rchild = mirroring(T.rchild)
    T.lchild,T.rchild = T.rchild,T.lchild

    return T

# preOrder每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点，访问其右子树。
# 在同一层中，不可能同时有两个节点压入栈，因此栈的大小空间为O(h)，h为二叉树高度。
# 时间方面，每个节点都被压入栈一次，弹出栈一次，访问一次，复杂度为O(n)。
def pre_visit(T):
    if T == None:
        return

    stack = []
    node = T
    while node or stack:
        while node:
            print(node.data)
            stack.append(node)
            node = node.lchild # 遍历完所有的左子树

        node = stack.pop()
        node = node.rchild #访问右子树

# 中序和先序就是打印的顺序不一样而已
def in_visit(T):
    if T == None:
        return
    stack = []
    node = T
    while node or stack:
        while(node):
            stack.append(node)
            node = node.lchild
        node = stack.pop()
        print(node.data)
        node = node.rchild

def post_visit(T):
    if T == None:
        return

    stack = [T]
    p = T
    back_up = []
    while stack:
        node = stack.pop()
        if node.lchild:
           stack.append(node.lchild)
        if node.rchild:
            stack.append(node.rchild)
        back_up.append(node.data)

    for each in back_up[::-1]:
        print(each,end='\t')

def level_visit(T):
    if T == None:
        return
    queue = [T]
    while queue:
        node = queue.pop(0)
        print(node.data,end='\t')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


if __name__ == '__main__':

    pRoot1 = Node(1)
    pRoot2 = Node(2)
    pRoot3 = Node(3)
    pRoot4 = Node(4)
    pRoot5 = Node(5)
    pRoot6 = Node(6)
    pRoot7 = Node(7)
    pRoot1.lchild = pRoot2
    pRoot1.rchild = pRoot3
    pRoot2.lchild = pRoot4
    pRoot2.rchild = pRoot5
    pRoot3.lchild = pRoot6
    pRoot3.rchild = pRoot7

    T = mirroring(pRoot1)
    level_visit(T)

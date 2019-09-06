# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/9/18
# file: 二叉树的遍历.py
# description:


import numpy as np

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def preorder_traverse(self,T):
        if T != None:
            print(T.data)
            self.preorder_traverse(T.lchild)
            self.preorder_traverse(T.rchild)

    def inorder_traverse(self,T):
        if T != None:
            self.inorder_traverse(T.lchild)
            print(T.data)
            self.inorder_traverse(T.rchild)

    def postorder_traverse(self,T):
        if T != None:
            self.postorder_traverse(T.lchild)
            self.postorder_traverse(T.rchild)
            print(T.data)

    # 前序和后序的区别就是放入节点的顺序不一样
    # 中序是一直把所有的左孩子放入栈中
    # 层次遍历和前中后序遍历的差别是层次遍历是队列,前中后序遍历是栈
    def pre_vis(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return res

    def in_vis(self, root):

        if not root:
            return []

        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def post_vis(self,root):

        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            top = stack.pop()
            res.insert(0,top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return res

    # 反思:
    # 1. queue进行弹出操作的时候注意queue是否为空. 栈也是同理!
    # 2. 没有返回函数值
    def level_vis(self, root):

        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            top = queue.pop(0)
            res.append(top.val)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return res


if __name__ == '__main__':

    root = Node(0)
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

    so = Solution()
    print(so.post_vis(root))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树的层次遍历.py
# @Author: smx
# @Date  : 2019/8/22
# @Desc  :


class NodeL:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solution(root):
    if root is None:
        return root

    queue = [root]
    while len(queue) != 0:
        size = len(queue)
        while size > 0:
            top = queue.pop()
            print(top.val)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
            size -= 1
        print('第。。。。层')
    return

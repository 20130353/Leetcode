#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树的右视图.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            length = len(queue)
            while length:
                top = queue.pop(0)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                if length == 1:
                    ans.append(top.val)
                length -= 1
        return ans


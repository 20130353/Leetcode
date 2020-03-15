#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树的层次遍历.py
# @Author: smx
# @Date  : 2019/8/22
# @Desc  :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []

        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            temp_ans = []
            while size > 0:
                top = queue.pop(0)
                temp_ans.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                size -= 1
            ans.insert(0, temp_ans)
        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树的遍历.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :

# Definition for a binary tree TreeNode.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = [root]
        ans = []
        count = 0
        while queue:
            count += 1
            values = []
            size = len(queue)
            while size:
                top = queue.pop(0)
                values.append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
                size -= 1
            if count % 2 == 0:
                ans.append(values[::-1])
            else:
                ans.append(values)
        return ans


if __name__ == '__main__':
    root = TreeNode(0)
    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)
    TreeNode4 = TreeNode(4)
    TreeNode5 = TreeNode(5)
    TreeNode6 = TreeNode(6)
    TreeNode7 = TreeNode(7)

    root.left = TreeNode2
    root.right = TreeNode3
    TreeNode3.left = TreeNode6
    TreeNode3.right = TreeNode7

    ans = Solution().zigzagLevelOrder(root)
    print(ans)

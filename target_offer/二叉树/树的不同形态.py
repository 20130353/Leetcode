#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 树的不同形态.py
# @Author: smx
# @Date  : 2019/10/16
# @Desc  :

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def pre_vis(self, T):
        if not T:
            return []

        ans = []
        stack = [T]
        while stack.__len__() != 0:
            top = stack.pop()
            ans.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return ans

    def post_vis(self, T):
        if not T:
            return []

        ans = []
        stack = [T]
        while stack.__len__() != 0:
            top = stack.pop()
            ans.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return ans[::-1]

    # 需要保证没有重复元素
    def build_tree(self, level, mid, leaves):
        if not level or not mid:
            return None
        if len(level) == 1 and len(mid) == 1:
            leaves.append(level[0])
            return Node(level[0])

        cur = level.pop(0)
        left_mid = mid[:mid.index(cur)]
        right_mid = mid[mid.index(cur) + 1:]
        left_level = [each for each in level if each in left_mid]
        right_level = [each for each in level if each in right_mid]

        node = Node(cur)
        node.left = self.build_tree(left_level, left_mid, leaves)
        node.right = self.build_tree(right_level, right_mid, leaves)
        return node


if __name__ == '__main__':
    level = list(map(int, input().strip().split(' ')))
    mid = list(map(int, input().strip().split(' ')))
    solution = Solution()
    leaves = []
    T = solution.build_tree(level, mid, leaves)
    pre_ans = solution.pre_vis(T)
    post_ans = solution.post_vis(T)
    print(' '.join(map(str, leaves)))
    print(' '.join(map(str, pre_ans)))
    print(' '.join(map(str, post_ans)))

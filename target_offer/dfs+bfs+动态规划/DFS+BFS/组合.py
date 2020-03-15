#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 组合.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

import copy as cp

# 组合元素个数等于指定值
# 如果用组合数公式，可以知道个数，但是不知道具体的组合结果！

# 01背包
class Solution:
    # 没有重复元素
    def DFS(self, n, target, cur_arr, pos, ans):
        if cur_arr.__len__() == target:
            ans.append(cp.copy(cur_arr))
            return
        if pos >= n:
            return

        cur_arr.append(pos + 1)
        self.DFS(n, target, cur_arr, pos + 1, ans)

        cur_arr.pop()
        self.DFS(n, target, cur_arr, pos + 1, ans)

    def combine(self, n, k):
        ans = []
        self.DFS(n, k, [], 0, ans)
        return ans


if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().combine(n, k))

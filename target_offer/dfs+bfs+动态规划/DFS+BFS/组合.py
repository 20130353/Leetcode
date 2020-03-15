#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 组合.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

import copy as cp


class Solution:
    # 没有重复元素
    def DFS(self, n, k, cur, pos, ans):
        if cur.__len__() == k:
            ans.append(cp.copy(cur))
            return
        if pos >= n:
            return

        cur.append(pos + 1)
        self.DFS(n, k, cur, pos + 1, ans)
        cur.pop()
        self.DFS(n, k, cur, pos + 1, ans)

    def combine(self, n, k):
        ans = []
        self.DFS(n, k, [], 0, ans)
        return ans


if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().combine(n, k))

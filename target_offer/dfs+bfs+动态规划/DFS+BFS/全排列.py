#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 全排列.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

import copy as cp
class Solution:
    def DFS(self, arrs, vis, n, pos, cur, ans):
        if pos >= n:
            if cur: ans.append(cp.copy(cur))
            return

        for i in range(n):
            if vis[i] == 0:
                cur.append(arrs[i])
                vis[i] = 1
                self.DFS(arrs, vis, n, pos + 1, cur, ans)
                vis[i] = 0
                cur.pop()

    def permute(self, arrs):
        ans = []
        n = len(arrs)
        vis = [0 for _ in range(n)]
        self.DFS(arrs, vis, len(arrs), 0, [], ans)
        return ans


if __name__ == '__main__':
    arr = [1, 1, 2]
    print(Solution().permute(arr))

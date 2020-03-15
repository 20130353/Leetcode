#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 组合.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 使用一次
class Solution:
    def DFS(self, arrs, n, vis, target, cur, cur_sum, ans):
        if cur_sum == target:
            if sorted(cur) not in ans:
                ans.append(sorted(cur))
            return

        for i, each in enumerate(arrs):
            if cur_sum + each <= target and vis[i] == 0:
                vis[i] = 1
                cur.append(each)
                self.DFS(arrs, n, vis, target, cur, cur_sum + each, ans)
                cur.pop()
                vis[i] = 0

    def combinationSum2(self, arrs, target):
        ans = []
        n = arrs.__len__()
        vis = [0 for _ in range(n)]
        self.DFS(arrs, len(arrs), vis, target, [], 0, ans)
        return ans


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))

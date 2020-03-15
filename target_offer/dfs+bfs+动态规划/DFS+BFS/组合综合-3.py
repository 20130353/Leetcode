#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 组合综合-3.py
# @Author: smx
# @Date  : 2020/2/20
# @Desc  :


class Solution:
    def DFS(self, n, k, vis, cur, cur_sum, pos, ans):
        if pos >= k:
            if cur_sum == n:
                sorted_cur = sorted(cur)
                if sorted_cur not in ans:
                    ans.append(sorted_cur)
            return

        for i in range(9):
            if vis[i] == 0 and (i + 1) + cur_sum <= n:
                cur.append(i + 1)
                vis[i] = 1
                self.DFS(n, k, vis, cur, cur_sum + i + 1, pos + 1, ans)
                cur.pop()
                vis[i] = 0

    def combinationSum3(self, k, n):
        vis = [0 for _ in range(9)]
        ans = []
        self.DFS(n, k, vis, [], 0, 0, ans)
        return ans


if __name__ == '__main__':
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))

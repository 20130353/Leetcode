#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 子集.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 不用copy的方法是每次传递都是新的元素
# 为什么不用这方法？
import copy as cp
class Solution:
    def DFS(self, arrs, n, pos, cur, ans):
        if pos >= n:
            ans.append(cp.copy(cur))
            return

        cur.append(arrs[pos])
        self.DFS(arrs, n, pos + 1, cur, ans)

        cur.pop()
        self.DFS(arrs, n, pos + 1, cur, ans)

    def subsets(self, arrs):
        ans = []
        self.DFS(arrs, len(arrs), 0, [], ans)
        return ans


class Solution:
    # 这样写就和全排列的思路是一样的！
    def DFS(self, arrs, n, start, cur, ans):
        ans.append(cur)
        for j in range(start, n):
            self.DFS(arrs, n, j + 1, cur + [arrs[j]], ans)

    def subsets(self, arrs):
        n = len(arrs)
        ans = []
        self.DFS(arrs, n, 0, [], ans)
        return ans


if __name__ == '__main__':
    arrs = []
    print(Solution().subsets(arrs))

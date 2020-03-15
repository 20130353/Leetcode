#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 子集升级版.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 包含重复元素
# 最后结果去重！
# 分清楚是子集重复是指元素是相同的。
# 去重的两大要素是map和排序

import copy as cp


class Solution:
    def DFS(self, arrs, n, pos, cur, ans):
        if pos >= n:
            if cur not in ans:
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

        # 这样只能保证[4,4],第二位的4只有一个选择，而不是来自后面的几种选择
        # 如果不排序，在新位置上相当于是新元素
        dup = set()
        for i in range(start, n):
            if arrs[i] not in dup:
                dup.add(arrs[i])
                self.DFS(arrs, n, i + 1, cur + [arrs[i]], ans)

    def subsetsWithDup(self, arrs):
        n = len(arrs)
        ans = []
        self.DFS(sorted(arrs), n, 0, [], ans)
        return ans


if __name__ == '__main__':
    arrs = [4, 4, 4, 1, 4]
    print(Solution().subsetsWithDup(arrs))

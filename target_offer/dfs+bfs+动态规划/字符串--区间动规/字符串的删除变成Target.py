#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串的删除变成Target.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :

# 把S变成T的方案数
# 不是特别理解：为什么相等的时候就不需要删除 --》 因为最终结果是变成相等，所以已经相等就不需要删除了
# 但是为什么没有j-1 -》 因为目标是T，不能修改T

class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(0, m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[m][n]

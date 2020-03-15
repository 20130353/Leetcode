#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数字拆分.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :

class Solution:
    def integerBreak(self, n):
        dp = [1 for _ in range(n + 1)]
        if n == 2: return 1
        dp[2] = 2
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j)
            if i < n and i > dp[i]: dp[i] = i
        return dp[n]


if __name__ == '__main__':
    n = 10
    print(Solution().integerBreak(n))

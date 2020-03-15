#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 硬币.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :

# 典型的背包方案问题
# 注意加方案的时候不加一！！！！
class Solution:
    def waysToChange(self, n):
        if n <= 1: return 1
        dp = [1] + [0 for _ in range(n)]
        coins = [1, 5, 10, 25]
        for i in range(4):
            for j in range(coins[i], n + 1):
                dp[j] += dp[j - coins[i]]
        return dp[n] % 1000000007


if __name__ == '__main__':
    n = 10
    print(Solution().waysToChange(n))

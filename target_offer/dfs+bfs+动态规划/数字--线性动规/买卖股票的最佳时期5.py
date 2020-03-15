#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 买卖股票的最佳时期5.py
# @Author: smx
# @Date  : 2020/2/23
# @Desc  :

# 包含手续费
class Solution:
    def maxProfit(self, arrs, fee):
        if not arrs: return 0
        n = len(arrs)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -arrs[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + arrs[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - arrs[i])
        return max(dp[n - 1])


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices, fee))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 买卖股票的最佳时期2.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :

# 1. 暴力遍历每种情况
# 2. 贪心算法，每次只要有正数就买入加
# 3. 动态规划，计算到第i天的收益，问题是不知道怎么计算收益，买入的时候收益-股票价格，卖出的时候收益+股票价格！
class Solution:
    def maxProfit(self, arrs):
        if not arrs: return 0
        n = len(arrs)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -arrs[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + arrs[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - arrs[i])
        return max(dp[n - 1])


if __name__ == '__main__':
    arrs = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(arrs))

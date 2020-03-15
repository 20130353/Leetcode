#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 买卖股票的最佳时期2.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :

# 加入最多只能完成两笔交易的限制
# 1. 暴力遍历每种情况
# 2. 贪心算法，每次只要有正数就买入加
# 3. 动态规划，计算到第i天的收益，问题是不知道怎么计算收益，买入的时候收益-股票价格，卖出的时候收益+股票价格！
# 增加了冷冻期，添加了一个状态转化！


class Solution:
    def maxProfit(self, arrs):
        if not arrs: return 0
        n = len(arrs)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][1] = -arrs[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + arrs[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - arrs[i])
            dp[i][2] = dp[i - 1][0]
        return max(dp[n - 1])


if __name__ == '__main__':
    arrs = [2, 1, 4]
    print(Solution().maxProfit(arrs))

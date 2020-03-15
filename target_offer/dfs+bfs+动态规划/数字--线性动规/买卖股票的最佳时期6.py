#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 买卖股票的最佳时期5.py
# @Author: smx
# @Date  : 2020/2/23
# @Desc  :

# 完成k笔交易！
# 在增加一个维度！
class Solution:
    def maxProfit(self, k, arrs):
        if not arrs: return 0
        if k <= 0: return 0
        # 次数非常多，所以可以编程之前的状态
        if k >= len(arrs) // 2: return self.max_nprofit(arrs)

        n = len(arrs)
        # 把有股票还是没有股票都放在最后，这样保证状态清楚

        # 保证最开始持股是负数
        dp = [[[0, 0] for _ in range(k)] for _ in range(n)]
        for i in range(n):
            for j in range(k):
                dp[i][j][1] = -0xfffff

        for i in range(n):
            for j in range(k):
                if i == 0:
                    dp[i][j][1] = -arrs[i]
                else:
                    if j == 0:
                        dp[i][j][1] = max(dp[i - 1][j][1], -prices[i])
                    else:
                        # 状态方程1
                        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                # 状态方程2
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
        return max(dp[n - 1][k - 1])

    def max_nprofit(self, arrs):
        if not arrs: return 0
        n = len(arrs)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -arrs[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + arrs[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - arrs[i])
        return max(dp[n - 1])


if __name__ == '__main__':
    prices = [2, 1, 4, 5, 2, 9, 7]
    k = 2
    print(Solution().maxProfit(k, prices))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 一和零.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :

# 背包变种：改变重量的个数，由原来的一个变成两个
class Solution:
    def findMaxForm(self, arrs, m, n):
        sarrs = sorted(arrs, key=lambda x: len(x))
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 遍历物品的循环应该放在前面！
        # 背包的遍历是：物品，重量
        for inx, each in enumerate(sarrs):
            num0 = each.count('0')
            num1 = each.count('1')
            # 从大循环开始避免被重复使用，因为大循环肯定包含小循环的物品，但是小循环一定不包含大循环的物品
            for i in range(m, num0 - 1, -1):
                for j in range(n, num1 - 1, -1):
                    dp[i][j] = max(dp[i - num0][j - num1] + 1, dp[i][j])
        return dp[m][n]


if __name__ == '__main__':
    arrs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(Solution().findMaxForm(arrs, m, n))

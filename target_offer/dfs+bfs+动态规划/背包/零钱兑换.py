#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 零钱兑换.py
# @Author: smx
# @Date  : 2020/2/21
# @Desc  :

class Solution:
    def coinChange(self, arrs, target):
        if target <= 0 or not arrs: return 0
        if target in arrs: return 1
        dp = [0] + [0xffffff for _ in range(target)]
        n = len(arrs)
        for i in range(n):
            for j in range(arrs[i], target + 1):
                dp[j] = min(dp[j], dp[j - arrs[i]] + 1)
        return dp[target] if dp[target] != 0xffffff else -1


if __name__ == '__main__':
    coins = [1, 2, 3, 4, 5, 6, 7]
    amount = 11
    print(Solution().coinChange(coins, amount))

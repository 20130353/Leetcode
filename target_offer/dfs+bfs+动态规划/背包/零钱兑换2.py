#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 零钱兑换.py
# @Author: smx
# @Date  : 2020/2/21
# @Desc  :

# 计算可以得到的组合数量
# 从coin可以改变的地方写起，减少迭代次数
class Solution:
    def change(self, target, arrs):
        dp = [1] + [0 for _ in range(target)]
        n = len(arrs)
        for i in range(n):
            for j in range(arrs[i], target + 1):
                dp[j] += dp[j - arrs[i]]
        return dp[target]


if __name__ == '__main__':
    amount = 0
    coins = []
    print(Solution().change(amount, coins))

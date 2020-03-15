#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 目标和.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :


# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
# 对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
# 本质是01背包问题，拿不拿对应+-号，target对重量，结果求方案数

# 因为只用到dp[i]和dp[i-1],所以迭代循环！
class Solution:
    def findTargetSumWays(self, arrs, target):
        n = len(arrs)
        dp = [0 for _ in range(2001)]
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1, n):
            next = [0 for _ in range(2001)]
            for j in range(-1000, 1001):
                if dp[j + 1000] > 0:
                    next[j + arrs[i] + 1000] += dp[j + 1000]
                    next[j - arrs[i] + 1000] += dp[j + 1000]
            dp = next
        return 0 if target > 1000 else dp[target + 1000]


if __name__ == '__main__':
    nums = [1000]
    S = 1000
    print(Solution().findTargetSumWays(nums, S))

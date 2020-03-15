#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最长上升子序列.py
# @Author: smx
# @Date  : 2020/2/23
# @Desc  :

# [10, 9, 2, 5, 3, 7, 21, 18]
# 对应的是[2,3,7,18]
class Solution:
    # def lengthOfLIS(self, arrs):
    #     if not arrs: return 0
    #     n = len(arrs)
    #     dp = [1 for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i):
    #             if dp[j] >= dp[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)

    def binary_search(self, arrs, target):
        # 找到比它大的最小元素
        # 找不到就返回-1
        left, right = 0, len(arrs) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arrs[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def lengthOfLIS(self, arrs):
        if not arrs: return 0
        n = len(arrs)
        dp = [arrs[0]]
        for i in range(1, n):
            pos = self.binary_search(dp, arrs[i])
            if dp[pos] > arrs[i]:
                dp[pos] = arrs[i]
            elif dp[pos] < arrs[i]:
                dp.append(arrs[i])
        return len(dp)


if __name__ == '__main__':
    arrs = [2, 2]
    print(Solution().lengthOfLIS(arrs))

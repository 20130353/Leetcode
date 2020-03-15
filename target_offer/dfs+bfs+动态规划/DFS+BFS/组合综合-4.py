#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 组合综合-3.py
# @Author: smx
# @Date  : 2020/2/20
# @Desc  :

# 数字可以重复使用
# 超时！应该用动态规划！
class Solution:
    def DFS(self, arrs, n, target, cur_sum, ans):
        if cur_sum == target:
            ans[0] += 1
            return

        if cur_sum > target:
            return

        for i in range(n):
            if arrs[i] + cur_sum <= target:
                self.DFS(arrs, n, target, cur_sum + arrs[i], ans)

    def combinationSum4(self, nums, target) -> int:
        n = len(nums)
        ans = [0]
        self.DFS(nums, n, target, 0, ans)
        return ans[0]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums, target))

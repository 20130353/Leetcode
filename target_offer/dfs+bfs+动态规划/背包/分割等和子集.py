#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 分割等和子集.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 分割成两个集合
# 1. DFS暴力搜索-target的结合
# 2. 01背包问题
# DFS
# class Solution:
#     def DFS(self, arrs, n, target, pos, cur_sum, flag):
#         if flag[0] or cur_sum > target:
#             return
#         if pos == n or cur_sum == target:
#             flag[0] = cur_sum == target
#             return
#
#         if sum((arrs[pos:])) + cur_sum < target:
#             return
#
#         self.DFS(arrs, n, target, pos + 1, cur_sum + arrs[pos], flag)
#         self.DFS(arrs, n, target, pos + 1, cur_sum, flag)
#
#     def canPartition(self, arrs):
#         if not arrs or arrs.__len__() <= 1 or sum(arrs) % 2 != 0:
#             return False
#         target = sum(arrs) / 2
#         arrs = sorted(arrs)
#         new_arrs = []
#         for i in range(len(arrs) - 1, -1, -1):
#             if arrs[i] > target:
#                 return False
#             if arrs[i] != target and arrs[i] != 0:
#                 new_arrs.append(arrs[i])
#             if arrs[i] == target:
#                 return True
#         flag = [False]
#         self.DFS(new_arrs, len(new_arrs), target, 0, 0, flag)
#         return flag[0]


class Solution:
    # 搞清楚状态！
    def canPartition(self, arrs):
        if not arrs: return True
        if sum(arrs) % 2 != 0: return False
        target = sum(arrs) // 2
        n = len(arrs)
        # dp[i][j]表示到第i个物品的j值是否能平均分割成两个集合
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, len(arrs) + 1):
            for j in range(target + 1):
                if j >= arrs[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arrs[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]


if __name__ == '__main__':
    arrs = [3, 3, 4, 5]
    print(Solution().canPartition(arrs))

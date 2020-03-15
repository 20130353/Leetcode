#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 化为k个相等的子集.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 思考一个问题：什么时候使用暴力穷举？
# 思考一个问题：什么时候使用暴力穷举？
# 思考一个问题：什么时候使用暴力穷举？
# 思考一个问题：什么时候使用暴力穷举？
# 思考一个问题：什么时候使用暴力穷举？
# 形成组合，且组合内元素无顺序！
# class Solution:
#     # 只能过143/149 case
#     def canPartitionKSubsets(self, arrs, k):
#         if not arrs or k > len(arrs) or sum(arrs) % k != 0:
#             return False
#         target = sum(arrs) / k
#         arrs = sorted(arrs)
#         ans = [0 for _ in range(k)]
#         for i in range(len(arrs) - 1, -1, -1):
#             if arrs[i] > target:
#                 return False
#             min_i = ans.index(min(ans))
#             if ans[min_i] + arrs[i] > target:
#                 return False
#         return True

class Solution:
    def DFS(self, arrs, n, target, k, ans, pos, flag):
        if flag[0]:
            return
        if pos == n:
            for each in ans:
                if each != target:
                    return
            flag[0] = True
            return

        if sum((arrs[pos:])) > (target - min(ans)) * k:
            return

        for j in range(k):
            if ans[j] + arrs[pos] <= target:
                ans[j] += arrs[pos]
                self.DFS(arrs, n, target, k, ans, pos + 1, flag)
                ans[j] -= arrs[pos]

    def canPartitionKSubsets(self, arrs, k):
        if not arrs or k > len(arrs) or sum(arrs) % k != 0:
            return False
        target = sum(arrs) / k
        arrs = sorted(arrs)
        new_arrs = []
        for i in range(len(arrs) - 1, -1, -1):
            if arrs[i] > target:
                return False
            # 这个没想到！个没想到！个没想到！个没想到！个没想到！
            if arrs[i] != target and arrs[i] != 0:
                new_arrs.append(arrs[i])
            if arrs[i] == target:
                k -= 1
        ans = [0 for _ in range(k)]
        flag = [False]
        self.DFS(new_arrs, len(new_arrs), target, k, ans, 0, flag)
        return flag[0]


if __name__ == '__main__':
    arrs = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(Solution().canPartitionKSubsets(arrs, k))

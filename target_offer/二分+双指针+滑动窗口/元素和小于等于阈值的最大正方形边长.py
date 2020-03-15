#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 元素和小于等于阈值的最大正方形边长.py
# @Author: smx
# @Date  : 2020/2/17
# @Desc  :

# 因为是正整数，所以当小正方形不满足条件时，大正方形也不满足
# 找的是最大的边长，所以可以用边长来优化
class Solution:
    def maxSideLength(self, mat, th):
        if not mat or th <= 0:
            return 0

        m, n = len(mat), len(mat[0])
        sum_m = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_m[i][j] = sum_m[i][j - 1] + sum_m[i - 1][j] - sum_m[i - 1][j - 1] + mat[i - 1][j - 1]

        max_k = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(max(1, max_k), min(i, j) + 1):
                    s = sum_m[i][j] - sum_m[i - k][j] - sum_m[i][j - k] + sum_m[i - k][j - k]
                    if s <= th:
                        max_k = max(max_k, k)
                    else:
                        break
        return max_k


if __name__ == '__main__':
    mat = [[18, 70],
           [61, 1],
           [25, 85],
           [14, 40],
           [11, 96],
           [97, 96],
           [63, 45]]
    threshold = 40184
    print(Solution().maxSideLength(mat, threshold))

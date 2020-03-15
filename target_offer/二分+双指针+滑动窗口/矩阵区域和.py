#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 矩阵区域和.py
# @Author: smx
# @Date  : 2020/2/17
# @Desc  :


# 矩阵区域和，按照区域对矩阵求和，求区域时，直接在ij基础上加减k
# 官方的前缀和是周围上了一圈0
class Solution:
    def matrixBlockSum(self, mat, K):
        m, n = len(mat), len(mat[0])
        sum_m = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_m[i][j] = sum_m[i - 1][j] + sum_m[i][j - 1] - sum_m[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return sum_m[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) \
                            - get(i + K + 1, j - K) + get(i - K, j - K)
        return ans

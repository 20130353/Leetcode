#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 和为目标值的子矩阵的数量.py
# @Author: smx
# @Date  : 2020/2/17
# @Desc  :

# 这样不会出现重复！
# 超时！
# 计算前缀和的过程和判断过程融合在一起！
class Solution:
    def numSubmatrixSumTarget(self, mat, target):
        if not mat:
            return 0

        m, n = len(mat), len(mat[0])
        sum_m = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_m[i][j] = sum_m[i][j - 1] + sum_m[i - 1][j] - sum_m[i - 1][j - 1] + mat[i - 1][j - 1]
                for width in range(1, j + 1):
                    for height in range(1, i + 1):
                        s = sum_m[i][j] - sum_m[i - height][j] - sum_m[i][j - width] + sum_m[i - height][j - width]
                        if s == target:
                            ans += 1
        return ans


if __name__ == '__main__':
    matrix = [[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]]
    target = 0
    print(Solution().numSubmatrixSumTarget(matrix, target))

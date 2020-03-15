#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 前缀和.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :

# 最大正方形
class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        # 计算矩阵前缀和
        sum_m = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_m[i][j] = sum_m[i][j - 1] + sum_m[i - 1][j] - sum_m[i - 1][j - 1] + int(matrix[i - 1][j - 1])

        max_area = 0 if 1 not in sum_m else 1
        # 计算最大正方形面积
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, min(i, j) + 1):
                    area = sum_m[i][j] - sum_m[i - k][j] - sum_m[i][j - k] + sum_m[i - k][j - k]
                    if area == k * k:
                        max_area = max(area, max_area)
                    else:
                        break
        return max_area


if __name__ == '__main__':
    matrix = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    print(Solution().maximalSquare(matrix))

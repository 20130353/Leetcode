#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 前缀和.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :

# 最大正方形
# numpy和list的区别：
# 1. list遍历只能使用遍历和c++数组的方式；numpy可以使用索引，tuple索引,eg:a[1,1]，a[1,:],我觉得python的numpy更像matlab语言的使用习惯
# 2. list存放元素内容可以不相同，numpy存放内容一定要相同
# 心得：计算正方形或者是任何形状或者数组的是否合适，都是这一段减去形状！

import numpy as np
class Solution:
    # 这里确定matrix的形式，是一维数组还是二维数组？还是两者都可以？
    def maximalSquare(self, matrix):

        if not matrix:
            return 0

        # 判断数组维度
        matrix = np.array(matrix)

        # 一维数组
        if np.ndim(matrix)==1:
            return int(max(matrix))

        # 二维数组
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

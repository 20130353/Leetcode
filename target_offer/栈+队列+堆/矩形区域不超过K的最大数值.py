#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 矩形区域不超过K的最大数值.py
# @Author: smx
# @Date  : 2020/2/15
# @Desc  :

import numpy as np


class Solution:

    def get_single_matrix(self, matrix):
        max_sum = -0xfffffff
        num = 0
        arr = []
        # 找小于的最大值
        for i in range(len(matrix)):
            num += matrix[i]
            if num <= k and num > max_sum:
                max_sum = num
            target = num - k  # 找大于的最小值
            sorted_num = sorted(arr)
            left, right = 0, len(sorted_num) - 1
            while left < right:
                mid = left + (right - left) // 2
                if sorted_num[mid] < target:
                    left = mid + 1
                else:
                    if num - sorted_num[mid] <= k and num - sorted_num[mid] > max_sum:
                        max_sum = num - sorted_num[mid]
                    right = mid
            arr.append(num)
        return max_sum

    def maxSumSubmatrix(self, matrix, k):
        if not matrix and k < 0:
            return 0
        matrix = np.matrix(matrix)
        rows, cols = matrix.shape
        if cols == 1:
            matrix = [matrix[i, 0] for i in range(rows)]
            max_sum = self.get_single_matrix(matrix)
            return max_sum if max_sum != -0xfffffff else -1
        elif rows == 1:
            matrix = [matrix[0, i] for i in range(cols)]
            max_sum = self.get_single_matrix(matrix)
            return max_sum if max_sum != -0xfffffff else -1
        else:
            max_sum = -0xfffffff
            # 只固定了下边界，没有上边界，所以是错误的
            # 所以人家的想法是固定两条边界，然后
            for top in range(rows):
                for down in range(top + 1, rows):
                    new_matrix = [np.sum(matrix[top:down + 1, i]) for i in range(cols)]
                    max_sum = max(self.get_single_matrix(new_matrix), max_sum)
            return max_sum if max_sum != -0xfffffff else -1


if __name__ == '__main__':
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    print(Solution().maxSumSubmatrix(matrix, k))

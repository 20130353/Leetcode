#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 阿里面试题.py
# @Author: smx
# @Date  : 2020/2/25
# @Desc  :

#
# // 评测题目: 统计标准数独问题的所有解的数量并输出（9
# X9棋盘大小）
# // 1）合理时间内给出计数结果
# // 2）尽可能优化时间效率
# // 3）提示，朴素枚举空间过大，可尝试解决小规模问题，如4x4棋盘大小，寻找优化线索

import numpy as np


class Solution():
    def DFS(self, mat, n, x, y, cur, count, row_set, col_set, mat_set, ans):
        if cur == count:
            ans[0] += 1
            return
        for num in range(10):
            if num not in row_set[x] and num not in col_set[y] and num not in mat_set[int(x / 3)][int(y / 3)]:
                for i in range(9):
                    for j in range(9):
                        if mat[i, j] == 0:
                            mat[x][y] = num
                            row_set[x].add(i)
                            col_set[y].add(j)
                            mat_set[int(x / 3)][int(y / 3)].add(i)
                            self.DFS(mat, n, i, j, cur + 1, count, row_set, col_set, mat_set, ans)
                            row_set[x].remove(i)
                            col_set[y].remove(j)
                            mat_set[int(x / 3)][int(y / 3)].remove(i)
                            mat[x][y] = 0
        return

    # 如果有解返回mat，如果无解，返回-1
    def get_num(self, mat):
        if not mat or (len(mat) != len(mat[0])): return -1
        n = len(mat)
        mat = np.matrix(mat)
        count = n * n - np.count_nonzero(mat)  # 需要填写的数字个数
        row_set = []  # 行出现的数字set
        col_set = []  # 列出现的数字set
        for i in range(n):
            row_set.append(set(mat[i, :].reshape(1, -1).tolist()[0]))
            col_set.append(set(np.reshape(mat[:, i], (1, -1)).tolist()[0]))
        ans = [-1]
        # 记录小的3 * 3 块是否出现这个数字
        mat_set = []
        for i in range(3):
            for j in range(3):
                mset = set(mat[(i * 3):(i + 1) * 3, j * 3:(j + 1) * 3].reshape([1, -1]).tolist()[0])
                mat_set.append(mset)
        for i in range(n):
            for j in range(n):
                if mat[i, j] == 0:
                    self.DFS(mat, n, i, j, 0, count, row_set, col_set, mat_set, ans)
        return ans[0]


if __name__ == '__main__':
    mat = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 0, 3, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 0, 6, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print(Solution().get_num(mat))

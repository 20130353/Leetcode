#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : shopee的位置--棋盘.py
# @Author: smx
# @Date  : 2019/8/17
# @Desc  :

# 超时
# def solution(mat, n, m, i, j):
#     if i == n and j == m:
#         global count
#         count += 1
#         return
#
#     if i + 1 <= n and mat[i + 1][j] != 1:
#         solution(mat, n, m, i + 1, j)
#
#     if j + 1 <= m and mat[i][j + 1] != 1:
#         solution(mat, n, m, i, j + 1)

# 这道题的收获是：递归函数改成dp动态规划就可以了
def solution(mat, n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if (i == 0 and j == 1) or (i == 1 and j == 0):
                dp[i][j] = 1
                continue
            if i - 1 >= 0 and mat[i - 1][j] != 1:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0 and mat[i][j - 1] != 1:
                dp[i][j] += dp[i][j - 1]
    return dp[n][m]


if __name__ == '__main__':
    n, m, k = map(int, input().strip().split(' '))
    mat = [[0] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().strip().split(' '))
        mat[x][y] = 1

    ans = solution(mat, n, m)
    print(ans)

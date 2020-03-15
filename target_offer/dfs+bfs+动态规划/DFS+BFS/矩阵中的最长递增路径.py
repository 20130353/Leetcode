#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 矩阵中的最长递增路径.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :

# 最普通的方法：深度搜索，超时！
# 超时-> 保存中间变量!!!!!!!!
# 超时-> 保存中间变量!!!!!!!!
# 超时-> 保存中间变量!!!!!!!!
# 超时-> 保存中间变量!!!!!!!!
# 超时-> 保存中间变量!!!!!!!!
# 超时-> 保存中间变量!!!!!!!!
class Solution:
    def DFS(self, x, y, mat, m, n, cache):
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # 说明已经有记录了！
        if cache[x][y] != 0:
            return cache[x][y]
        max_len = 1
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            # 在各种道路中选择最长的一条
            if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] > mat[x][y]:
                length = self.DFS(nx, ny, mat, m, n, cache)
                max_len = max(max_len, length + 1)
        cache[x][y] = max_len
        return max_len

    def longestIncreasingPath(self, mat):
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.DFS(i, j, mat, m, n, cache))
        return ans


if __name__ == '__main__':
    nums = [[9]]
    print(Solution().longestIncreasingPath(nums))

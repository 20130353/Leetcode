#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 被包围的区域.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :


class Solution:

    def DFS(self, x, y, mat, m, n, vis, points, flag):
        # 这里不能剪枝，如果提前剪枝了，那么因为有些节点没有被收入，导致会在开始被检测到，进入DFSn多次！
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < m and 0 <= ny < n and vis[nx][ny] == 0 and mat[nx][ny] == 'O':
                points.append((nx, ny))
                if (nx == 0 or ny == 0 or nx == m - 1 or ny == n - 1):
                    flag[0] = True
                vis[nx][ny] = 1
                self.DFS(nx, ny, mat, m, n, vis, points, flag)
        return

    def solve(self, mat):
        if not mat:
            return
        m, n = len(mat), len(mat[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if vis[i][j] == 0 and mat[i][j] == 'O':
                    points = [(i, j)]
                    flag = [True] if (i == 0 or j == 0 or i == m - 1 or j == n - 1) else [False]
                    vis[i][j] = 1
                    self.DFS(i, j, mat, m, n, vis, points, flag)
                    if not flag[0]:
                        for each in points:
                            mat[each[0]][each[1]] = 'X'
        return


if __name__ == '__main__':
    mat = [["O", "O", "O", "O", "X", "X"],
           ["O", "O", "O", "O", "O", "O"],
           ["O", "X", "O", "X", "O", "O"],
           ["O", "X", "O", "O", "X", "O"],
           ["O", "X", "O", "X", "O", "O"],
           ["O", "X", "O", "O", "O", "O"]]

    Solution().solve(mat)
    for each in mat:
        print(each)

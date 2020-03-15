#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 岛屿数量.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :

class Solution:
    def DFS(self, x, y, mat, m, n):
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == '1':
                mat[nx][ny] = '0'
                self.DFS(nx, ny, mat, m, n)

    def BFS(self, x, y, mat, m, n):
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = [(x, y)]
        while queue:
            top = queue.pop()
            for i in range(4):
                nx = top[0] + dir[i][0]
                ny = top[1] + dir[i][1]
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == '1':
                    mat[nx][ny] = '0'
                    queue.append((nx, ny))

    def numIslands(self, mat):
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == '1':
                    mat[i][j] = '0'
                    ans += 1
                    self.BFS(i, j, mat, m, n)
                    # self.DFS(i, j, mat, m, n)
        return ans


if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 1, 1]]
    print(Solution().numIslands(mat))

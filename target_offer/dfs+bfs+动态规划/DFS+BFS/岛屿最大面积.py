# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/26/18
# file: 岛屿最大面积.py
# description:

# 重点是vis！
class Solution:
    def DFS(self, x, y, mat, m, n, cur_area, max_area):
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if cur_area[0] > max_area[0]: max_area[0] = cur_area[0]
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1:
                mat[nx][ny] = 0
                cur_area[0] += 1
                self.DFS(nx, ny, mat, m, n, cur_area, max_area)

    def BFS(self, x, y, mat, m, n, cur_area, max_area):
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = [(x, y)]
        while queue:
            top = queue.pop()
            for i in range(4):
                nx = top[0] + dir[i][0]
                ny = top[1] + dir[i][1]
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1:
                    cur_area[0] += 1
                    mat[nx][ny] = 0
                    queue.append((nx, ny))
        if cur_area[0] > max_area[0]: max_area[0] = cur_area[0]

    def maxAreaOfIsland(self, mat):
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        max_area = [0]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = 0
                    self.BFS(i, j, mat, m, n, [1], max_area)
                    # self.DFS(i, j, mat, m, n, [1], max_area)
        return max_area[0]


if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 1, 1]]
    print(Solution().maxAreaOfIsland(mat))

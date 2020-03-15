#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 朋友圈.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :


# 用深度优先遍历，遍历到这个人的时候顺着这个人到下一个人！
# 用队列的BFS只能减少内存调用，但是无法减少时间消耗！
class Solution:
    def DFS(self, M, m, n, y):
        for j in range(n):
            if M[y][j] == 1:
                M[y][j] = 0
                self.DFS(M, m, n, j)
        return

    def BFS(self, M, m, n, i):
        queue = []
        for j in range(n):
            if M[i][j] == 1:
                queue.append(j)
                M[i][j] = 0
        while queue:
            top = queue.pop(0)
            for j in range(n):
                if M[top][j] == 1:
                    queue.append(j)
                    M[top][j] = 0

    def findCircleNum(self, M):
        ans = 0
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    # self.DFS(M, m, n, j)
                    self.BFS(M, m, n, j)
                    M[i][j] = 0
                    ans += 1
        return ans


if __name__ == '__main__':
    mat = [[1, 1, 1],
           [1, 1, 0],
           [1, 0, 1]]
    print(Solution().findCircleNum(mat))

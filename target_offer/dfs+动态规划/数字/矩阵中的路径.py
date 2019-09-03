# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 矩阵中的路径.py
# description:

'''
    给定一个字符矩阵,,判断是否存在一条包含字符串所有字符发路径
'''


'''
    反思：
    1. 他给定义的matrix是字符串，必须要使用i*cols+j的方式才能遍历
    2. vis的True和False写成一样的，这个本该是在代码检查阶段就检查出来的，但是没有！！！下次谨记！

'''

class Solution:

    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def DFS(self, ans, map_, vis, i, j, m, n, index, path):

        if ans[0]:
            return

        if index >= len(path):
            ans[0] = True
            return

        for k in range(4):
            ni = i + self.dir[k][0]
            nj = j + self.dir[k][1]
            if ni >= 0 and nj >= 0 and ni < m and nj < n and not vis[ni][nj] and map_[ni * n + nj] == path[index]:
                vis[ni][nj] = True
                self.DFS(ans, map_, vis, ni, nj, m, n, index + 1, path)
                vis[ni][nj] = False

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        vis = [[False for _ in range(cols)] for _ in range(rows)]
        ans = [False]
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0] and not vis[i][j]:
                    vis[i][j] = True
                    self.DFS(ans, matrix, vis, i, j, rows, cols, 1, path)
                    vis[i][j] = False
        return ans[0]


if __name__ == '__main__':

    # print(Solution().hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))
    print(Solution().hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SGGFIECVAASABCEHJIGQEM"))

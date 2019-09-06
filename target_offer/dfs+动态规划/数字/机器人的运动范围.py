# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 机器人的运动范围.py
# description:

'''
    给定一个棋盘,要求机器人只能走上下左右的方向,不能进入到坐标之和等与s的方格,求机器人能进入多少方格?
'''

'''
    反思：
        1. 自定义的变量需要在init初始化函数中声明
        2. 函数传递参数记得数好，代码检查要检查好！
        3. 边界，看清是从1开始还是从0开始的！

'''
class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def get_sum(self, a, b):
        if a < 10:
            sum_a = a
        else:
            sum_a = sum(list(map(int, str(a))))
        if b < 10:
            sum_b = b
        else:
            sum_b = sum(list(map(int, str(b))))
        return sum_a + sum_b

    def DFS(self, th, sum_, i, j, m, n, vis):
        for k in range(4):
            ni = i + self.dir[k][0]
            nj = j + self.dir[k][1]
            if ni >= 0 and nj >= 0 and ni < m and nj < n and not vis[ni][nj] and self.get_sum(ni, nj) <= th:
                vis[ni][nj] = True
                sum_[0] = sum_[0] + 1
                self.DFS(th, sum_, ni, nj, m, n, vis)

    def movingCount(self, threshold, rows, cols):
        vis = [[False for _ in range(cols)] for _ in range(rows)]
        sum_ = [0]
        if threshold > 0:
            sum_[0] = 1
            vis[0][0] = True
            self.DFS(threshold, sum_, 0, 0, rows, cols, vis)

        return sum_[0]


if __name__ == '__main__':
    so = Solution()
    print(so.movingCount(15, 20, 20))

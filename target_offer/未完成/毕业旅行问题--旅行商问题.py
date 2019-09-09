#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 毕业旅行问题--旅行商问题.py
# @Author: smx
# @Date  : 2019/8/19
# @Desc  :

# 存在的问题：想到的是最小生成树算法 -》 动态规划
# 收获：用状态表示点集合！

class Solution:
    def tsp(self, matrix):
        m, n = len(matrix) * len(matrix), len(matrix)
        # 状态压缩DP,5表示0101,dp[i][j]表示从0出发,经过i中的点到达j,要求i中有j
        # i表示一个状态集合
        dp = [[float('inf')] * n for _ in range(m)]
        dp[1][0] = 0
        # 这个要两层循环，从i-j包括任意两点之间的循环
        for i in range(1, m):
            if not (i & 1):  # i中不能包括0,不能从0出发
                continue
            for j in range(1, n):  # 判断这些点是否存在状态中
                if i & (1 << j):  # 如果i中包括j就重复了
                    continue
                for k in range(n):  # 找已经在集合中点，判断i通过集合中的点到j的之间的距离
                    if i & (1 << k):  # 如果i中包括k，i中加上j,0到j的最短距离可能为原来i中任何一个k到j的距离与剩余最短距离之和
                        dp[(1 << j) | i][j] = min(dp[(1 << j) | i][j], dp[i][k] + matrix[k][j])
        res = float('inf')
        # 最后还要回到0
        for i in range(n):
            # 怎么保证所有点都经历过一遍了呢？--》m-1中的点是一个一个点加起来算的，所以一定会经过所有点！
            res = min(res, dp[m - 1][i] + matrix[i][0])
        return res


if __name__ == '__main__':
    n = int(input().strip())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().strip().split(' '))))
    print(Solution().tsp(mat))

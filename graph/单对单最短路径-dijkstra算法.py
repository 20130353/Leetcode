# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/18/18
# file: 单对单最短路径-dijkstra算法.py
# description:
# 每次找到距离起点最近的且没有被访问的点
# 利用新被访问的点更新最短路径
# 最终找到和每个点距离起点最近的点
# 这是起点对多个点的最短路径，
# 如果是两个之间的最短路径可以直接用DP，时间复杂度n3
# 如果是递归，时间复杂度阶乘！
# 所以时间最优的是迪杰斯克拉算法，时间复杂度是n2

import math
import copy as cp

if __name__ == '__main__':

    n, m = input().split()
    n, m = int(n), int(m)
    v = [0]
    vis = [0 for _ in range(n)]
    map = [[math.inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                map[i][j] = 0

    for _ in range(m):
        x = input()
        a, b, w = x.split(' ')
        map[int(a)][int(b)] = int(w)
        map[int(b)][int(a)] = int(w)

    dis = cp.deepcopy(map[0])
    vis[0] = 1  # v0是起点
    for i in range(1, n):
        # 找到一个最近的顶点
        next_v = -1
        min_dis = math.inf
        for k in range(1, n):
            if vis[k] == 0 and dis[k] < min_dis:
                next_v = k
                min_dis = dis[k]
        if next_v == -1:
            break
        else:
            v.append(next_v)
            vis[next_v] = 1
            for k in range(n):
                if vis[k] == 0 and dis[k] > min_dis + map[next_v][k]:
                    dis[k] = min_dis + map[next_v][k]
    print(' '.format(map(str, v)))


'''
9 16
0 1 1
0 2 5
1 2 3
1 3 7
1 4 5
2 4 1
2 5 7
3 4 2
3 6 3
4 5 3
4 6 6
4 7 9
5 7 5
6 7 2
6 8 7
7 8 4
'''

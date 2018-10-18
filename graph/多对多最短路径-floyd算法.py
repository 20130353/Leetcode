# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/18/18
# file: 多对多最短路径-floyd算法.py
# description: 个人觉得将dijstra算法改成多起点遍历输出的时间效率和Floyd的时间效率是一样的
# 这里是将中间节点遍历了一遍

import math
import copy as cp

if __name__ == '__main__':

    n, m = input().split()
    n, m = int(n), int(m)

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

    dis = [[math.inf for _ in range(n)] for _ in range(n)]
    p = cp.deepcopy(dis)

    for v in range(n):
        for w in range(n):
            dis[v][w] = map[v][w]
            p[v][w] = w

    for k in range(n):
        for v in range(n): # v 是起点
            for w in range(n): # w 是终点
                if dis[v][w] > dis[v][k] + dis[k][w]:
                    dis[v][w] = dis[v][k] + dis[k][w]
                    p[v][w] = p[v][k]

    print(p)
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

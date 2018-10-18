# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/18/18
# file: 单对单最短路径-dijkstra算法.py
# description: 一步一步更新经多经过当前点的最短路径

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

    dis = cp.deepcopy(map[0])
    vis[0] = 1 # v0 是起点,算作是已经被访问过了
    print(0,end = '\t')
    for i in range(1,n):
        # 找到一个ie最近的顶点
        min_j = -1
        min_dis = math.inf
        for k in range(1,n):
            if vis[k] == 0 and dis[k] < min_dis:
                min_j = k
                min_dis = dis[k]
        if min_j == -1:
            break
        else:
            vis[min_j] = 1
            print(min_j,end = '\t')
            for k in range(n):
                if vis[k] == 0 and dis[k] > min_dis + map[min_j][k]:
                    dis[k] = min_dis + map[min_j][k]
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

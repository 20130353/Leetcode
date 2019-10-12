# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/17/18
# file: 最小生成树-prim算法.py
# description:
# 每次找到权重最小的边加入树
import numpy as np
import math
import copy as cp

if __name__ == '__main__':

    n, m = input().split()
    n, m = int(n), int(m)

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

    min_dis = cp.deepcopy(map[0])
    for i in range(n):
        min_v = math.inf
        next_v = -1
        for j in range(n):
            if min_dis[j] != 0 and min_dis[j] < min_v:
                next_v = j
                min_v = min_dis[j]
        if next_v == -1: # 所有点的都被遍历了
            break
        else:
            min_dis[next_v] = 0
            for k in range(n):
                if map[next_v][k] < min_dis[k]:
                    min_dis[k] = map[next_v][k]

'''
9 15
0 1 10
0 5 11
1 2 18
1 6 16
1 8 12
2 3 22
2 8 8
3 4 20
3 6 24
3 7 16
3 8 21
4 5 26
4 7 7
5 6 17
6 7 19
'''
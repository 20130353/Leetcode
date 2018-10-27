# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/27/18
# file: 01_matrix.py
# description:
'''
     出现的问题是:
     1. 深度太大,导致死机.
     原因:vis可以没有设置,导致是不断重复访问

     2. min_dis 不知道要怎么返回
     原因: 直接用结束条件卡路径长度,在和min路径长度比较.只有当满足结束路径的时候才能结束,要不然必须要要暴力穷举下去.
'''

'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1


'''

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def DFS(i,j,map,vis,dis,min_dis):

    # print(type(map[i][j]))
    print('i,j,map,dis,min_dis',i,j,map[i][j],dis,min_dis[0])

    if dis > min_dis[0]:
        return

    if map[i][j] == 0:
        if min_dis[0] > dis:
            min_dis[0] = dis
        return

    for k in range(4):
        ni = i + dir[k][0]
        nj = j + dir[k][1]
        if ni >= 0 and ni < len(map) and nj >= 0 and nj < len(map[0])\
            and vis[ni][nj] == False:
            vis[ni][nj] = True
            DFS(ni,nj,map,vis,dis+1,min_dis)
            vis[i][j] = False

import math
if __name__ == '__main__':
    n,m = list(map(int, input().strip().split(' ')))
    dict = []
    for inx in range(n):
        str = list(map(int, input().strip().split(' ')))
        dict.append(str)

    ans = [[math.inf for _ in range(m)] for _ in range(n)]
    vis = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            min_dis = [math.inf]
            vis[i][j] = True
            DFS(i, j, dict, vis, 0, min_dis)
            ans[i][j] = min_dis[0]
            vis[i][j] = False

    for i in range(n):
        for j in range(m):
            print(ans[i][j],end='\t')
        print()

'''
3 3
0 0 0
0 1 0
0 0 0


'''
# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/27/18
# file: 01_matrix_基础模板.py
# description:
'''
     出现的问题是:
     1. 深度太大,导致死机.
     原因:vis可以没有设置,导致是不断重复访问

     2. min_dis 不知道要怎么返回
     原因: 直接用结束条件卡路径长度,在和min路径长度比较.只有当满足结束路径的时候才能结束,要不然必须要要暴力穷举下去.


     3. 有个更优秀的算法可以参考
     https://www.cnblogs.com/grandyang/p/6602288.html
'''

'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:
3 3 
0 0 0
0 1 0
0 0 0
输出:
0 0 0
0 1 0
0 0 0

示例 2:
输入:
3 3
0 0 0
0 1 0
1 1 1
输出:
0 0 0
0 1 0
1 2 1

解题：如果当前元素是0的话，最近距离是1，如果当前元素不是0的话，找到距离最近的0元素。
用BFS比DFS更容易搜到最优结果！
'''

import math

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# def DFS+BFS(i, j, map, vis, dis, min_dis):
#     print('i,j,map,dis,min_dis', i, j, map[i][j], dis, min_dis[0])
#     if dis > min_dis[0]:
#         return
#
#     if map[i][j] == 0:
#         if min_dis[0] > dis:
#             min_dis[0] = dis
#         return
#
#     for k in range(4):
#         ni = i + dir[k][0]
#         nj = j + dir[k][1]
#         if ni >= 0 and ni < len(map) and nj >= 0 and nj < len(map[0]) \
#                 and vis[ni][nj] is False:
#             vis[ni][nj] = True
#             DFS+BFS(ni, nj, map, vis, dis + 1, min_dis)
#             vis[i][j] = False


def BFS(si, sj, map, vis, dis, min_dis):
    queue = [(si, sj, 0)]

    while queue.__len__() != 0:
        i, j, num = queue.pop()
        if map[i][j] == 0:
            if num < min_dis[0]:
                min_dis[0] = num
        if num > min_dis[0]:
            break

        for k in range(4):
            ni = i + dir[k][0]
            nj = j + dir[k][1]
            if ni >= 0 and ni < len(map) and nj >= 0 and nj < len(map[0]) and vis[ni][nj] is False:
                vis[ni][nj] = True
                queue.append((ni, nj, num + 1))


if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    arr = []
    for inx in range(n):
        str = list(map(int, input().strip().split(' ')))
        arr.append(str)

    ans = [[math.inf for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            min_dis = [math.inf]
            vis = [[False for _ in range(m)] for _ in range(n)]
            vis[i][j] = True
            # DFS+BFS(i, j, map, vis, 0, min_dis)
            BFS(i, j, arr, vis, 0, min_dis)
            ans[i][j] = min_dis[0]
            vis[i][j] = False

    for i in range(n):
        for j in range(m):
            print(ans[i][j], end='\t')
        print()

'''
3 3
0 0 0
0 1 0
0 0 0
'''

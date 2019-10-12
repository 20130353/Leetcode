# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/26/18
# file: island_size_基础模板.py
# description:

'''
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

    出现的问题是:
    1. vis标记什么时候需要恢复，什么时候不需要恢复。搜索最长路径的时候不需要，搜可行路径的时候需要。差别是最长路径一定会加上当前节点，所以一个节点只要走一遍就够了。但是找可行路径的时候需要都走！
    还有一个调试bug的好方法是: 打印i,j值,同时在ipad上对照原始的数组形式
    2. 用BFS比DFS时间更短，消耗资源更少！
'''
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def DFS(i, j, map, vis, cur, max):
    print('i,j,sum:', i, j, cur)
    if cur[0] > max[0]:
        max[0] = cur[0]

    for inx in range(4):
        ni = i + dir[inx][0]
        nj = j + dir[inx][1]
        if ni >= 0 and ni < len(map) and nj >= 0 and nj < len(map[0]) and map[ni][nj] == '1' and vis[ni][nj] is False:
            vis[ni][nj] = True
            cur[0] += 1
            DFS(ni, nj, map, vis, cur, max)


def BFS(si, sj, map, vis, cur, max):
    queue = [(si, sj)]
    while queue.__len__() != 0:
        i, j = queue[0][0], queue[0][1]
        queue.pop(0)
        for inx in range(4):
            ni = i + dir[inx][0]
            nj = j + dir[inx][1]
            if ni >= 0 and ni < len(map) and nj >= 0 and nj < len(map[0]) and map[ni][nj] == '1' \
                    and vis[ni][nj] is False:
                vis[ni][nj] = True
                cur[0] += 1
                queue.append((ni, nj))
    if cur[0] > max[0]:
        max[0] = cur[0]


if __name__ == '__main__':
    n = int(input().strip())
    map = []
    vis = []
    for _ in range(n):
        a = list(input().strip().replace(',', ''))
        map.append(a)
        vis.append([False for _ in a])

    max = [0]
    for i in range(n):
        for j in range(map[i].__len__()):
            if map[i][j] == '1' and vis[i][j] is False:
                vis[i][j] = True
                # DFS+BFS(i, j, map, vis, [1], max)
                BFS(i, j, map, vis, [1], max)
    print(max[0])

'''
示例1：
8 
0,0,1,0,0,0,0,1,0,0,0,0,0
0,0,0,0,0,0,0,1,1,1,0,0,0
0,1,1,0,1,0,0,0,0,0,0,0,0
0,1,0,0,1,1,0,0,1,0,1,0,0
0,1,0,0,1,1,0,0,1,1,1,0,0
0,0,0,0,0,0,0,0,0,0,1,0,0
0,0,0,0,0,0,0,1,1,1,0,0,0
0,0,0,0,0,0,0,1,1,0,0,0,0

====================
6

示例 2:
1
0,0,0,0,0,0,0,0

===============
0

'''

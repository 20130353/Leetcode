# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 矩阵中的路径.py
# description:

'''
    给定一个字符矩阵,,判断是否存在一条包含字符串所有字符发路径
'''

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def DFS(map, vis, str, i, j, index, flag):

    if flag[0]:
        return
    if index == len(str):
        flag[0] = True
        return

    for k in range(4):
        next_i = i + dir[k][0]
        next_j = j + dir[k][1]
        if next_i >= 0 and next_i < len(map) and next_j >=0 and next_j < len(map[0])\
                and vis[next_i][next_j] == 0 and map[next_i][next_j] == str[index]:
            vis[next_i][next_j] = 1
            DFS(map, vis, str, next_i, next_j, index + 1, flag)
            vis[next_i][next_j] = 0


if __name__ == '__main__':
    map = [['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']]
    map_n, map_m = len(map), len(map[0])
    str = ['a','b','c','b']

    vis = [[0 for _ in range(map_m)] for _ in range(map_n)]
    flag = [False]
    for i in range(map_n):
        for j in range(map_m):
            if vis[i][j]== 0 and map[i][j] == str[0]:
                vis[i][j] = 1
                DFS(map, vis, str, i, j, 1, flag)
                vis[i][j] = 0


    if flag[0]:
        print('Yes')
    else:
        print('No')



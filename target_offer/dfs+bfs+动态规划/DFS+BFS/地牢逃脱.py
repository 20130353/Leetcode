#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 地牢逃脱.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :

#
# 最终的题意是：从给定起点（一定为'.'），按照给定的若干跳跃（可以跨过障碍，但不可以落在'x'上），到达任意一个'.'的最小步骤次数集合中，选择一个最大的！
# 如果存在一个点'.'从起点始终无法抵达，则认为起点到该点的最小距离为无穷∞，则返回-1.
# 因此，从起点开始广度优先遍历到所有可达点，记录每个可达点的最小距离，将其存入集合中。
# 然后遍历集合寻找最大的距离。如果存在一个点'.'无法抵达，直接返回-1.
# 所以是假设重点是任意点，找到一点，其达到的最短路径最大
def BFS(m, n, matrix, x, y, arr, k):
    queue = [(x, y)]
    vis = [[1 for _ in range(n)] for _ in range(m)]
    vis[x][y] = 0
    count = 1
    step = 0
    max_count = sum([matrix[i].count('.') for i in range(m)])
    while queue:
        step += 1
        length = len(queue)
        while length:
            top = queue.pop(0)
            for i in range(k):
                new_x = top[0] + arr[i][0]
                new_y = top[1] + arr[i][1]
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == '.' and vis[new_x][new_y] == 1:
                    queue.append((new_x, new_y))
                    vis[new_x][new_y] = 0
                    count += 1
                    if count == max_count:
                        return step
            length -= 1
    return -1


if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    matrix = []
    for _ in range(n):
        matrix.append(list(input().strip()))
    x, y = map(int, input().strip().split(' '))
    k = int(input().strip())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split(' '))))
    ans = BFS(m, n, matrix, x, y, arr, k)
    print(ans)

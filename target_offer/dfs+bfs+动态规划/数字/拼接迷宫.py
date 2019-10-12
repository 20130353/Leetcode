#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 拼接迷宫.py
# @Author: smx
# @Date  : 2019/8/24
# @Desc  :
import copy as cp


def dfs(arr, cur_i, cur_j, row, col, flag):
    global ans
    if ans:
        return

    if flag and (cur_i == 0 or cur_j == 0):
        ans = True
        return

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(4):
        next_i = cur_i + dir[i][0]
        next_j = cur_j + dir[i][1]
        if next_i >= 0 and next_j >= 0 and next_i < row and next_j < col and (
                arr[next_i][next_j] == 'S' or arr[next_i][next_j] == '.'):
            arr[next_i][next_j] = '#'
            dfs(arr, next_i, next_j, row, col, True)


def solution(arr, row, col):
    global ans
    for i in range(row):
        for j in range(col):
            if ans is False and arr[i][j] == 'S':
                arr[i][j] = '#'
                dfs(arr, i, j, row, col, False)
                arr[i][j] = 'S'
    return


if __name__ == '__main__':
    T = int(input().strip())
    ans = ['Yes', 'No']
    for i in range(T):
        n, m = map(int, input().strip().split(' '))
        arr = []
        for _ in range(n):
            arr.append(list(input().strip()))
        ans = False
        # shang
        new_arr = cp.deepcopy(arr)
        for i in range(n):
            arr.append(new_arr[i])
        solution(arr, 2 * n, m)
        if ans:
            print('Yes')
        else:
            # zuo
            new_arr = []
            for i in range(n):
                new_arr.append(arr[i] + arr[i])
            solution(new_arr, n, 2 * m)
            if ans:
                print('Yes')
            else:
                print('No')

#
# 2
# 2 2
# S#
# #.
# 3 3
# ...
# ###
# #S#
# No
# Yes

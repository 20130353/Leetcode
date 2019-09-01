#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 消消乐.py
# @Author: smx
# @Date  : 2019/8/24
# @Desc  :


import copy as cp
def find_tong(arr, vis, cur_i, cur_j, row, col, key, count):
    if count[0] >= 3:
        return

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(4):
        next_i = cur_i + dir[i][0]
        next_j = cur_j + dir[i][1]
        if next_i >= 0 and next_j >= 0 and next_i < row and next_j < col and vis[next_i][next_j] == 0 and \
                arr[next_i][next_j] == key:
            vis[next_i][next_j] = 1
            count[0] += 1
            find_tong(arr, vis, next_i, next_j, row, col, key, count)


def make_tong(arr, vis, cur_i, cur_j, row, col, key):
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(4):
        next_i = cur_i + dir[i][0]
        next_j = cur_j + dir[i][1]
        if next_i >= 0 and next_j >= 0 and next_i < row and next_j < col and vis[next_i][next_j] == 0 and arr[next_i][
            next_j] == key:
            vis[next_i][next_j] = 1
            make_tong(arr, vis, next_i, next_j, row, col, key)


def get_count(arr):
    n = 5
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != '#':
                ans += 1
    return ans


def solution(arr):
    n = 5
    ps = []
    for i in range(n):
        for j in range(n):
            vis = [[0] * n for _ in range(n)]
            count = [0]
            find_tong(arr, vis, i, j, n, n, arr[i][j], count)
            if count[0] >= 3:
                ps.append((i, j))

    if len(ps) == 0:
        return get_count(arr)

    min_ans = float('inf')
    for i in range(len(ps)):
        cur_i, cur_j = ps[i][0], ps[i][1]
        new_arr = cp.deepcopy(arr)
        vis = [[0] * n for _ in range(n)]
        make_tong(new_arr, vis, cur_i, cur_j, n, n, arr[cur_i][cur_j])

        temp_arr = []
        for j in range(n):
            i_col = [arr[k][j] for k in range(n) if arr[k][j] != '#']
            temp_arr.append(i_col + ['#'] * (n - len(i_col)))
        temp_arr = []
        for j in range(n - 1, -1, -1):
            i_col = [arr[k][j] for k in range(n) if arr[k][j] != '#']
            temp_arr.append(i_col)
        ans = get_count(temp_arr)
        min_ans = min(min_ans, ans)
    return min_ans


if __name__ == '__main__':
    arr = []
    for _ in range(5):
        arr.append(list(input().strip().split(' ')))
    # ans = 3
    ans = solution(arr)
    print(ans)

# 3 1 2 1 1
# 1 1 1 1 3
# 1 1 1 1 1
# 1 1 1 1 1
# 3 1 2 2 2
# 3

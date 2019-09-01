#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 西虹市首富.py
# @Author: smx
# @Date  : 2019/8/23
# @Desc  :


# 不是很懂为什么这道题不对？
def dfs(arr, m, vis, ans, cur_pos, cur_dis):
    global min_dis
    global max_value

    if m == 0:
        if cur_dis < min_dis:
            min_dis = cur_dis
            for i in range(1, len(ans)):
                max_value = max(max_value, abs(ans[i - 1] - ans[i]))
        return

    if cur_dis > min_dis:
        return

    for i in range(len(arr)):
        if vis[i] == 0:
            vis[i] = 1
            ans[cur_pos] = arr[i]
            if len(ans) == 1:
                cur_dis = arr[0]
            else:
                cur_dis += ans[cur_pos]
            dfs(arr, m - 1, vis, ans, cur_pos + 1, cur_dis)
            vis[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    max_value = 0
    min_dis = float('inf')
    leng = len(arr)
    vis = [0] * leng
    ans = [0] * m
    dfs(arr, m, vis, ans, 0, 0)
    print(max_value)

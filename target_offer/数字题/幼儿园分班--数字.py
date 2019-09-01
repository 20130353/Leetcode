#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 幼儿园分班--数字.py
# @Author: smx
# @Date  : 2019/8/19
# @Desc  :

# 存在的问题：检查存在最大深度问题，一般是没有递归的坐标问题！

import copy as cp
def solution(n, dict, cur_pos, s1, s2):
    global flag
    if flag == 1:
        return

    if cur_pos == n:
        flag = 1
        return

    f = True
    for each in s1:
        if cur_pos + 1 in dict[each] or each in dict[cur_pos + 1]:
            f = False
    if f:
        solution(n, dict, cur_pos + 1, cp.deepcopy(s1) + [cur_pos + 1], s2)

    f = True
    for each in s2:
        if cur_pos + 1 in dict[each] or each in dict[cur_pos + 1]:
            f = False
    if f:
        solution(n, dict, cur_pos + 1, s1, cp.deepcopy(s2) + [cur_pos + 1])


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    dict = {}
    for i in range(1, n + 1):
        dict[i] = []

    flag = 0
    for _ in range(m):
        a, b = map(int, input().strip().split(' '))
        dict[a].append(b)

    solution(n, dict, 0, [], [])
    print(flag)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : OGF.py
# @Author: smx
# @Date  : 2019/8/23
# @Desc  :

# 这是最简单暴力的做法，但是可能会超时！
def dfs(arr, hp, sp, hp_up, sp_up, n, count, path):
    global min_count

    if hp <= 0:
        return

    if n <= 0:
        min_count = min(min_count, count)
        return

    if count >= min_count:
        return

    # 选择1：恢复20%
    if hp != hp_up:
        dfs(arr, min(hp_up, hp * 1.2) - n, sp, hp_up, sp_up, n, count + 1, path + ' op1 ')

    # 选择2：杀死增加1sp
    new_n = n - 1
    dfs(arr, hp - new_n, min((sp + 1) % 3, sp_up), hp_up, sp_up, new_n, count + 1, path + ' op2 ')

    # 使用A技能杀死，sp=0
    if sp > 0:
        new_n = n - arr[sp - 1]
        dfs(arr, hp - new_n, 0, hp_up, sp_up, new_n, count + 1, path + ' op3 ')


if __name__ == '__main__':
    hp, sp_up, n = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    min_count = float('inf')
    dfs(arr, hp, 0, hp, sp_up, n, 0, '')
    if min_count == float('inf'):
        print('Loss')
    else:
        print(min_count)

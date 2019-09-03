#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 和为0的01数组的连续序列.py
# @Author: smx
# @Date  : 2019/9/2
# @Desc  :

def solution(arr, n, target):
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1

    sum_map = {0: 0}
    cur_sum, max_leng = 0, -1
    # max_start = -1
    for i in range(1, n + 1):
        cur_sum += arr[i - 1]
        if cur_sum not in sum_map.keys():
            sum_map[cur_sum] = i
        if (cur_sum - target) in sum_map and (i - sum_map[cur_sum - target]) > max_leng:
            max_leng = i - sum_map[cur_sum - target]
            # max_start = sum_map[cur_sum - target]
    return max_leng


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n, 0)
    print(ans)
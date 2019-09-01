#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 队列的最小修改.py
# @Author: smx
# @Date  : 2019/8/17
# @Desc  :


#  这道题存在的问题是：没有想清楚答案的本质，多算了一种情况
def solution(arr, n):
    if n == 1:
        return 0

    for i in range(n - 1, -1, -1):
        if arr[i] < arr[i - 1]:
            return i

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n)
    print(ans)

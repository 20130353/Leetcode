#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 操作序列.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
ans = [0 for i in range(n)]
left, right = 0, n - 1
flag = 0
for i in range(n - 1, -1, -1):
    if flag == 0:
        ans[left] = arr[i]
        left += 1
        flag = 1
    else:
        ans[right] = arr[i]
        right -= 1
        flag = 0
print(' '.join(map(str, ans)))

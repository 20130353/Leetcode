#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 连续子区间和.py
# @Author: smx
# @Date  : 2019/8/15
# @Desc  :


# 存在的问题： 超时！ -》 记录中间变量

def solution(arr, target, n):
    if n == 0:
        return 0
    if n == 1:
        return 1 if arr[0] > target else 0

    count, i, j = 0, 0, 0
    # 这里可以把sum记录下来优化，不用每次都加一遍,这样就对了！
    tsum = arr[0]
    while i < n and j < n:
        if tsum < target:
            j += 1
            if j < n:
                tsum += arr[j]
        else:
            tsum -= arr[i]
            count += n - j
            i += 1
    return count


if __name__ == '__main__':
    n, target = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, target, n)
    print(ans)

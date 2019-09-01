#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 01背包.py
# @Author: smx
# @Date  : 2019/8/18
# @Desc  :

# coding:utf-8
import sys


# 存在的问题： 想到dp，但是关于没有找到递归状态！有点固执在max(dp[i-1][j],dp[i-1][j-vi])上了！
# 总结：对于这种数次数，只能从顶到底的任务，存在重复计算的任务 不能拆解成动态规划

def solution(arr, w):
    if sum(arr) <= w:
        return 2 ** len(arr)

    if len(arr) <= 0 or w <= 0:
        return 1
    if len(arr) == 1 and arr[0] < w:
        return 2
    if len(arr) == 1 and arr[0] > w:
        return 1

    if w > arr[0]:
        ans = solution(arr[1:], w - arr[0]) + solution(arr[1:], w)
        # print('arr {}, w {}, ans {} '.format(arr, w, ans))
        return ans
    else:
        ans = solution(arr[1:], w)
        # print('arr {}, w {}, ans {} '.format(arr, w, ans))
        return ans


if __name__ == '__main__':
    n, w = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    # ans = solution(arr, w)
    ans = solution(arr, w)
    print(ans)

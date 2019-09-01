#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 小米大礼包--背包.py
# @Author: smx
# @Date  : 2019/8/27
# @Desc  :


# # 存在的问题：
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为60.00% --> 改掉初始值，减小循环,加入一些确切判断！
#
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为70.00% --> 将或判断改成if判断+赋值操作

def solution(n, m, arr):
    sum_arr = sum(arr)
    if m == 0 or sum_arr < m:
        return 0
    if m in arr or sum_arr == m:
        return 1

    dp = [1] + [0] * (m)
    for i in range(1, n + 1):
        for j in range(m, arr[i - 1] - 1, -1):
            if dp[j - arr[i - 1]] == 1:
                dp[j] = 1
    return dp[m]


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    ans = solution(n, m, arr)
    print(ans)

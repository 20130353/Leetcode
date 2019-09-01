#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 商品交易--背包.py
# @Author: smx
# @Date  : 2019/8/19
# @Desc  :

def solution(arr):
    n = len(arr)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = (0, 0)
    dp[0][1] = (-arr[0], 1)
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0]
        # 当前没有=max（之前有卖了，不做）
        if dp[i - 1][1][0] + arr[i] > dp[i][0][0] or (
                dp[i - 1][1][0] + arr[i] == dp[i][0][0] and dp[i - 1][1][1] + 1 < dp[i][0][1]):
            dp[i][0] = (dp[i - 1][1][0] + arr[i], dp[i - 1][1][1] + 1)

        # 当前有=max(之前没有，不做)
        dp[i][1] = dp[i - 1][1]
        if dp[i - 1][0][0] - arr[i] > dp[i][1][0] or (
                dp[i - 1][0][0] - arr[i] == dp[i][1][1] and dp[i - 1][0][1] + 1 < dp[i][1][1]):
            dp[i][1] = (dp[i - 1][0][0] - arr[i], dp[i - 1][0][1] + 1)
    return max(dp[n - 1][0], dp[n - 1][1])


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr)
    print('{} {}'.format(ans[0], ans[1]))

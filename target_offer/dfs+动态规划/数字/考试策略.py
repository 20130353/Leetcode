#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 考试策略--01背包.py
# @Author: smx
# @Date  : 2019/8/19
# @Desc  :

# 存在的问题：理解数据有问题！ pi，ai，qi，bi 是指同一道题的花费时间和收益
# 存在的问题：数据从第一个开始，就会丢掉最后一个i -》 下次直接不全前面的，然后从下标1开始
def solution(n, p, a, q, b):
    t = 120
    dp = [[0] * (t + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if j >= q[i]:
                dp[i][j] = max(dp[i - 1][j - q[i]] + b[i], dp[i - 1][j - p[i]] + a[i], dp[i - 1][j])
            elif j >= p[i]:
                dp[i][j] = max(dp[i - 1][j - p[i]] + a[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    return dp[n][t]


if __name__ == '__main__':
    n = int(input().strip())
    p, a, q, b = [0], [0], [0], [0]
    for _ in range(n):
        x1, x2, x3, x4 = list(map(int, input().strip().split(' ')))
        p.append(x1)
        a.append(x2)
        q.append(x3)
        b.append(x4)
    ans = solution(n, p, a, q, b)
    print(ans)

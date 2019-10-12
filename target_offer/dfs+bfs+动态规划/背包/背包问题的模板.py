#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 背包问题的模板.py
# @Author: smx
# @Date  : 2019/8/19
# @Desc  :

def knapsack01(n, cost, v, W):
    dp = [0] * W
    for i in range(n):
        for j in range(W - 1, cost[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - cost[i]] + v[i])
    return dp[W - 1]


# 完全背包和01背包只差物品的个数
# f[i][j]=max(f[i−1][j−k∗w[i]]+k∗v[i])∣0<=k∗w[i]<=j
# f[i][j]=max(f[i−1][j],f[i][j−w[i]]+v[i])， 这种方式需要用就从小到大
def fullsack(n, cost, v, W):
    dp = [0] * W
    for i in range(n):
        for j in range(cost[i], W):
            dp[j] = max(dp[j], dp[j - cost[i]] + v[i])
    return dp[W - 1]


# 多重背包-第一种方式
def multisack(n, cost, v, p, W):
    dp = [0] * W
    for i in range(n):
        for j in range(cost[i], W):
            for k in range(min(p[i], j // cost[i])):
                dp[j] = max(dp[j], dp[j - k * cost[i]] + k * v[i])
    return dp[W - 1]


# 多重背包-第二种方式：转为有权重的物品个数
def multisack1(n, cost, v, p, W):
    dp = [0] * W
    for i in range(n):
        num = min(p[i], W // cost[i])
        k = 1
        while num > 0:
            if k > num: k = num
            num -= k
            for j in range(W - 1, cost[i] * k - 1, -1):
                dp[j] = max(dp[j], dp[j - cost[i] * k] + v[i] * k)


# 混合背包：01背包，完全背包，多重背包 夹在一起
def missack(n, cost, p, v, W):
    dp = [0] * W
    for i in range(n):
        if p[i] == 1:
            for j in range(W - 1, cost[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - cost[i]] + v[i])
        else:
            for j in range(cost[i], W):
                dp[j] = max(dp[j], dp[j - cost[i]] + v[i])
    return dp[W - 1]


# 二维背包
def two_axis_sack(n, cost1, cost2, v, W1, W2):
    dp = [[0] * W1 for _ in range(W2)]
    for i in range(n):
        for j in range(W1, cost1[i] - 1, -1):
            for k in range(W2, cost2[i] - 1, -1):
                dp[j][k] = max(dp[j][k], dp[j - cost1[1]][k - cost2[i]] + v[i])
    return dp[W1][W2]

# 分组背包：这里需要注意，要标记出来组号，如果只有一维的话，那么找到的就不是上一组的结果的了
def arr_sack(dict_arr, dict_w, dict_v, W):
    dp = [[0] * W for _ in range(len(dict_arr))]
    # 所有组
    for inx, k in enumerate(dict_arr.keys()):
        # 所有背包重量
        for j in range(W, -1, -1):
            values = dict_arr[k]
            # 所有组成员
            for i in range(len(values)):
                dp[k][j] = max(dp[k - 1][j], dp[k - 1][j - dict_w[i]] + dict_v[i])


def K_solution(n, W, K, cost, v):
    dp = [[0] * W for _ in range(len(K))]
    a, b = [0] * W, [0] * W
    for i in range(n):
        for j in range(W, cost[i] - 1, -1):
            for l in range(1, K):
                a[l] = dp[j][l]
                b[l] = dp[j - cost[i]] + v[i]
            a[K + 1] = -1
            b[K + 1] = -1
            x, y, o = 1, 1, 1
            while o != K + 1 and (a[x] != -1 or b[y] != -1):
                if (a[x] > b[y]):
                    dp[j][o] = a[x]
                    x += 1
                else:
                    dp[j][o] = b[y]
                    y += 1
                if dp[j][o] != dp[j][o - 1]:
                    o += 1

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 糖果游戏--数字.py
# @Author: smx
# @Date  : 2019/8/27
# @Desc  :

#  这里有个问题：
# 当出现重复元素的时候拿作还是拿右呢？ --> 需要用动态规划

# --> 考虑到环形， 直接拿最大，然后切成一个环 --> 存在的问题：可能拿不到最大收益，所以需要尝试每一个位置


def solution(arr, n):
    vis = [0] * n
    max_vlaue = max(arr)
    inx = arr.index(max_vlaue)
    suma = [max_vlaue, 0]
    vis[inx] = 1
    count = 1
    i, j = inx - 1, inx + 1
    while count != n:
        i = n - 1 if i == -1 else i
        j = 0 if j == n else j

        while vis[i] != 0:
            i -= 1
            i = n - 1 if i == -1 else i

        while vis[j] != 0 and count != n - 1:
            j += 1
            j = 0 if j == n else j

        if arr[i] >= arr[j] or count == n - 1:
            select = i
            i -= 1
        else:
            select = j
            j += 1

        suma[count & 1] += arr[select]
        vis[select] = 1
        count += 1
    return suma[0] - suma[1]


def solution1(arr, n):
    max_ans = -float('inf')
    for i in range(n):
        new_arr = arr[i:]
        for each in arr[:i]:
            new_arr.append(each)
        # print(new_arr)
        dp = [[0] * n for _ in range(n)]
        dp[n - 1][n - 1] = new_arr[n - 1]
        for i in range(n - 1, -1, -1):
            for j in range(i, n, 1):
                if i == j:
                    dp[i][j] = new_arr[i]
                else:
                    dp[i][j] = max(new_arr[i] - dp[i + 1][j], new_arr[j] - dp[i][j - 1])
        max_ans = max(max_ans, dp[0][n - 1])
    return max_ans


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(int(input().strip()))
    ans = solution1(arr, n)
    print(ans)

# 10
# 30
# 38
# 63
# 29
# 70
# 71
# 75
# 71
# 27
# 27

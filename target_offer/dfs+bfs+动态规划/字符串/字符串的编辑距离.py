#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串的编辑距离.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :
#
# 存在的问题：
# 1. 初始条件没有想清楚
# 2. 字符串比较写错了

'''
    求：把 a 转换成 b 的最小操作次数，也就是所谓的最小编辑距离。
    举例： "xy" => "xz"，只需要把 y 替换成 z，因此，最小编辑距离为 1。
    "xyz" => "xy"，只需要删除 z ，因此，最小编辑距离为 1。

'''


def edit_distance(A, B):
    # print('A,B:', A, B)

    if len(A) == 0 and len(B) == 0:
        return 0
    if len(B) == 0 and len(A):
        return len(A)
    if len(A) == 0 and len(B):
        return len(B)
    if A[-1] == B[-1]:
        return edit_distance(A[:-1], B[:-1])
    else:
        res1 = edit_distance(A[:-1], B)
        res2 = edit_distance(A, B[:-1])
        res3 = edit_distance(A[:-1], B[:-1])
        # print('1,2,3:', res1, res2, res3)
        return min(res1, res2, res3) + 1

class Solution:
    def editDis(self, a, b):
        n, m = len(a), len(b)
        max_value = max(n, m)
        dp = [[max_value] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if i - 1 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j - 1 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        # for each in dp:
        #     print(each)
        return dp[n][m]


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            target = input().strip()
            ans = Solution().editDis(string, target)
            print(ans)
    except Exception as e:
        pass

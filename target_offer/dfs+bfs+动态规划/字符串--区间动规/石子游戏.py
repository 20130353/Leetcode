#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 石子游戏.py
# @Author: smx
# @Date  : 2020/2/23
# @Desc  :

class Solution:
    def stoneGame(self, arrs):
        if len(arrs) <= 1: return True
        n = len(arrs)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # i==j,表示只有一团石子，先手全部拿走
        for i in range(n):
            dp[i][i][0] = arrs[i]
            dp[i][i][1] = 0

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = l + i - 1
                left = arrs[i] + dp[i + 1][j][1]
                right = arrs[j] + dp[i][j - 1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]  # 变成先手！
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0] # 变成后手！
        gap = dp[0][n - 1][0] - dp[0][n - 1][1]
        return gap >= 0


if __name__ == '__main__':
    arrs = [5, 3, 4, 5]
    print(Solution().stoneGame(arrs))

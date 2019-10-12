# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 上台阶--进阶版.py
# description:


class Solution:
    def jumpFloorII(self, n):
        dp = [0, 1, 2] + [0] * n
        dp_sum = sum(dp)
        for i in range(3, n + 1):
            dp[i] = dp_sum + 1
            dp_sum += dp[i]
        return dp[n]


if __name__ == '__main__':
    so = Solution()
    print(so.jumpFloorII(4))

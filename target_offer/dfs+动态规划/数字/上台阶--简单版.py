# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 上台阶--简单版.py
# description:

# 存在的问题：初始值不对！初始值应该设置成题目给定的。
class GoUpstairs:
    def countWays(self, n):
        dp = [0, 0, 1, 2] + [0] * (n - 3)
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n] % (1000000007)

if __name__ == '__main__':
    so = GoUpstairs()
    print(so.countWays(3))

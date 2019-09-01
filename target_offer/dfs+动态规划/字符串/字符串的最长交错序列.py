#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串的最长交错序列.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :

class Mixture:
    def maxMixture(self, string, n):
        dp = [[0] * (2) for _ in range(n + 1)]
        for i in range(1, n + 1):
            if string[i - 1] == '0':
                dp[i][0] = max(dp[i - 1][1] + 1, dp[i - 1][0])
            else:
                dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1])
        # for each in dp:
        #     print(each)
        return max(dp[n][0], dp[n][1])


if __name__ == '__main__':
    try:
        while True:
            # n = int(input().strip())
            string = input().strip().replace(' ', '')
            ans = Mixture().maxMixture(string, len(string))
            print(ans)
    except Exception as e:
        pass

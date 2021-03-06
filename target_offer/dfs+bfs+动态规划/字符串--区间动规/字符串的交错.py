#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串的交错.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :


# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为35.00%

# 和最长公共子序列是一样的
# dp[i][j]表示若s3的前i+j个字符能够由s1前i个字符和s2的前j个字符交织而成
class Mixture:
    def chkMixture(self, s1, n, s2, m, target, k):
        if k != m + n:
            return False

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if target[i + j - 1] == s1[i - 1] and (j == 0 or dp[i - 1][j] == 1):
                    dp[i][j] = 1
                if target[i + j - 1] == s2[j - 1] and (i == 0 or dp[i][j - 1] == 1):
                    dp[i][j] = 1
        return True if dp[n][m] == 1 else False

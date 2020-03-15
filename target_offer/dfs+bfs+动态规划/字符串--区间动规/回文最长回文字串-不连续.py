#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文最长回文字串-不连续.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :


# ij需要i+1和j-1，所以需要斜着填！先填写最下面！！！！
class Solution:
    def longestPalindromeSubseq(self, s):
        if not s: return 0
        n = len(s)
        dp = [[1 for _ in range(n)] for _ in range(n)]
        for i in range(n - 2, -1, -1):
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = 2
            for j in range(i + 2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    s = ''
    print(Solution().longestPalindromeSubseq(s))

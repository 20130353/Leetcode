#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文最长回文子串.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :


# ij需要i+1和j-1，所以需要斜着填！先填写最下面！！！！
class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) <= 1: return s
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_len = 1
        max_ans = s[0]
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if max_len < 2:
                    max_len = 2
                    max_ans = s[i:i + 2]
            for j in range(i + 2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_ans = s[i:j + 1]
        return max_ans

    # 顶级写法
    # for i in range(n - 1, -1, -1):
    #     for j in range(i, n):
    #         if (a[i] == a[j]) and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
    #             dp[i][j] = 1


if __name__ == '__main__':
    s = 'ac'
    print(Solution().longestPalindrome(s))

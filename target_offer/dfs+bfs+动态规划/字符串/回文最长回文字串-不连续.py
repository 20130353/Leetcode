#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文最长回文字串-不连续.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :


# 存在的问题：遍历需要从内向外遍历

class Palindrome:
    def getLongestPalindrome(self, a, n):
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            dp[i][i] = 1
            if i + 1 < n and a[i] == a[i + 1]:
                dp[i][i + 1] = 1
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        # for i in range(n):
        #     print(dp[i])
        return dp[0][n - 1]


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            # string = 'cbabdf'
            # string = 'aaaa'
            # string = 'abcabccbadda'
            # string = 'abcabccbaddabcc'
            # string = 'adbca'
            ans = Palindrome().getLongestPalindrome(string, len(string))
            print(ans)
            # break
    except Exception as e:
        pass

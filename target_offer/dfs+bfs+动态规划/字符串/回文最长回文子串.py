#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文最长回文子串.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :


# 存在的问题：遍历需要从内向外遍历
class Palindrome:
    def getLongestPalindrome(self, a, n):
        dp = [[0] * n for _ in range(n)]
        max_leng = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if a[i] == a[j] and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if j - i + 1 >= max_leng:
                        max_leng = j - i + 1
        # for i in range(n):
        #     print(dp[i])
        return max_leng


if __name__ == '__main__':
    # string = 'cbabdf'
    # string = 'aaaa'
    # string = 'abcabccbadda'
    # string = 'abcabccbaddabcc'
    try:
        while True:
            string = input().strip()
            ans = Palindrome().getLongestPalindrome(string, len(string))
            print(ans)
    except Exception as e:
        pass

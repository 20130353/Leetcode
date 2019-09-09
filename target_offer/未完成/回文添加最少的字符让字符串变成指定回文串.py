#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文添加最少的字符让字符串变成回文串.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :

# 存在的问题：总是搞不对那个输出的顺序

class Palindrome:
    def addLeastPalindrome(self, a, require_string, n):
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            dp[i][i + 1] = 0 if a[i + 1] == a[i] else 1
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
        # for each in dp:
        #     print(each)

        new_leng = n + dp[0][n - 1]
        ans = ['0'] * new_leng
        ans_cpos = new_leng // 2
        requ_cpos = len(require_string) // 2
        key = require_string[requ_cpos]
        inx = a.index(key)
        ans[ans_cpos] = require_string[requ_cpos]
        i, j = inx - 1, inx + 1
        ans_i, ans_j = ans_cpos - 1, ans_cpos + 1
        if len(require_string) & 1 == 0:
            ans[ans_cpos + 1] = require_string[requ_cpos]
            i += 1
            ans_i += 1
        while i >= 0 and j <= n - 1:
            if a[i] == a[j]:
                ans[ans_i] = a[i]
                ans[ans_j] = a[j]
                i -= 1
                j += 1
            elif dp[i - 1][j] <= dp[i][j - 1] and 'A' <= a[i] and 'Z' >= a[i] or a[i] <= a[j]:
                ans[ans_i] = a[i]
                ans[ans_j] = a[i]
                i -= 1
            else:
                ans[ans_i] = a[j]
                ans[ans_j] = a[j]
                j += 1
            ans_i -= 1
            ans_j += 1

        if i > 0:
            ans[ans_i] = a[i - 1]
            ans[ans_j] = a[i - 1]
        if j < n:
            ans[ans_i] = a[j]
            ans[ans_j] = a[j]
        return ''.join(ans)


if __name__ == '__main__':
    try:
        while True:
            string = 'A1B21C'
            ans_string = '121'
            ans = Palindrome().addLeastPalindrome(string, ans_string, len(string))
            print(ans)
            break
    except Exception as e:
        print(e)

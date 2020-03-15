#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文字串的个数.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :

import numpy as np


class Palindrome:
    def palindromeNum(self, a, n):
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if a[i] == a[j] and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
        return np.sum(dp)


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            ans = Palindrome().palindromeNum(string, len(string))
            print(ans)
            break
    except Exception as e:
        print(e)

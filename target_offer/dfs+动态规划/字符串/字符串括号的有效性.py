#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串括号的有效性.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :


# dp的作用是找到之前匹配的最后位置，所以dp[i]表示以i作为结尾，连续括号匹配的最大长度
import re
class Solution(object):
    def validParentheses(self, a, n):
        if re.search(r'[^()]', a) is False or n & 1 == 1:
            return 'NO'

        dp = [0] * n
        for i in range(1, n):
            j = i - 1 - dp[i - 1]
            if a[i] == ')' and j >= 0 and a[j] == '(':
                dp[i] = dp[i - 1] + 2
                if j - 1 >= 0:
                    dp[i] += dp[j - 1]
        # for each in dp:
        #     print(each)
        return 'YES' if max(dp) == n else 'NO'

if __name__ == '__main__':
    # string = ')()()(((()())))('
    # string = '())'
    try:
        while True:
            string = input().strip()
            ans = Solution().validParentheses(string, len(string))
            print(ans)
    except Exception as e:
        print(e)

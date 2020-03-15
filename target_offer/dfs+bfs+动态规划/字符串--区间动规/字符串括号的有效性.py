#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串括号的有效性.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :
#
# AC
class Solution(object):
    def validParentheses(self, a, n):
        dp = [0] * n
        for i in range(1, n):
            j = i - 1 - dp[i - 1]
            if a[i] == ')' and j >= 0 and a[j] == '(':
                dp[i] = dp[i - 1] + 2
                if j - 1 >= 0:
                    dp[i] += dp[j - 1]  # 加上之前的部分!
        return True if (max(dp) == n) else False

class Solution(object):
    # 实现不需要栈，就需要记录一下（的数量
    def validParentheses(self, string, n):
        if n & 1 == 1:
            return False
        num = 0
        for i in range(n):
            if string[i] == '(':
                num += 1
            elif string[i] == ')':
                num -= 1
                if num < 0:
                    return False
            else:
                return False
        return True if num == 0 else False


if __name__ == '__main__':
    string = input().strip()
    ans = Solution().validParentheses(string, len(string))
    print('YES') if ans else print('NO')

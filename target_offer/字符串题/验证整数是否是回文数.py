#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 验证整数是否是回文数.py
# @Author: smx
# @Date  : 2020/2/8
# @Desc  :
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    x = 0
    # x = -121
    # x = 121
    x = 11
    x = 13
    x = 10
    print(Solution().isPalindrome(x))

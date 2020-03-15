#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 验证回文字符串.py
# @Author: smx
# @Date  : 2020/2/8
# @Desc  :

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 我的思路是比较大小的每一种格式
# 其他人的思路是将字符串直接全部转换成小写，且只要26个字符和数字,不使用函数整体时间快很多！

# class Solution:
#     def isPalindrome(self, s):
#         if not s or len(s) <= 1:
#             return True
#
#         A, B = 0, len(s) - 1
#         while A < B:
#             while A < len(s) and not s[A].isalnum():
#                 A += 1
#             while B >= 0 and not s[B].isalnum():
#                 B -= 1
#             if A < B:
#                 if (s[A] != s[B]) and (s[A].upper() != s[B]) and (s[A] != s[B].upper()):
#                     return False
#                 A += 1
#                 B -= 1
#         return True


class Solution:
    def isPalindrome(self, s):
        if not s or len(s) <= 1:
            return True
        s = s.lower()
        arr = 'abcdefghijklmnopqrstuvwxyz0123456789'
        A, B = 0, len(s) - 1
        while A < B:
            while A < len(s) and s[A] not in arr:
                A += 1
            while B >= 0 and s[B] not in arr:
                B -= 1
            if A < B:
                if s[A] != s[B]:
                    return False
                A += 1
                B -= 1
        return True


if __name__ == '__main__':
    string = '.1...2121,.'
    # string = ''
    # string = ' 123'
    print(Solution().isPalindrome(string))

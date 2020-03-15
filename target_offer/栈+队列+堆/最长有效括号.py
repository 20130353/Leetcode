#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最长有效括号.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 暴力算法会超时！
# 只能用dp
class Solution:
    # 存在的问题是：无法判断切断的位置，这种思路只能配合dp
    def longestValidParentheses(self, string):

        def check(s):
            left = 0
            for i in range(s.__len__()):
                if s[i] == '(':
                    left += 1
                else:
                    if left > 0:
                        left -= 1
                    else:
                        return False
            if left != 0: return False
            return True

        if not string or len(string) <= 0:
            return 0

        max_len = 0
        for i in range(string.__len__()):
            for j in range(i + 1, string.__len__()):
                new_s = string[i:j + 1]
                if new_s.__len__() % 2 == 0 and check(new_s):
                    max_len = max(max_len, new_s.__len__())
        return max_len


if __name__ == '__main__':
    string = "()((()))"
    print(Solution().longestValidParentheses(string))

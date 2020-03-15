#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 括号的分数.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :

class Solution:
    def scoreOfParentheses(self, s):
        if not s:
            return 0

        stack = []
        for each in s:
            if each == '(':
                stack.append(each)
            else:
                score = 0
                while stack and stack[-1] != '(':
                    score += stack.pop()
                stack.pop()
                if score == 0:
                    score = 1
                else:
                    score *= 2
                stack.append(score)
        return sum(stack)


if __name__ == '__main__':
    string =  "(()(()))"
    print(Solution().scoreOfParentheses(string))

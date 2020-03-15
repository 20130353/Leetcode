#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串解码.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

class Solution:
    def decodeString(self, string):
        if not string or len(string) <= 1:
            return string
        stack = []
        i = 0
        while i < len(string):
            if string[i].isdigit():
                num = ''
                while string[i].isdigit():
                    num += string[i]
                    i += 1
                stack.append(num)
            elif string[i] == '[' or string[i].isalpha():
                stack.append(string[i])
                i += 1
            else:
                s = ''
                while stack and stack[-1] != '[':
                    s = stack.pop() + s
                if stack: stack.pop()
                if stack and stack[-1].isdigit():
                    num = int(stack.pop())
                    stack.append(s * num)
                else:
                    stack.append(s)
                i += 1
        return ''.join(stack)


if __name__ == '__main__':
    # s = "3[a]2[bc]"
    s = "100[a2[c]]"
    # s = "[[a][b]][c]"
    print(Solution().decodeString(s))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 计算器.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

# 主要思想：
# 平常见到的表达式是一棵树，根节点是表达式符号。
# 中序表达式：树的中序遍历
# 前缀表达式：树的先序遍历
# 后缀表达式：树的后序遍历
# 对计算机友好的方式是使用后续表达式，所以计算过程是将中序表达式转换成后缀表达式，之后计算后缀表达式的结果。
# 这里需要明确一点：通常中序转后序结果不唯一，但是基于符号的优先级，得到结果唯一。
# 注意：可能出现连续数字，要将数字分割开来
class Solution:
    def cal_post(self, string):
        stack = []
        i = 0
        while i < len(string):
            if string[i].isdigit():
                num = ''
                while i < len(string) and string[i].isdigit():
                    num += string[i]
                    i += 1
                stack.append(int(num))
                i += 1  # 去掉分割的逗号
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if string[i] == '+': res = num1 + num2
                if string[i] == '-': res = num1 - num2
                if string[i] == '*': res = num1 * num2
                if string[i] == '/': res = num1 / num2
                stack.append(res)
                i += 1
        return stack[0]

    def in2post(self, string):
        # 需要使用逗号或者其他符号将数字分割开来
        ans = ''
        stack = []
        priority = {'+': 2, '-': 2, '*': 1, '/': 1, '(': 3}
        i = 0
        while i < len(string):
            if string[i].isdigit():
                num = ''
                while i < len(string) and string[i].isdigit():
                    num += string[i]
                    i += 1
                ans += num + ','
            else:
                if string[i] == ')':
                    while stack and stack[-1] != '(':
                        ans += stack.pop()
                    if stack: stack.pop()
                else:
                    while string[i] != '(' and stack and priority[stack[-1]] <= priority[string[i]]:
                        ans += stack.pop()
                    stack.append(string[i])
                i += 1
        while stack:
            ans += stack.pop()
        return ans

    def calculate(self, s):
        if not s or len(s) <= 0:
            return 0

        string = self.in2post(s.strip().replace(' ', ''))
        ans = self.cal_post(string)
        return ans


if __name__ == '__main__':
    string = "4*((1+1)+4)"
    print(Solution().calculate(string))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 逆波兰表达式求值.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :


class Solution:
    def evalRPN(self, arr):
        if not arr or len(arr) <= 0:
            return 0
        stack = []
        for each in arr:
            # 这里可以直接判断是否是符号，避开判断数字
            if str(each).lstrip('-').isdigit():
                stack.append(int(each))
            else:
                if len(stack) < 2: return 0
                num2, num1 = stack.pop(), stack.pop()
                if each == '+':
                    stack.append(num1 + num2)
                elif each == '-':
                    stack.append(num1 - num2)
                elif each == '*':
                    stack.append(num1 * num2)
                else:
                    if num1 <= 0 and num2 <= 0:
                        res = (-num1) // (-num2)
                    elif num1 <= 0 and num2 > 0:
                        res = -((-num1) // (num2))
                    elif num1 > 0 and num2 <= 0:
                        res = -((num1) // (-num2))
                    else:
                        res = num1 // num2
                    stack.append(res)
        return stack[-1]


if __name__ == '__main__':
    s = ["4", "3", "-"]
    print(Solution().evalRPN(s))

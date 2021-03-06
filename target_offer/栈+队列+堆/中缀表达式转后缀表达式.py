# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/23/18
# file: 中缀表达式转后缀表达式.py
# description:

'''
    将中缀表达式转成后缀表达式,再计算后缀表达式的结果
    后缀表达式是数字在前，符号在后面。
'''
dict = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2,'%':2,'^':3}


def solution(str):
    stack = []
    res = ''
    for each in str:
        if each not in ['+', '-', '*', '/', '(', ')']:
            res += each
        elif each == '(':
            stack.append('(')
        elif each == ')':
            while (stack and stack[-1] != '('):
                res += stack.pop()
            del stack[-1]
        else:
            if len(stack) == 0:
                stack.append(each)
            else:
                top_pri = dict[stack[-1]]
                cur_pri = dict[each]
                # 当前符号大于等于栈顶的符号就放入栈
                if cur_pri >= top_pri:
                    stack.append(each)
                else:
                    # 将小于当前元素的符号都出栈
                    while (stack and dict[stack[-1]] >= cur_pri):
                        res += stack.pop()
                    stack.append(each)
    while (len(stack) != 0):
        res += stack.pop()
    return res


def cal(str):
    stack = []
    ops = ['+', '-', '*', '/']
    for each in str:
        if each not in ops:
            stack.append(each)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if each == '+':
                num = float(num1) + float(num2)
            elif each == '-':
                num = float(num1) - float(num2)
            elif each == '*':
                num = float(num1) * float(num2)
            else:
                num = float(num1) / float(num2)
            stack.append(num)
    return stack[-1]


if __name__ == '__main__':
    # str = '6*(5+(2+3)*8+3)'
    str = '1+((2+3)*4)-5'
    hou_str = solution(str)
    print(hou_str)
    res = cal(hou_str)
    print(res)

# -*- coding: utf-8 -*-
# @File    : 中缀表达式转前缀表达式.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :


dict = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}


def solution(string):
    stack = []
    res = ''
    for i in range(len(string) - 1, -1, -1):
        each = string[i]
        if each not in ['+', '-', '*', '/', '(', ')']:
            res += each
        elif each == ')':
            stack.append(')')
        elif each == '(':
            while (stack and stack[-1] != ')'):
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
                    while (stack and dict[stack[-1]] >= cur_pri):
                        res += stack.pop()
                    stack.append(each)
    while (len(stack) != 0):
        res += stack.pop()
    return res[::-1]


if __name__ == '__main__':
    string = '1+((2+3)*4)-5'
    ans = solution(string)
    print(ans)

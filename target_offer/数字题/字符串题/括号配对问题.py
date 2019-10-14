# -*- coding: utf-8 -*-
# @File    : 括号配对问题.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :

# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为40.00%
# def solution(string):
#     num1, num2 = 0, 0
#     for i in range(len(string)):
#         if string[i] == '(':
#             num1 += 1
#         elif string[i] == '[':
#             num2 += 1
#         elif string[i] == ')':
#             num1 -= 1
#             if num1 < 0:
#                 return False
#         elif string[i] == ']':
#             num2 -= 1
#             if num2 < 0:
#                 return False
#         else:
#             pass
#     return True


# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为60.00%
# stack最后栈不为空！
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为60.00%
def solution(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == '[':
            stack.append('[')
        elif string[i] == ')':
            if stack.__len__() == 0 or stack.pop() != '(':
                return False
        elif string[i] == ']':
            if stack.__len__() == 0 or stack.pop() != '[':
                return False
        else:
            pass
    return len(stack) == 0


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string)
    print('true') if ans else print('false')

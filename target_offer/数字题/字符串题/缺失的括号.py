# -*- coding: utf-8 -*-
# @File    : 缺失的括号.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :


def solution(string):
    num = 0
    ans = 0
    for i in range(len(string)):
        if string[i] == '(':
            num += 1
        else:
            num -= 1
            if num < 0:
                ans += 1
                num = 0
    return ans + num


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string)
    print(ans)

# -*- coding: utf-8 -*-
# @File    : 括号匹配深度.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :

def solution(string):
    max_leng = 0
    num = 0
    for each in string:
        if each == '(':
            num += 1
        else:
            num -= 1
        max_leng = max(num, max_leng)
    return max_leng


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string)
    print(ans)

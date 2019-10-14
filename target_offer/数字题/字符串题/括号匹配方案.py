# -*- coding: utf-8 -*-
# @File    : 括号匹配方案.py
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
            if num > 0:
                ans = num if ans == 0 else ans * num
            num -= 1
            num = max(0, num)
    return ans


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string)
    print(ans)

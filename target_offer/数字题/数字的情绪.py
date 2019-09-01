#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数字的情绪.py
# @Author: smx
# @Date  : 2019/8/15
# @Desc  :

# 这道题存在的问题是：没有找每一个case，验证每一个if条件
# 请检查是否存在语法错误或者数组越界非法访问等情况, 因为0不能被整除，所以就需要判断

def solution(num, str_num):
    flag_one = False
    flag_all = True
    for i, each in enumerate(str_num):
        if each == 0 or num % each == 0:
            flag_one = True
        else:
            flag_all = False

    if flag_all:
        return 'G'
    if flag_one:
        return 'H'
    return 'S'


if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        num = int(input().strip())
        str_num = list(map(int, str(num)))
        ans = solution(num, str_num)
        print(ans)

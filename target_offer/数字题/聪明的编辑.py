#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 聪明的编辑--字符串.py
# @Author: smx
# @Date  : 2019/8/15
# @Desc  :

# 这道题有个问题是key[0],key[1],key[2], 需要判断length
# 这道题写的比较好的点是： 没有用递归

def solution(string):
    if len(set(string)) == 1:
        return string[:2]
    i = 0
    while i < len(string):
        key = string[i:i + 4]
        if len(key) >= 3 and key[0] == key[1] and key[1] == key[2]:
            string = string[:i] + string[i + 1:]
            continue
        if len(key) == 4 and key[0] == key[1] and key[2] == key[3]:
            string = string[:i + 3] + string[i + 4:]
            continue
        i += 1
    return string

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        string = input().strip()
        ans = solution(string)
        print(ans)

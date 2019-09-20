#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最长公共前缀.py
# @Author: smx
# @Date  : 2019/8/15
# @Desc  :

# 腾讯的面试题：
# 存在的问题：当时写的代码太差！


def solution(strings):
    min_leng = float('inf')
    for each in strings:
        min_leng = min(min_leng, len(each))

    for i in range(min_leng):
        k = i
        key = strings[0][k]
        for j in range(len(strings)):
            if strings[j][k] != key:
                return strings[0][:k]


if __name__ == '__main__':
    strings = ['flower', 'flow', 'flight']
    strings = ['abc', 'df', 'gh']
    ans = solution(strings)
    print(ans)

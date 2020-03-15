#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 彩色宝石项链.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :

string = input().strip()
n = string.__len__()
min_length = n
match = {}
left = 0
for right in range(2 * n):
    if string[right % n] in 'ABCDE':
        if string[right % n] not in match.keys():
            match[string[right % n]] = 1
        else:
            match[string[right % n]] += 1
    while left < right and len(match) == 5:
        # print(left, right, match)
        min_length = min(min_length, right - left + 1)
        if string[left % n] in 'ABCDE':
            match[string[left % n]] -= 1
            if match[string[left % n]] <= 0:
                match.pop(string[left % n])
        left += 1
print(n - min_length)

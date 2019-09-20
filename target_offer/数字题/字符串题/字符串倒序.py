#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串倒序.py
# @Author: smx
# @Date  : 2019/8/18
# @Desc  :

if __name__ == '__main__':
    string = input().strip().split(' ')
    ans = ''
    for inx, each in enumerate(string[::-1]):
        if each == '':
            continue
        if inx == 0:
            ans += each
        else:
            ans += ' ' + each
    print(ans)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 复读机.py
# @Author: smx
# @Date  : 2019/8/20
# @Desc  :


if __name__ == '__main__':

    strings = input().strip().split(' ')
    ans = ''
    for each in strings:
        if len(each) & 1 == 1:
            ans += ' ' + each[::-1]
        else:
            ans += ' ' + each
    print(ans.strip())

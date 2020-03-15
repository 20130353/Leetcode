#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 合法IP.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :


def check(string):
    if string.count('.') != 3:
        return False
    for each in string.split('.'):
        if int(each) > 255 or int(each) < 0:
            return False
    return True


while True:
    string = input().strip()
    if string == '':
        break
    print('YES' if check(string) else 'NO')

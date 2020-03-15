#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 时间转换.py
# @Author: smx
# @Date  : 2019/8/18
# @Desc  :


if __name__ == '__main__':
    string = input().strip()
    if string[-2:] == 'PM':
        if string[:2] == '12':
            print(string[:-2])
        else:
            print(str(int(string[:2]) + 12) + string[2:-2])
    else:
        if string[:2] == '12':
            print('00:00:00')
        else:
            print(string[:-2])

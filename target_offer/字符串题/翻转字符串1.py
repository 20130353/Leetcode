#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 翻转字符串1.py
# @Author: smx
# @Date  : 2019/8/18
# @Desc  :


strings = list(input().strip().split(' '))
ans = ' '.join(map(lambda x: x[::-1], strings))
print(ans)

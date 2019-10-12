# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/28/18
# file: 无重复字符的最长子串长度.py
# description:

'''
    给定一个子串,找到一个无重复字符的最长子串
'''
import numpy as np

def check(data,char):
    for each in data:
        if each == char:
            return False
    return True

def get_substring(data):
    if len(data) <= 0 or data == None:
        return 0

    f = []
    for i in range(0,len(data)):
        if i == 0 or check(data[i-f[i-1]:i],data[i]) == False:
            f.append(1)
        else:
            f.append(f[i-1]+1)

    max_length,end = max(f), np.argmax(f)
    substring = data[end-max_length+1:end+1]
    return substring


if __name__ == '__main__':

    # data = 'abcabcbb'
    # data = 'bbbb'
    # data = ''
    data = 'abcddff'

    res = get_substring(data)
    print(res)


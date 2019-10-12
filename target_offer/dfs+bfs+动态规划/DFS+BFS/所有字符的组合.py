# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 所有字符的组合.py
# description:

'''
    给定abc,输出a,b,c,ab,ac,abc
    和字符串排列是一样的，只是多加了空字符
'''

def combination(res, chars, index, pos):
    if index == 3:
        for each in res:
            if each != '':
                print(each, end='')
        print('\n')
        return
    for j in range(pos, len(chars)):
        res[index] = chars[j]
        combination(res, chars, index + 1, j + 1)

if __name__ == '__main__':
    chars = ['', 'a', 'b', 'c']
    for each in chars:
        if each != '':
            print(each)

    res = ['', '', '']
    combination(res, chars, 0, 0)

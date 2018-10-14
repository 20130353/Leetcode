# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 字符串的排列.py
# description:

'''
    给定abc,输出abc的全排列
'''


def permutation(res,chars,bools,index):
    if index == 3:
        for each in res:
            print(each,end='')
        print('\n')
        return

    for inx in range(len(chars)):
        if bools[inx] == 0:
            bools[inx] = 1
            res[index] = chars[inx]
            permutation(res,chars,bools,index+1)
            bools[inx] = 0
    return

if __name__ == '__main__':

    chars = ['a','b','c']
    bools = [0,0,0]
    res = ['','','']
    permutation(res,chars,bools,0)

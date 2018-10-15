# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 数值的整数次方.py
# description:

'''
    实现power函数
    解法1.将指数分成正负,分别求他们的乘积
    解法2.用递归的方式划分
'''

def get_multiply(a,n):
    for i in range(n):
        a = a * a
    return a

def solution1(a,p):
    if a == 0:
        return 0
    elif p == 0:
        return 1
    elif p > 0:
        return get_multiply(a,p)
    else:
        res = get_multiply(a,p)
        if res == 0:
            return 0
        else:
            return 1/res
    return

def solution2(a,p):

    if a == 0:
        return 0
    if p == 0:
        return 1
    if p == 1:
        return a
    if p & 1 == 0:
        return solution2(a,p//2) * solution2(a,p//2)
    else:
        return solution2(a,p//2) * solution2(a,p//2) * a

if __name__ == '__main__':

    a,power = 3,1
    res = solution2(a,power)
    print(res)

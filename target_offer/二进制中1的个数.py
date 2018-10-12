# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/11/18
# file: 二进制中1的个数.py
# description:

# reference link:https://www.cnblogs.com/cotyb/p/5186461.html

import numpy as np

# convert the number to binary number
# def positive2binary(n):
#     if n <= 0:
#         return 0
#
#     b = []
#     while(n):
#         b.insert(n%2)
#         n /= 2
#
#     return b
#
# def negative2binary(n):
#     if n >= 0:
#         return 0
#
#     obn = -n
#     b = []
#     while(obn>0):
#         b.insert(0,np.int(obn%2))
#         obn = np.floor(obn/2)
#
#     ones_code = [-each for each in b]
#     ones_code[-1] = ones_code[-1] + 1
#     for inx in range(len(ones_code)-1,0,-1):
#         if ones_code[inx] >= 2:
#             ones_code[inx] = 1
#             if inx < len(ones_code)-1:
#                 ones_code[inx+1] = ones_code[inx+1] + 1
#
#     return ones_code


def count(n):
    cnt = 0
    while(n):
        cnt += 1
        n = (n-1) & n
    return cnt

# advanced version
# 因为在Python中，对于超出32位的大整数，会自动进行大整数的转变，这就导致了在右移位过程中，
# 不会出现移到了0的情况，也就会造成了死循环。
# 在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
def NumberOf1(n):
    count = 0
    while n&0xffffffff != 0:
        count += 1
        n = n & (n-1)
    return count

if __name__ == '__main__':
    # res = negative2binary(-5)
    # for inx in range(len(res)):
    #     print(res[inx],end='')

    print(NumberOf1(-5))
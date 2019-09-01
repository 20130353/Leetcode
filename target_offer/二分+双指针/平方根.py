#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 平方根.py
# @Author: smx
# @Date  : 2019/8/22
# @Desc  :


def solution(A):
    if A < 0:
        return -1

    if A == 0:
        return 0

    maxi = max(1, int(A))
    d = 0.000001
    for i in range(maxi + 1):
        if i ** 2 == A or i ** 2 == (A - d):
            return i
    return -1


if __name__ == '__main__':
    A = 5
    # A = 1
    # A = 0
    #

    ans = solution(A)
    print(ans)

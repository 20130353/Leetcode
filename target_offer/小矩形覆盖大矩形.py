# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 小矩形覆盖大矩形.py
# description:

def cover(n):
    if n < 0 :
        return 0

    a  = [0,1,4]
    if n < 2:
        return a[n]

    for i in range(2,n):
        a.append(a[i-1]  + a[i-2])
    return a[n]

if __name__ == '__main__':
    print(cover(0))
    print(cover(1))
    print(cover(2))
    print(cover(8))
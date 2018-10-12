# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 变态青蛙跳.py
# description:

def jump(n):
    if n <= 0:
        return 0
    else:
        return 2**(n-1)

if __name__ == '__main__':
    print(jump(0))
    print(jump(1))
    print(jump(2))
    print(jump(3))
    print(jump(100))

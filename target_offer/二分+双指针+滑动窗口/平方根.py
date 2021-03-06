#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 平方根.py
# @Author: smx
# @Date  : 2019/8/22
# @Desc  :

# 有一些计算结果是因为平方结果和y的差值小于极小值的到,但是事实上y有对应的整数根, 所以为了排除这种情况, 就将根四舍五入,确定整数是不是y的平凡根.
def is_square(x, mid):
    a = round(mid)
    if a * a == x:
        return a
    else:
        return mid


# 这里用了个小技巧, mid==x/mid,这样可以省去使用mid*mid溢出.
def binary_sqrt(x):
    if x == 0 or x == 1:
        return x
    low, high = 0, max(1, x)
    d = 0.0000001
    while True:
        mid = low + (high - low) / 2
        if mid == x / mid or abs(mid - x / mid) <= d:
            return is_square(x, mid)
        elif mid < x / mid:
            low = mid
        else:
            high = mid


# 这里是用f(x)=0的方式求x，不能用求导的方式，因为求导的过程中x直接=0了，没有办法求。
# def newton_sqrt(y0):
#     x = y0
#     d = 0.000001
#     while True:
#         nextx = x - (x * x - y0) / (2 * x)
#         if abs(nextx - y0 / nextx) <= d:
#             return is_square(y0, nextx)
#         x = nextx
#

# 进一步优化公式
# 根据切线方程得到的公式！
def newton_sqrt(y0):
    x = y0
    d = 0.000001
    while True:
        nextx = (x * x + y0) / (2 * x)
        if abs(nextx - y0 / nextx) <= d:
            return is_square(y0, nextx)
        x = nextx


if __name__ == '__main__':
    print(binary_sqrt(9))
    print(binary_sqrt(3))
    print(binary_sqrt(4))
    print(binary_sqrt(5))
    print(binary_sqrt(9))

    print('---------------')

    print(newton_sqrt(9))
    print(newton_sqrt(3))
    print(newton_sqrt(4))
    print(newton_sqrt(5))
    print(newton_sqrt(9))

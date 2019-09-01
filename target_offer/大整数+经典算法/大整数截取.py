#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 大整数截取.py
# @Author: smx
# @Date  : 2019/8/23
# @Desc  :

# 好的地方：第一时间把测试用例的答案写上了，保证的基本的9%得分
# 总结这道题：
# 不敢相信是测试样例错了，导致我没有在第一时间找到答案，浪费了很多时间理解题意。
# 后面要是能再快一点写完就可以拿满分了，写带代码慢了一点，边界上没加右边界。


def solution(string, A):
    count = 0
    leng = len(string)
    for i in range(leng):
        for j in range(i + 1, leng + 1):
            # print('{} {} {}'.format(i, j, sting[i:j]))
            sub = string[i:j]
            ans = int(sub) % 1000000007
            print(ans)
            if ans == A:
                count += 1
    return count


if __name__ == '__main__':
    sting = input().strip()
    n = int(input().strip())

    for i in range(n):
        A = int(input().strip())
        ans = solution(sting, A)
        print(ans)

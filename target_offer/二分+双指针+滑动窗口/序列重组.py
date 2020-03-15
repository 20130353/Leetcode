#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 序列重组.py
# @Author: smx
# @Date  : 2019/8/15
# @Desc  :

from itertools import permutations


def solution(num1, num2, m):
    p1 = list(set(permutations(num1, len(num1))))
    p2 = list(set(permutations(num2, len(num2))))

    total_ans = None
    for i in range(len(p1)):
        v1 = p1[i]
        for j in range(len(p2)):
            v2 = p2[j]
            temp_ans = [sum(map(int,each)) % m for each in zip(v1, v2)]
            string_ans = ''.join(list(map(str, temp_ans)))
            if total_ans is None:
                total_ans = string_ans
            else:
                total_ans = max(total_ans, string_ans)

    while total_ans[0] == '0':
        total_ans = total_ans[1:]
    return total_ans

if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    num1 = input().strip().split(' ')
    num2 = input().strip().split(' ')
    ans = solution(num1, num2, m)
    print(' '.join(ans))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 公平划分--数字.py
# @Author: smx
# @Date  : 2019/8/17
# @Desc  :

# 请检查是否存在语法错误或者数组越界非法访问等情况
# case通过率为80.00%
#
# 26
# 4
# 435 5742 292529 83782 3627 37267 326752 4353 99279 23 2526 26362 4342 3232 3290987 535 3242 4242 54674 685 342 6854 548584 6585 54 4262
# 对应输出应该为:
# 19017122
# 你的输出为:
# not enough values to unpack (expected 2, got 1)
# 存在的问题：读取文件的问题！

def cal_gap(a, b):
    dis = 0
    # print('{} {}'.format(N1, N2))
    for i in a:
        for j in b:
            dis += abs(i - j)
    return dis


def solution(arr, n, k, pos, N1, N2, min_dis):
    if cal_gap(N1, N2) >= min_dis[0]:
        return

    if pos >= n:
        min_dis[0] = min(min_dis[0], cal_gap(N1, N2))
        return

    if len(N1) < k:
        N1.append(arr[pos])
        solution(arr, n, k, pos + 1, N1, N2, min_dis)
        N1.pop()

    if len(N2) < n - k:
        N2.append(arr[pos])
        solution(arr, n, k, pos + 1, N1, N2, min_dis)
        N2.pop()
    return


if __name__ == '__main__':
    try:
        while True:
            n, k = map(int, input().strip().split(' '))
            arr = list(map(int, input().strip().split(' ')))
            min_dis = [float('inf')]
            solution(arr, n, k, 0, [], [], min_dis)
            print(min_dis[0])
            break
    except Exception as e:
        print(e)

# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 两个有序数组的中位数.py
# description:

'''
给定两个有序数组,求他们的中位数
解法1: 归并排序,求(n+m)/2 个
解法2: 分成四个子数组,用(n/2 + m/2)和k之间的关系确定第k个元素在哪里
相关题目:求两个数组的第k个数
'''
import numpy as np


def solution(A, B, m, n):
    if (m + n) & 1 == 0:
        return (get_median(A, B, m, n, (m + n) / 2) + get_median(A, B, m, n, (m + n) / 2 + 1)) / 2
    else:
        return get_median(A, B, m, n, (m + n) / 2 + 1)


def get_median(A, B, m, n, k):
    if n <= 0:
        return A[k - 1]
    if m <= 0:
        return B[k - 1]
    if k <= 1:
        return min(A[0], B[0])
    # print(n//2,m//2)
    if (B[np.int(n // 2)] >= A[np.int(m // 2)]):
        if m // 2 + n // 2 + 1 >= k:
            return get_median(A, B, m, np.int(n // 2), k)
        else:
            return get_median(A + m / 2 + 1, B, m - m / 2 + 1, n, k - (m / 2 + 1))
    else:
        if ((m / 2 + 1 + n / 2) >= k):
            return get_median(A, B, m / 2, n, k);
        else:
            return get_median(A, B + n / 2 + 1, m, n - (n / 2 + 1), k - (n / 2 + 1));


if __name__ == '__main__':
    data1 = [1, 2, 3, 4]
    data2 = [2, 3, 4, 5]
    res = get_median(data1, data2, 4, 4, 2)
    print(res)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 公平划分--数字.py
# @Author: smx
# @Date  : 2019/8/17
# @Desc  :

# 感觉会超时！
# 存在的问题是：只考虑了选择k，但是没有考虑另一个集合的元素是否完整
# 存在的问题是：集合的边界错误，导致case过不了！下次应该自己多写几个案例。不要考虑异常的case，要多些几个正常的case
# def solution(arr, n, k, pos, N1):
#     if k == 0:
#         sub1, sub2 = [], []
#         for i, each in enumerate(N1):
#             if each:
#                 sub1.append(arr[i])
#             else:
#                 sub2.append(arr[i])
#         dis = 0
#         for i in sub1:
#             for j in sub2:
#                 dis += abs(i - j)
#         global min_dis
#         print('N1 {}, N2 {}, dis {}'.format(sub1, sub2, dis))
#         min_dis = min(min_dis, dis)
#
#     if pos + 1 <= n:
#         N1[pos] = True
#         solution(arr, n, k - 1, pos + 1, N1)
#
#         N1[pos] = False
#         solution(arr, n, k, pos + 1, N1)

# 改进点：加k和n-k的判断
# 请检查是否存在语法错误或者数组越界非法访问等情况
# case通过率为80.00%
# 这道题归在了dp，以为要用到中位数的性质，中位数和其他数的绝对差最小，
# 但是后面取数会影响前面取数的结果，不满足动态规划的无后效性，也就行不通了。
# 还是感谢大佬们的思路，用的是回溯，不知道为什么总说数组访问越界，只过了80%

def solution(arr, n, k, pos, N1, N2, min_dis):
    if N1.__len__() == 0:
        gap = sum(N2)
    elif N2.__len__() == 0:
        gap = sum(N1)
    else:
        gap = sum([abs(i - j) for j in N1 for i in N2])

    if gap >= min_dis[0]:
        return

    if pos >= n:
        # print('N1 {},N2 {} gap {}'.format(N1, N2, gap))
        min_dis[0] = min(min_dis[0], gap)
        return

    if N1.__len__() < k:
        N1.append(arr[pos])
        solution(arr, n, k, pos + 1, N1, N2, min_dis)
        N1.pop()

    if N2.__len__() < n - k:
        N2.append(arr[pos])
        solution(arr, n, k, pos + 1, N1, N2, min_dis)
        N2.pop()
    return


if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    min_dis = [float('inf')]
    solution(arr, n, k, 0, [], [], min_dis)
    print(min_dis[0])

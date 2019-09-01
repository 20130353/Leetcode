#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 篮球队问题--数字.py
# @Author: smx
# @Date  : 2019/8/19
# @Desc  :


import copy as cp


# 存在的问题：请检查是否存在语法错误或者数组越界非法访问等情况-- 超时！ -》 中间去掉以后绝对不可能达到的方案！
# 存在的问题：运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大 -> 优化结束条件
# 存在的问题：运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大 ->
# 简化条件，简化成A-集合的最小值<B集合+A的最小值，所以可以先排序,但是也不能剪枝！
# 改成dp: dp[i][j] 到第i个物品总和为j的总数量，判断是否满足条件 --》


def judge(s1, s2, sum1, sum2):
    if sum1 <= sum2:
        return False

    if sum1 - sum2 >= 2 * min(s1):
        return False

    return True


def solution(n, cur_pos, arr, s1, s2, ns1, ns2, nsum):
    if cur_pos == n:
        if judge(s1, s2, ns1, ns2):
            global count
            count += 1
        return

    new_s1 = cp.deepcopy(s1) + [arr[cur_pos]]
    solution(n, cur_pos + 1, arr, new_s1, s2, ns1 + arr[cur_pos], ns2, nsum)

    new_s2 = cp.deepcopy(s2) + [arr[cur_pos]]
    ns2 += arr[cur_pos]
    if ns2 > ns1 + (nsum - ns1 - ns2):
        return
    solution(n, cur_pos + 1, arr, s1, new_s2, ns1, ns2, nsum)


# def solution(arr, n):
#     all_sum = sum(arr)
#     res = 0
#     dp = [[0 for i in range(all_sum + 1)] for i in range(2)]
#     for i in range(all_sum + 1):
#         dp[0][i] = 0
#     dp[0][0] = 1
#     for i in range(0, n):
#         for j in range(1, all_sum + 1):
#             dp[1][j] = dp[0][j]  # 这里是用dp[0][j],表示之前的dp[i-1][j]，省空间
#             if arr[i] <= j:
#                 dp[1][j] = dp[1][j] + dp[0][j - arr[i]]
#                 if j > all_sum - j and j - arr[i] < all_sum - j + arr[i]:
#                     res = res + dp[0][j - arr[i]]  # 这里满足条件的就会计入，因为剩下的默认装入B，所以整体已经分成A和B了
#         for j in range(1, all_sum):
#             dp[0][j] = dp[1][j]
#     return res


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    arr.sort()
    count = 0
    nsum = sum(arr)
    solution(n, 0, arr, [], [], 0, 0, nsum)
    print(count)

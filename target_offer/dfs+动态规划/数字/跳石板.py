#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 跳石板.py
# @Author: smx
# @Date  : 2019/9/2
# @Desc  :
#
# 您的代码已保存
# 请检查是否存在语法错误或者数组越界非法访问等情况
# case通过率为30.00% -->超内存
# def yueshu(n):
#     ans = []
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             ans.append(i)
#     return ans
# def dfs(n, target, count, min_count):
#     global yueshu_dict
#     if n > target:
#         return
#
#     if count >= min_count[0]:
#         return
#
#     if n == target:
#         min_count[0] = min(min_count[0], count)
#         return
#
#     if n not in yueshu_dict.keys():
#         yueshu_dict[n] = yueshu(n)
#     arr = yueshu_dict[n]
#
#     for each in arr:
#         dfs(n + each, target, count + 1, min_count)
#

# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为30.00%
# 没有考虑n不是4的情况

# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为40.00%

def solution(n, target):
    if n == target:
        return 0
    if n < 4 or target < n:
        return -1
    dp = [0] + [float('inf')] * target
    for i in range(n, target + 1):
        for step in range(2, i // 2):
            if (i - step) % step == 0 and (i - step) >= n:
                dp[i - n] = min(dp[i - n], dp[i - step - n] + 1)
    return dp[target - n]


if __name__ == '__main__':
    n, target = map(int, input().strip().split(' '))
    # min_count = [float('inf')]
    # yueshu_dict = {}
    # dfs(n, target, 0, min_count)
    ans = solution(n, target)
    print(-1) if ans == float('inf') else print(ans)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 笔记精选--数字.py
# @Author: smx
# @Date  : 2019/8/18
# @Desc  :

# 温馨提示：有时候，申请大的全局数组会导致超时，如果有此类情况，请检查您的全局数组是否超过题目要求的内存大小。
# 排除这个错误后，再检查别的情况引起的超时错误：例如死循环、循环结束条件错误等，或者需要更好的算法！
#
#
# def solution(arr, vis, cur_pos, n, count):
#     if cur_pos >= n:
#         global max_count, max_num
#         if max_count == count and max_num > sum(vis):
#             max_num = sum(vis)
#         elif max_count < count:
#             max_count = count
#             max_num = sum(vis)
#         return
#
#     solution(arr, vis, cur_pos + 1, n, count)
#
#     if vis[cur_pos - 1] is False:
#         vis[cur_pos] = True
#         solution(arr, vis, cur_pos + 1, n, count + arr[cur_pos])
#         vis[cur_pos] = False


# 存在的问题：超时！ -》 改成dp，需要保存两个状态，取和不取的状态
# dp[i][1] = max(dp[i-1][0]+a[i],dp[i-1][1])
# dp[i][0] = dp[i-1][1]

# 存在的问题：当地点赞数量相同的时候，取笔记本数量较小的一种方式 -》 记录笔记本数量

def solution(arr):
    n = len(arr)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = (0, 0)
    dp[0][1] = (arr[0], 1)
    for i in range(1, n):
        dp[i][0] = dp[i - 1][1]
        LT, LF = dp[i - 1][1], dp[i - 1][0]
        if (LF[0] + arr[i] < LT[0]) or (LF[0] + arr[i] == LT[0] and LF[1] + 1 > LT[1]):
            dp[i][1] = dp[i - 1][1]
        else:
            dp[i][1] = (dp[i - 1][0][0] + arr[i], dp[i - 1][0][1] + 1)
    return max(dp[n - 1][0], dp[n - 1][1])

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr)
    print(ans)

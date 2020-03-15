#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 编码字符串--字符串--区间动规.py
# @Author: smx
# @Date  : 2019/8/20
# @Desc  :

# 不知道为什么暴力解法就是不过！
# def solution(string, path):
#     ans = re.findall(r'\d+', string)
#     if len(ans) != 1:
#         return 0
#
#     if string == '':
#         return 0
#
#     if len(string) == 1:
#         print(path + ' ' + string)
#         if '0' <= string and string <= '9':
#             return 1
#         else:
#             return 0
#
#     if len(string) == 2:
#         if string <= '26':
#             print('{} {} {}'.format(path, string[0], string[1]))
#             print('{} {}'.format(path, string))
#             return 2
#         else:
#             print('{} {} {}'.format(path, string[0], string[1]))
#             return 1
#
#     if '0' <= string[:2] and string[:2] <= '26':
#         return solution(string[1:], path + ' ' + string[0]) + solution(string[2:], path + ' ' + string[:2])
#     else:
#         return solution(string[1:], path + ' ' + string[0])

# 存在的问题：1. 存在的0的状况没有考虑进去
# 存在的问题：没有考虑26的情况
def solution(string):
    if len(string) == 0 or string == '0':
        return 0
    n = len(string)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        if '1' <= string[i - 1] and string[i - 1] <= '9':
            dp[i] = dp[i - 1]
        if (string[i - 2] == '2' or string[i - 1] == '1') and '0' <= string[i - 1] and string[i - 1] <= '6':
            dp[i] += dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    n = input().strip()
    ans = solution(n)
    print(ans)

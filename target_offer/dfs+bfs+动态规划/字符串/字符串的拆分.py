#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 寻找子串--字符串.py
# @Author: smx
# @Date  : 2019/8/17
# @Desc  :

# 第一种情况：过掉当前这个字符,这个可以不要，直接用之前的max来表示，最大的可以拼接的长度一定是max_ans
# max_ans = max(max_ans, dp[j])
# 改了结果之后正确率达到65%，但是还是超时！
# 第二种情况：每次判断是否能找到一个匹配去增加字串的长度，但是增加的结果不一定会比max_ans大，只有在max_ans的结果上加1，才会比max_ans大，所以只需要判断max_ans的位置之前是否能增加一个匹配。
# 但是存在的问题是：max可能出现的位置有多个，找一个位置最大的，同时但是可能符合的模式串又可能有多个，还可以改进，直到已经不是max_ans

# 改了结果之后正确率达到75%
# 可以把每个字符和字符串数组的匹配提前计算出来，保存下来，改进的地方是判断pattern是否在字符串数组中！
# 存在的问题是：计算时间复杂度的时候sum这些的函数的复杂度也要算上。

# 存在的问题是：有错误case！
# 所以这道题总结下来：
# 简单的递归--> 超时！
# dp-> 超时
# dp +  其他保存好前缀数组 -> 正确答案

def get_next(s):
    next_arr = [-1] * (len(s) + 1)
    i, cnt = 0, -1
    while i < len(s):
        if cnt == -1 or s[cnt] == s[i]:
            cnt += 1
            i += 1
            next_arr[i] = cnt
        else:
            cnt = next_arr[cnt]
    return next_arr


def kmp(s1, s2, s):
    next_arr = get_next(s2)
    i, j = 0, 0
    while i < len(s1):
        if s1[i] == s2[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next_arr[j]
        if j == len(s2):
            s[i - j].append(i)
            j = next_arr[j]
    return s


# 阶梯思路：KMP+DP
# 这里的拆分不需要连续，所以可以用直接跳的方式，如果是连续的话，需要用1表示
def solution(arr, T,n):
    s = {}
    for i in range(n):
        s[i] = []
    for each in arr:
        s = kmp(T, each, s)

    dp = [0] * (n + 1)
    max_ans = 0
    for i in range(n - 1, -1, -1):
        for j in s[i]:  # 找到每个匹配的模式，计算在当前模式之下可以获得的最大子串个数
            if dp[j] < max_ans:
                break
            max_ans = max(dp[j] + 1, max_ans)
        dp[i] = max_ans

    return dp[0]

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().strip())
    T = input().strip()
    ans = solution(arr, T,len(T))
    print(ans)

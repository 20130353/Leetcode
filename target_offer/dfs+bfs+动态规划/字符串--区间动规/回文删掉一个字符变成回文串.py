#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文删掉一个字符变成回文串.py
# @Author: smx
# @Date  : 2019/8/13
# @Desc  :


#  思路：尝试删除每一个字符，判断删除之后的字符串是否是回文
#  判断是否是回文有两种方法：1. 双指针(时间复杂度N,可以判断整体是否是回文） 2. 动态规划（时间复杂度N^2，判断字符串的全部回文）
#  删除字符就是找序列问题！
class Solution:
    def judge_double(self, string):
        new_str = '#'.join(string)
        i, j = 0, len(new_str) - 1
        while new_str[i] == new_str[j] and i < j:
            i += 1
            j -= 1
        return True if i == j else False

    def judge_dp(self, a):
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        # 判断回文必须从判断小串
        for i in range(n - 1, 0, -1):
            for j in range(i, n):
                if a[i] == a[j] and (i == j or i == j - 1 or dp[i - 1][j - 1] == 1):
                    dp[i][j] = 1
        return dp[0][n - 1]

    def solution(self, string):
        n = len(string)
        for i in range(-1, n):
            temp = ''
            if i != -1:
                temp += string[:i]
            temp += string[i + 1:]
            flag = self.judge_dp(temp)
            if flag:
                return i

def solution(string):
    i = 0
    leng = len(string)
    while i <= (leng // 2) and string[i] == string[leng - i - 1]:
        i += 1
    if i > leng // 2:  # 整个是回文字符串
        return -1
    else:
        if string[i] == string[leng - i - 2]:  # 删除掉左边的字符
            return leng - i - 1
        else:  # 删除掉右边的字符
            return i


if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        string = input().strip()
        ans = solution(string)
        print(ans)

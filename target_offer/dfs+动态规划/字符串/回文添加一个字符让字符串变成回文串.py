#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文添加最少的字符让字符串变成回文串.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :


# 存在的问题：没有考虑重复出现的情况

# class Palindrome:
#     # 算法思路是先找到最长回文字串，然后找左右两边的字符交集，总长-交集*2=需要增加的字符
#     def addLeastPalindrome(self, a, n):
#         dp = [[0] * n for _ in range(n)]
#         max_start, max_leng = 0, 0
#         for i in range(n - 2, -1, -1):
#             for j in range(i, n):
#                 if (a[i] == a[j]) and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
#                     dp[i][j] = 1
#                     if j - i + 1 >= max_leng:
#                         max_leng = j - i + 1
#                         max_start = i
#
#         lleft = string[:max_start]
#         lright = string[max_start + max_leng:]
#         if len(lleft) <= len(lright):
#             inter = [each for each in lleft if each in lright]
#         else:
#             inter = [each for each in lright if each in lleft]
#         return n - len(inter) * 2 - max_leng + n


# 我的dp存在的问题初始值设置不对，也找不到路径
# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为15.00%
class Palindrome:
    def addLeastPalindrome(self, a, n):
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            dp[i][i + 1] = 0 if a[i + 1] == a[i] else 1
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
        if dp[0][n - 1] == 1:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            ans = Palindrome().addLeastPalindrome(string, len(string))
            print(ans)
    except Exception as e:
        pass

# -*- coding: utf-8 -*-
# @File    : 平方串.py
# @Author  : smx
# @Date    : 2019/10/13 
# @Desc    :

# AC
# 一个字符串和其自身的连接所得的字符串称为该字符串的平方串。例如字符串abc的平方串为”abc”+”abc”=”abcabc”，”abcabc”称为”abc”的平方串。
class Solution():
    def max_common_sequence(self, s1, s2, n, m):
        if not s1 or not s2 or n <= 0 or m <= 0:
            return -1

        if s1 in s2:
            return s1.__len__()

        if s2 in s1:
            return s2.__len__()

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]

    def solution(self, string):
        max_leng = -float('inf')
        # 找到左右两个部分的最长公共子串
        for i in range(string.__len__()):
            pre, post = string[:i + 1], string[i + 1:]
            num = self.max_common_sequence(pre, post, pre.__len__(), post.__len__())
            if num > max_leng:
                max_leng = num
        return max_leng * 2


if __name__ == '__main__':
    string = input().strip()
    ans = Solution().solution(string)
    print(ans)

# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长公共子串
# description:

# dp过程
# 运行超时: 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为66.67 %

# 运行超时: 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为14.29 %
# 应该是语言的问题！
class Solution:
    def max_common_subarr(self, s1, s2, m, n):
        if not s1 or not s2:
            return -1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_leng, max_end = -1, -1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_leng:
                        max_leng = dp[i][j]
                        max_end = i
        if max_leng == -1:
            return -1


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    ans = Solution().max_common_subarr(s1, s2, len(s1), len(s2))
    print(ans)

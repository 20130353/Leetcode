# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长公共子串
# description:

'''

最长公共子串和最长公共子序列的区别是:
子串一定是连续的子序列
子序列可以是数组中不连续的数组的组合

'''


class Solution:

    def max_common_subsequence(self, s1, s2):

        if not s1 or not s2:
            return 0

        m, n = len(s1), len(s2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        max_len = 0
        max_index = -1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        max_index = i - max_len

        return max_len, max_index


if __name__ == '__main__':
    s1 = [3, 5, 7, 4, 8, 6, 7, 8, 2]
    s2 = [3, 4, 7, 4, 8, 6, 7, 9, 0]
    print(Solution().max_common_subsequence(s1, s2))

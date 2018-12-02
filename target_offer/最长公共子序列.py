# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长公共子序列
# description:


# 反思:
# 1. 写动规函数,开始就把m和n写出来
# 2. 如果扩展dp数组的大小的话,小心原来的数组可能溢出!
class Solution:

    def max_common_sequence(self, s1, s2):

        if not s1 or not s2:
            return 0
        m, n = len(s1), len(s2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


if __name__ == '__main__':
    s1 = [3, 5, 7, 4, 8, 6, 7, 8, 2]
    s2 = [1, 3, 4, 5, 6, 7, 7, 8]
    print(Solution().max_common_sequence(s1, s2))

# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长公共子序列
# description:

# 反思:
# 1. 写动规函数,开始就把m和n写出来
# 2. 如果扩展dp数组的大小的话,小心原来的数组可能溢出!
class Solution:
    def max_common_sequence(self, s1, s2, n, m):
        if not s1 or not s2 or n <= 0 or m <= 0:
            return -1
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i, j = n - 1, m - 1
        ans = ''
        while i >= 0 or j >= 0:
            if s1[i] == s2[j]:
                ans = s1[i] + ans
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] and i >= j:
                i -= 1
            else:
                j -= 1
        return ans

if __name__ == '__main__':
    try:
        while True:
            s1 = input().strip()
            s2 = input().strip()
            ans = Solution().max_common_sequence(s1, s2, len(s1), len(s2))
            print(ans)
    except Exception as e:
        print(e)

# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长公共子串
# description:
class Solution:
    def max_common_subarr(self, s1, s2, m, n):
        if not s1 or not s2:
            return -1
        dp = [[0] * n for _ in range(m)]
        max_leng, max_end = 0, -1
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_leng:
                        max_leng = dp[i][j]
                        max_end = i
        # for each in dp:
        #     print(each)
        # print(max_leng)
        return s1[max_end - max_leng + 1:max_end + 1]


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    ans = Solution().max_common_subarr(s1, s2, len(s1), len(s2))
    print(ans)

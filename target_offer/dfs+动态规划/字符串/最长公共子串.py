# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长公共子串
# description:

# 没有AC

class Solution:
    # dp过程
    # 您的代码已保存
    # 运行超时: 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
    # case通过率为66.67 %
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

    # dp优化
    # 算法思想：如果a[i]==a[j]，i++，j++，否则的话从j中找到和a[i]相等的元素，如果没有的话i++
    # 您的代码已保存
    # 运行超时: 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
    # case通过率为23.81 %
    def solution(self, s1, s2, n, m):
        row, col = 0, m - 1
        max_leng, max_end = 0, -1
        while row < n:
            i, j = row, col
            leng = 0
            while i < n and j < m:
                if s1[i] == s2[j]:
                    leng += 1
                    if leng > max_leng:
                        max_leng = leng
                        max_end = i
                else:
                    leng = 0
                i += 1
                j += 1
            if col > 0:  # i从0开始，j从m-1开始到0，
                col -= 1
            else:
                row += 1
        return s1[max_end - max_leng + 1:max_end + 1]


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    ans = Solution().max_common_subarr(s1, s2, len(s1), len(s2))
    # ans = Solution().solution(s1, s2, len(s1), len(s2))
    print(ans)

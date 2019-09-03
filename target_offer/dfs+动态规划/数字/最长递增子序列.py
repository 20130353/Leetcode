# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长递增子序列
# description:

class Solution:
    # 您的代码已保存
    # 运行超时: 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
    # case通过率为4.76 %

    # 以a[i]为最后一个元素的最长递增子序列
    def max_increase_sequence(self, arr, n):
        if not arr or n <= 0:
            return 0, -1

        dp = [1] * n
        # 需要找到每个元素对应的最长递增子序列
        paths = [[each] for each in arr]
        for i in range(n):
            for j in range(i):
                if arr[i] >= arr[j]:
                    if dp[j] + 1 > dp[i] or (dp[j] + 1 == dp[i] and arr[j] < paths[i][-2]):
                        dp[i] = dp[j] + 1
                        paths[i] = paths[j] + [arr[i]]

        # print(dp)
        # print(paths)
        return ' '.join(map(str, paths[dp.index(max(dp))]))


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = Solution().max_increase_sequence(arr, n)
    print(ans)

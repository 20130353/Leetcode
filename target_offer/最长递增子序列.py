# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长递增子序列
# description:

'''

    解法: 动规方程: dp[i] = max(dp[j]) + 1

'''


class Solution:

    def max_increase_sequence(self, data):

        if not data:
            return 0

        dp = [1 for _ in range(len(data))]
        for i in range(len(data)):
            for j in range(0, i): # 这里可以搜索整个dp数组,也可以搜索之前的i个元素,因为在整个数组中比i元素小的元素个数只能有i个.所以就搜索i之前的元素就可以了
                if data[i] > data[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    data = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    # data = []
    # data = [2]
    # data = [1,4,3,2,6,5]
    # data = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(Solution().max_increase_sequence(data))

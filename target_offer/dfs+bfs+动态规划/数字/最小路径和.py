# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最小路径和
# description:

'''
    给定一个矩阵，吗矩阵只能从左上角沿右边或者下边的方向走，求到右下角的最小路径是多少？

    两种思路：
    １．　暴力搜索
    ２．　动规

'''


# # 第一种方法：DFS+BFS
# class Solution:
#
#     def min_path(self, i, j, max_i, max_j, map, cur_sum, res):
#
#         if i == max_i and j == max_j:
#             res[0] = min(cur_sum, res[0])
#             return
#
#         if i + 1 <= max_i:
#             self.min_path(i + 1, j, max_i, max_j, map, cur_sum + map[i + 1][j], res)
#
#         if j + 1 <= max_j:
#             self.min_path(i, j + 1, max_i, max_j, map, cur_sum + map[i][j + 1], res)
#
#         return
#
#     def min_path_main(self, data):
#
#         # 只有一行
#         if type(data[0]).__name__ != 'list':
#             return sum(data)
#         else:
#             ans = [0xffffffff]
#             self.min_path(0, 0, len(data) - 1, len(data[0]) - 1, data, data[0][0], ans)
#
#         return ans


# 第二种方法：动规
class Solution:

    def min_path_main(self, data):

        # 只有一行
        if type(data[0]).__name__ != 'list':
            return sum(data)

        else:
            m, n = len(data), len(data[0])

            ans = [[0xffffffff for _ in range(n)] for _ in range(m)]

            # 初始化第一行
            for j in range(n):
                if j == 0:
                    ans[0][0] = data[0][0]
                else:
                    ans[0][j] = ans[0][j - 1] + data[0][j]

            # 初始化第一列(去除第一行的第一个)
            for i in range(1, m):
                ans[i][0] = ans[i - 1][0] + data[i][0]

            # 计算ans矩阵
            for i in range(1, m):
                for j in range(1, n):
                    ans[i][j] = min(ans[i - 1][j] + data[i][j], ans[i][j - 1] + data[i][j])

            return ans[m - 1][n - 1]


if __name__ == '__main__':
    data = [[1, 2, 3], [1, 1, 1]]  # ans:4
    data = [1]  # and:1

    print(Solution().min_path_main(data))

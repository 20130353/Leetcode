# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-2
# file: 最长递增子序列
# description:

# class Solution:
#     # 您的代码已保存
#     # 运行超时: 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
#     # case通过率为4.76 %
#     # 时间复杂度是nlogn --> 用二分
#     # 以a[i]为最后一个元素的最长递增子序列
#     def max_increase_sequence(self, arr, n):
#         if not arr or n <= 0:
#             return 0, -1
#
#         dp = [1] * n
#         # 需要找到每个元素对应的最长递增子序列
#         paths = [[each] for each in arr]
#         for i in range(n):
#             for j in range(i - 1):
#                 if arr[i] >= arr[j]:
#                     if dp[j] + 1 > dp[i] or (dp[j] + 1 == dp[i] and arr[j] < paths[i][-2]):
#                         dp[i] = dp[j] + 1
#                         paths[i] = paths[j] + [arr[i]]
#
#         # print(dp)
#         # print(paths)
#         return ' '.join(map(str, paths[dp.index(max(dp))]))

# 这道题的精华在于保存tail数组，保存长度为i的最后一个数字，这个数组是递增数组，可以用二分查找！
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为4.76%

# 存在的问题：找不到错误的case！
class Solution:
    def binear_search(self, arr, target, n):
        # 返回位置
        low, high = 0, n - 1
        while low < high:
            mid = low + (high - low + 1) // 2
            if arr[mid] <= target:
                low = mid
            else:
                high = mid - 1
        if arr[low] <= target:
            return low, arr[low]
        else:
            return -1, -1

    def max_increase_sequence(self, arr, n):
        tail = [-1] * (n + 1)  # tail[i]表示长度为i的序列的最后一个字符
        dp = [1] * n  # dp[i]表示以a[i]为最后一个字符的最长递增子序列长度
        tail[1] = min(arr)
        paths = {min(arr): [min(arr)]}
        max_increse_leng = 1
        for i in range(arr.index(min(arr)) + 1, n):
            max_leng, max_num = self.binear_search(tail, arr[i], max_increse_leng + 1)
            if max_leng != -1:
                dp[i] = max_leng + 1
                paths[arr[i]] = paths[max_num] + [arr[i]]
                if arr[i] < tail[dp[i]] or tail[dp[i]] == -1:
                    tail[dp[i]] = arr[i]
                max_increse_leng = max(max_increse_leng, dp[i])
        # return max(dp), paths[tail[max_increse_leng]]
        return ' '.join(map(str, paths[tail[max_increse_leng]]))


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = Solution().max_increase_sequence(arr, n)
    print(ans)

# 10
# 4 0 3 2 9 10 8 7 1 5
# --》0 2 9 10

# 10
# 1 2 3 4 5 6 7 8 9 10
# --》1 2 3 4 5 6 7 8 9 10


# 10
# 1 11 7 6 8 12 9 13 10 5
# --》1 6 8 9 10

# 14
# 0 32 10 21 20 15 30 9 6 40 4 50 1 60


# 10
# 10 1 4 9 12 0 2 3 4 3
# 0 2 3 3

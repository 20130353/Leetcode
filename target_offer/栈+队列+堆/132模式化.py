# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 132模式化.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

#
# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。
# 设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

# 解决思路：
# 1. 滑动窗口
# 2. 单调栈,存在的问题是忽略aj>ai;忽略找到去掉的最小的元素;超时！
#
# class Solution:
#     def find132pattern(self, arr):
#         if not arr or len(arr) <= 2:
#             return False
#         stack = []
#         for i in range(len(arr)):
#             flag = 0
#             min_value = 0xfffffff
#             while stack and arr[stack[-1][0]] <= arr[i]:
#                 num = stack.pop()
#                 if num[1] == 1 and min_value > num[2]:
#                     min_value = num[2]
#                 elif num[1] == 0 and min_value > arr[num[0]]:
#                     min_value = arr[num[0]]
#                 else:
#                     pass
#                 flag = 1
#             if stack:
#                 for each in stack:
#                     if each[1] == 1 and each[2] < arr[i]:
#                         return True
#             stack.append((i, flag, min_value))
#         if stack:
#             for i in range(len(stack) - 1):
#                 if stack[i][1] == 1 and stack[i][2] < arr[stack[-1][0]]:
#                     return True
#         return False


# 主要思想是：从左到右遍历一遍找到到当前元素最小的，然后当前元素作为最大值，找到右边任何一个比最小元素大的元素就证明存在。
# 从右边开始是一个不断递增的数列，最后找到的元素确定是比当前元素小！
# class Solution:
#     def find132pattern(self, nums):
#         le = len(nums)
#         if le < 2: return False
#
#         mi = [nums[0]]
#         for i in range(1, le):
#             mi.append(min(nums[i], mi[-1]))
#
#         stack = []
#         # 遍历的值是中间值
#         for i in range(le - 1, -1, -1):
#             # 如果当前值大于最小值，只有找到中间值或者是右边的值就可以！
#             if nums[i] > mi[i]:
#                 # 找到第一个大于最小值的值
#                 while stack and mi[i] >= stack[-1]:
#                     stack.pop()
#
#                 # 如果大于最小值的值小于当前值，那么当前值就是最大的值，那么最小值和右边的值也就确定了
#                 if stack and stack[-1] < nums[i]:
#                     return True
#
#                 # 为什么放num，如果不放num会错过可行解！
#                 # 栈内元素都是大于nums[i]的，直接把nums[i],推进栈，不影响递减。
#                 stack.append(nums[i])
#         return False

# 只能解决89/95的case
class Solution:
    def find132pattern(self, arr):
        if not arr or len(arr) <= 2: return False

        left, right = 0, 0
        win = []
        while right < len(arr):
            win.append(arr[right])
            while left < right and win[0] > win[-1]:
                left += 1
                win.pop(0)
            if win[0] < win[-1] and len(win[1:-1]) >= 1:
                max_value = max(win[1:-1])
                if max_value > win[0] and max_value > win[-1]: return True
            right += 1
        return False


if __name__ == '__main__':
    arr = [3, 5, 0, 3, 4]
    print(Solution().find132pattern(arr))

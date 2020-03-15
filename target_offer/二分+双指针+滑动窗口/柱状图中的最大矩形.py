#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 柱状图中的最大矩形.py
# @Author: smx
# @Date  : 2020/2/12
# @Desc  :

# # 第一种解法：双指针
# # 存在的问题是：如果最大面积和中间不连接，这样找不到
# class Solution:
#     def largestRectangleArea(self, arr):
#         if not arr:
#             return 0
#
#         if len(arr) == 1:
#             return arr[0]
#
#         left, right = len(arr) // 2, len(arr) // 2
#         max_area = max(arr)
#         min_value = arr[left]
#         while left >= 0 and right < len(arr):
#             area = (right - left + 1) * min_value
#             if area > max_area: max_area = area
#             if arr[left] > arr[right]:
#                 left -= 1
#                 if left >= 0 and arr[left] < min_value: min_value = arr[left]
#             else:
#                 right += 1
#                 if right < len(arr) and arr[right] < min_value: min_value = arr[right]
#         if left > 0:
#             while left >= 0:
#                 if arr[left] < min_value: min_value = arr[left]
#                 area = (right - left) * min_value
#                 if area > max_area: max_area = area
#                 left -= 1
#         if right > len(arr):
#             while right < len(arr):
#                 if arr[right] < min_value: min_value = arr[right]
#                 area = (right + 1) * min_value
#                 if area > max_area: max_area = area
#                 right += 1
#         return max_area


# 第一种解法：两个单调栈
# 存在的问题是：用了两个单调栈，其实用一个单调栈，退出的时候就可以找到右边最小的位置！
class Solution:
    def largestRectangleArea(self, arr):
        if not arr:
            return 0

        if len(arr) == 1:
            return arr[0]

        left_stack = []  # 当前元素的左边第一个比它小的元素
        left_arr = []
        for inx, each in enumerate(arr):
            while left_stack and arr[left_stack[-1]] >= each:
                left_stack.pop()
            if left_stack:
                left_arr.append(left_stack[-1])
            else:
                left_arr.append(-1)
            left_stack.append(inx)

        right_stack = []  # 当前元素的左边第一个比它小的元素
        right_arr = []
        for i in range(len(arr) - 1, -1, -1):
            while right_stack and arr[right_stack[-1]] >= arr[i]:
                right_stack.pop()
            if right_stack:
                right_arr.append(right_stack[-1])
            else:
                right_arr.append(len(arr))
            right_stack.append(i)

        right_arr = right_arr[::-1]
        max_area = max(arr)
        for i in range(len(arr)):
            area = (right_arr[i] - left_arr[i] - 1) * arr[i]
            # print('right_arr[i] {}, left_arr[i] {}, area {}'.format(right_arr[i], left_arr[i], area))
            if area > max_area: max_area = area
        return max_area


# 抓住一个点，就是遇到小值才出栈，计算面积
# 两种代码书写方式：1. 入栈之前将所有大于的元素出栈 2.要么入栈要不出栈
# class Solution(object):
#     def largestRectangleArea(self, height):
#         """
#         # 别人的代码
#         :type height: List[int]
#         :rtype: int
#         """
#         if height == None:
#             return 0
#         stack = []  # 单调递增栈
#         height.append(-1)
#         ans = 0
#         for i in range(len(height)):
#             cur = height[i]
#             # 如果栈为空或者当前柱比栈顶柱要高，入栈
#             if len(stack) == 0 or cur >= height[stack[-1]]:
#                 stack.append(i)
#             else:
#                 # 当前值比栈内元素小，就出栈计算面积
#                 while len(stack) != 0 and cur <= height[stack[-1]]:
#                     h = height[stack.pop()]
#                     left = stack[-1] if len(stack) != 0 else -1
#                     ans = max(ans, h * (i - left - 1))
#                 stack.append(i)
#         return ans

# 这段代码写的非常漂亮！
class Solution(object):
    def largestRectangleArea(self, arr):
        if arr == None:
            return 0
        stack = []  # 单调递增栈
        arr.append(-1)
        ans = 0
        arr.append(-1) # 用最后加一个元素的方式避免倒出来所有的元素！
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                h = arr[stack.pop()]
                left = stack[-1] if stack else -1
                ans = max((i - left - 1) * h, ans)
            stack.append(i)
        return ans


if __name__ == '__main__':
    arr = [4, 1]
    print(Solution().largestRectangleArea(arr))

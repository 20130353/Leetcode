#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 颜色分类.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
# 使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 主要思想是遇到0就和[1,2]位置的最小值交换，遇到1就和2位置交换，最后的确保1和2的位置正确
# 需要注意的是：到1交换时，必须考虑A的位置，可能会因为之前交换，导致A的位置在后面，所以就交换错了。
# class Solution:
#     def sortColors(self, nums):
#         if len(nums) <= 1:
#             return
#
#         # A:3的第一个位置；B:2的第一个位置；C:循环遍历
#         A, B, C = 0, 0, 0
#         while A < len(nums) and nums[A] != 2:
#             A += 1
#         while B < len(nums) and nums[B] != 1:
#             B += 1
#
#         C = min(A, B) + 1
#         while C < len(nums):
#             if nums[C] == 0:
#                 if A < B:
#                     nums[A], nums[C] = nums[C], nums[A]
#                     while A < len(nums) and nums[A] != 2:
#                         A += 1
#                 else:
#                     nums[B], nums[C] = nums[C], nums[B]
#                     while B < len(nums) and nums[B] != 1:
#                         B += 1
#             elif nums[C] == 1:
#                 if C > A:
#                     nums[A], nums[C] = nums[C], nums[A]
#                     if A < B: B = A
#                     while A < len(nums) and nums[A] != 2:
#                         A += 1
#             C += 1
#         C = A + 1
#         while C < len(nums):
#             if nums[C] == 1:
#                 nums[A], nums[C] = nums[C], nums[A]
#                 while A < len(nums) and nums[A] != 2:
#                     A += 1
#             C += 1
#         return

class Solution:
    def sortColors(self, nums):
        if len(nums) <= 1:
            return
        # A:0的最右边，B:2的最左边 C:遍历指针
        A, B, C = 0, len(nums) - 1, 0
        while C <= B:
            if nums[C] == 0:
                nums[A], nums[C] = nums[C], nums[A]
                A += 1
                C += 1
            elif nums[C] == 2:
                nums[B], nums[C] = nums[C], nums[B]
                B -= 1
            else:
                C += 1


if __name__ == '__main__':
    arr = [1, 0, 1, 0, 1, 0, 2]
    num = Solution().sortColors(arr)
    print(arr)

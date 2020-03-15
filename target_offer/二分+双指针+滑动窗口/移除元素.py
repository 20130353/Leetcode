#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 移除元素.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0

        # A:给定值的第一个位置
        # B:遍历数组的元素
        A = 0
        while A < len(nums) and nums[A] != val:
            A += 1
        B = A + 1
        while B < len(nums):
            if nums[B] != val:
                nums[A], nums[B] = nums[B], nums[A]
                A = 0
                while A < len(nums) and nums[A] != val:
                    A += 1
            B += 1
        return A


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 4, 5, 5, 5]
    num = Solution().removeElement(arr, 5)
    print(arr)
    print(num)

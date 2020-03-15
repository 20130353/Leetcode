#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 移动0.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

class Solution:
    def moveZeroes(self, nums):
        if not nums or len(nums) <= 1:
            return
        A = 0
        while A < len(nums) and nums[A] != 0:
            A += 1
        B = A + 1
        while B < len(nums):
            if nums[B] == 0:
                B += 1
            else:
                save = nums[B]
                nums[B] = nums[A]
                nums[A] = save
                A += 1
                B += 1


if __name__ == '__main__':
    arr = [1, 2, 0, 3, 0, 0]
    Solution().moveZeroes(arr)
    print(arr)

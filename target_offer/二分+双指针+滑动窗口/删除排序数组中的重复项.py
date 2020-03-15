#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 删除排序数组中的重复项.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :
# 删除重复元素，保留一个

class Solution:
    def removeDuplicates(self, nums):
        if not nums or len(nums) <= 1:
            return

        # A:不重复元素可以放的位置
        # B:遍历数组的元素
        A, B = 1, 1
        while B < len(nums):
            if nums[A - 1] == nums[B]:
                B += 1
            else:
                nums[A], nums[B] = nums[B], nums[A]
                A += 1
                B += 1
        return A


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 4, 5, 5, 5]
    num = Solution().removeDuplicates(arr)
    print(arr)
    print(num)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 删除排序数组中的重复项--升级版.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

class Solution:
    # 返回长度
    def removeDuplicates(self, nums):
        if not nums or len(nums) <= 2:
            return len(nums)
        A, B = 2, 2
        while B < len(nums):
            if (nums[A - 1] == nums[B]) and (nums[A - 2] == nums[A - 1]):
                B += 1
            else:
                nums[A], nums[B] = nums[B], nums[A]
                A += 1
                B += 1
        return A


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 2, 3]
    num = Solution().removeDuplicates(arr)
    print(arr)
    print(num)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 区间和检索-不改变数组.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :

class NumArray:

    def __init__(self, nums):
        self.arr = []
        self.nums = nums
        ans = 0
        for i in range(len(nums)):
            ans += nums[i]
            self.arr.append(ans)

    def sumRange(self, i, j):
        if i == j:
            return self.nums[i]
        elif i == 0:
            return self.arr[j]
        else:
            return self.arr[j] - self.arr[i - 1]


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    print(NumArray(nums).sumRange(2, 2))

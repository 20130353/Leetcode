#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最大子数组的和--数字.py
# @Author: smx
# @Date  : 2019/8/28
# @Desc  :


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0] for i in range(len(nums))]
        max_result = nums[0]  # 最开始的是nums[0]，后面如果是负数肯定更小，如果是整数肯定变大
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
            if max_result < dp[i]:
                max_result = dp[i]
        return max_result

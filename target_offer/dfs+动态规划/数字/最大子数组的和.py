#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最大子数组的和.py
# @Author: smx
# @Date  : 2019/8/28
# @Desc  :

class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        # 以a[i]位置为子数组的最后一个元素的最大和
        # 这里无法用双指针，为什么？
        # 虽然这里也是区间的题目，但是没有缩和开区间的可能性（有可能性就是指连续正整数），所以无法用
        dp = [each for each in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], dp[i])
        return max(dp)


if __name__ == '__main__':
    # arr = [3, 2, 4, -1, 0, 3, 4, 5, 6]
    arr = list(map(int, input().strip().split(',')))
    ans = Solution().maxSubArray(arr)
    print(ans if ans >= 0 else 0)

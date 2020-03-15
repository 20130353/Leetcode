#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 区间和的个数.py
# @Author: smx
# @Date  : 2020/2/17
# @Desc  :


# 超时--> 用空间换时间
# 超时-> 将前缀树组变成有序，然后用二分查找，sum-upper<=x<=sum-lower
# 用python提供的只能只能返回插入元素的位置，有相同元素的时候很麻烦
import bisect


class Solution:
    def countRangeSum(self, nums, lower, upper):
        if not nums: return 0

        n = len(nums)
        sum_m = []
        ans = 0
        total_sum = 0
        for i in range(1, n + 1):
            total_sum += nums[i - 1]
            bisect.insort_left(sum_m, total_sum)
            # 在元素的左边插入，返回插入元素的位置
            left_inx = bisect.bisect_left(sum_m, total_sum - upper)
            while left_inx >= 0 and sum_m[left_inx] == total_sum - upper:
                left_inx -= 1
            right_inx = bisect.bisect_right(sum_m, total_sum - lower)
            while right_inx < len(sum_m) and sum_m[right_inx] == total_sum - lower:
                right_inx += 1
            ans += right_inx - left_inx
        return ans


if __name__ == '__main__':
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(Solution().countRangeSum(nums, lower, upper))

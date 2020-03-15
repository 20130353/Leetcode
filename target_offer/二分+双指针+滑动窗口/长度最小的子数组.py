#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 长度最小的子数组.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# 找到大于等于的最小子数组
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums or len(nums) <= 0 or sum(nums) < s:
            return 0
        left, right = 0, 0
        count = nums[left]
        length = len(nums)
        while right < len(nums) and left < len(nums):
            if count < s:
                if right + 1 < len(nums):
                    right += 1
                    count += nums[right]
                else:
                    break
            else:
                length = min(length, right - left + 1)
                count -= nums[left]
                left += 1
        return length


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    ans = Solution().minSubArrayLen(11, arr)
    print(ans)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 连续的子数组和为k的倍数.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :

import math


class Solution:
    def checkSubarraySum(self, nums, k):
        total_sum = 0
        sum_dict = {0: -1}
        for i in range(len(nums)):
            total_sum += nums[i]
            if total_sum not in sum_dict.keys():
                sum_dict[total_sum] = i
            for each in sum_dict.items():
                if k == 0 and (total_sum - each[0]) == 0 and i != each[1] and (i - each[1]) >= 2:
                    return True
                if k != 0 and (total_sum - each[0]) % k == 0 and i != each[1] and (i - each[1]) >= 2:
                    return True
        return False


if __name__ == '__main__':
    arr = [0, 0]
    k = 0
    print(Solution().checkSubarraySum(arr, k))

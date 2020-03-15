#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 和为s的连续整数数列.py
# @Author: smx
# @Date  : 2020/2/17
# @Desc  :

# 可以用数组或者map保存前缀和，然后用二分或者map直接查找
# 还有这种k的思想也是非常常用的思想！
class Solution:
    def subarraySum(self, nums, k):
        ans = 0
        if not nums:
            return ans
        dict = {0: 1} if k != 0 else {}  # 最容易出问题的地方！0????
        total_sum = 0
        for each in nums:
            total_sum += each
            if total_sum not in dict.keys():
                dict[total_sum] = 1
            else:
                dict[total_sum] += 1
            target = total_sum - k
            # 这里会重复加
            if target in dict.keys():
                ans += dict[target]
            # 减掉当前元素的一次
            if k == 0 and total_sum != 0:
                ans -= 1
        return ans


if __name__ == '__main__':
    nums = [1, 0, 1]
    k = 3
    print(Solution().subarraySum(nums, k))

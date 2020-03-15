#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数组拆分.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :

class Solution:
    def arrayPairSum(self, nums):
        snums = sorted(nums)
        asum = 0
        for i in range(len(snums)):
            if i % 2 == 0: asum += snums[i]
        return asum


if __name__ == '__main__':
    arrs = [1, 2, 3, 2]
    print(Solution().arrayPairSum(arrs))

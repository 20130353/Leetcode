#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 买卖股票的最佳时期.py
# @Author: smx
# @Date  : 2020/2/22
# @Desc  :

class Solution:
    def maxProfit(self, arrs):
        if not arrs: return 0
        min_v = arrs[0]
        max_ans = 0
        for i in range(len(arrs)):
            if arrs[i] < min_v: min_v = arrs[i]
            max_ans = max(max_ans, arrs[i] - min_v)
        return max_ans


if __name__ == '__main__':
    arrs = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(arrs))

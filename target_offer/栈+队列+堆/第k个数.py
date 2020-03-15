#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第k个数.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :

# 和丑数的思想是一样的！
# 如果是节约空间，可以将前面的部分弹出
class Solution:
    def getKthMagicNumber(self, k):
        arr = [1]
        inx3, inx5, inx7 = 0, 0, 0
        while len(arr) < k:
            next_value = min(arr[inx3] * 3, arr[inx5] * 5, arr[inx7] * 7)
            arr.append(next_value)
            while arr[inx3] * 3 <= next_value:
                inx3 += 1
            while arr[inx5] * 5 <= next_value:
                inx5 += 1
            while arr[inx7] * 7 <= next_value:
                inx7 += 1
        return arr[-1]


if __name__ == '__main__':
    k = 7
    print(Solution().getKthMagicNumber(k))

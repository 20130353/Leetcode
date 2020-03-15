#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 合并两个有序数组.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

class Solution:
    def merge(self, nums1, m, nums2, n):
        if not nums1:
            nums1 = nums2
            return
        if not nums2:
            return
        if nums1[m - 1] <= nums2[0]:
            nums1[m:] = nums2
            return

        A, B = 0, 0
        while A < m and B < n:
            if nums1[A] <= nums2[B]:
                A += 1
            else:
                for i in range(m, A, -1):
                    nums1[i] = nums1[i - 1]
                nums1[A] = nums2[B]
                B += 1
                m += 1
        if B < n:
            nums1[m:] = nums2[B:]
        return


if __name__ == '__main__':
    arr1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    arr2 = [1, 2, 2]

    Solution().merge(arr1, 6, arr2, len(arr2))
    print(arr1)

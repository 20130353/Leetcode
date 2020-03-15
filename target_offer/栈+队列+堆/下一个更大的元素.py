#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 下一个更大的元素.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :


# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
# 找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

# 单调递减的栈
class Solution:
    def nextGreaterElement(self, arr1, arr2):
        if not arr2 or not arr1:
            return [-1] * len(arr1)

        # 给arr构造单调递减的栈
        stack = [-1]
        map = {}
        for i in range(len(arr2) - 1, -1, -1):
            while stack[-1] != -1 and arr2[stack[-1]] <= arr2[i]:
                stack.pop()
            map[arr2[i]] = arr2[stack[-1]] if stack[-1] != -1 else -1
            stack.append(i)
        ans = [map[each] for each in arr1]
        return ans


if __name__ == '__main__':
    arr1 = [4, 1, 2]
    arr2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(arr1, arr2))

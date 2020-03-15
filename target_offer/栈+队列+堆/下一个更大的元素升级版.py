#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 下一个更大的元素升级版.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
# 数字--线性动规 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
# 如果不存在，则输出 -1。


# 思路：
# 找到左右两边第一个比它大的数
# 1. 用两个单调栈
# 2. 一个单调栈，记录入和出的第一个大的数字, 问题：得到的不是循环数组.
# 这回写的不错，循环的关键在于可以直接相加得到原来的数组
import copy


class Solution:
    def nextGreaterElements(self, arr):
        if not arr:
            return arr
        right = [-1 for _ in range(len(arr))]
        stack = [-1] + list(range(len(arr) - 1, -1, -1))  # 存放的单调递增的序号栈！
        for i in range(len(arr) - 1, -1, -1):
            while stack[-1] != -1 and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack[-1] != -1: right[i] = arr[stack[-1]]
            stack.append(i)
        return right


if __name__ == '__main__':
    arr = [5, 4, 3, 4, 2, 5, 1]
    print(Solution().nextGreaterElements(arr))

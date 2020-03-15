#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 双指针+滑动窗口.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :


# 连续正整数，特点是左边收缩一定会导致整体变小
def solution(arr, n, target):
    if sum(arr) < target or target <= 0:
        return -1

    if sum(arr) == target:
        return n

    left,win = 0,0
    max_length = -0xfffff
    # 核心是右边一直不断加入，左边是看情况收缩
    for right in range(n):
        win += arr[right]
        while left < right and win >= target:
            if win == target:
                max_length = max(max_length, right - left + 1)
            win -= arr[left]
            left += 1
    return max_length

# 和为s的连续序列
def solution(arr, n, target):
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1

    sum_map = {0: 0}
    win, max_leng = 0, -1
    for i in range(1, n + 1):
        win += arr[i - 1]
        if win not in sum_map.keys():
            sum_map[win] = i
        if (win - target) in sum_map and (i - sum_map[win - target]) > max_leng:
            max_leng = i - sum_map[win - target]
    return max_leng

# 盛水问题
class Solution:
    def maxArea(self, arr):
        if not arr or len(arr) <= 1:
            return 0

        left, right = 0, len(arr) - 1
        max_value = -0xffffff
        while left != right:
            max_value = max((right - left) * min(arr[left], arr[right]), max_value)
            if arr[left] <= arr[right]:
                left += 1
            else:
                right -= 1
        return max_value



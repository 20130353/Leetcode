#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 双指针+滑动窗口.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :


# 和为s的连续正整数，特点是左边收缩一定会导致整体变小
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

# 和为s的连续序列，需要多用一个map保存中间结果
# 这道题可以用双指针、map、如果是有序的可以用二分查找
# map为什么查找速度快：因为底层是散列表，每次找到只有通过哈希函数的key的位置是否元素即可
# list为什么查找慢：底层是线性表，只能遍历

def solution(arr, n, target):
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1

    # 本质是一维前缀和，和的第一个是0
    sum_map = {0: 0}
    cur_sum, max_leng = 0, -1
    for i in range(1, n + 1):
        cur_sum += arr[i - 1]
        if cur_sum not in sum_map.keys():
            sum_map[cur_sum] = i
        if (cur_sum - target) in sum_map and (i - sum_map[cur_sum - target]) > max_leng:
            max_leng = i - sum_map[cur_sum - target]
    return max_leng

# 盛水问题
class Solution:
    # 这个升水问题的重点是：只要两边高就可以保留着中间的水。
    # 本质是数组排列组合的问题，一定会涉及到两边边界变化，所以可以用双指针
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



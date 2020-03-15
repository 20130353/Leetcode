#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最大矩形.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

# 问题的关键在于如何将矩阵转换成柱状图
# 按照每一行进行转换，如果当前行的这一位是0，那么整体高度为0，如果这一位是1，加上前面高度

class Solution:
    def maxRect(self, arr):
        if arr == None:
            return 0

        stack = []  # 单调递增栈
        arr.append(-1)
        ans = 0
        arr.append(-1)  # 用最后加一个元素的方式避免倒出来所有的元素！
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                h = arr[stack.pop()]
                left = stack[-1] if stack else -1
                ans = max((i - left - 1) * h, ans)
            stack.append(i)
        return ans

    def maximalRectangle(self, matrix):
        if not matrix or len(matrix) <= 0:
            return 0

        arr = matrix[0]
        arr = [int(each) for each in arr]
        ans = self.maxRect(arr)

        if len(matrix) == 1:
            return ans
        for i in range(1, len(matrix)):
            new_arr = matrix[i]
            new_arr = [int(each) for each in new_arr]
            for j in range(len(new_arr)):
                if new_arr[j] == 1:
                    new_arr[j] += arr[j]
            ans = max(ans, self.maxRect(new_arr))
            arr = new_arr
        return ans


if __name__ == '__main__':
    arr = [['0']]
    print(Solution().maximalRectangle(arr))

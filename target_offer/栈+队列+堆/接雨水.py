#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 接雨水.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :

class Solution:
    def trap(self, arr):
        if not arr:
            return
        stack = []
        ans = 0
        for inx, each in enumerate(arr):
            if each == 0 and len(stack) == 0:
                continue
            else:
                values = []
                # 这里太笨！应该直接计算雨水面积！而且计算水的面积出错了！
                while stack and stack[-1] <= each:
                    values.insert(0, stack.pop())
                if len(values) > 1:
                    if stack and stack[-1] >= each:
                        base = each
                    else:
                        base = min(values[0], each)
                    temp_ans = len(values) * base
                    for h in values:
                        temp_ans -= h
                    ans += temp_ans
                stack.append(each)
        return ans

# 单调栈
class Solution:
    def trap(self, height):
        len_h = len(height)
        if len_h < 3:
            return 0
        stack, res = list(), 0
        for i in range(len_h):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                # 左面必须有墙才能接水
                if stack:
                    base = min(height[i], height[stack[-1]]) #左边还有墙
                    # height * width, //两边的最低高度（水高） - 自身高度（容器厚度）
                    res += (base - height[tmp]) * (i - stack[-1] - 1)
            stack.append(i)
        return res


if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(arr))

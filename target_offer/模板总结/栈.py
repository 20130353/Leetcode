#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 栈.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :


# 单调栈和双指针的区别就是弹出东西不一样:
# 单调栈弹出后进的元素
# 双指针弹出首先进的元素

# 字符串的解压缩
# 题目的意思是(ab)3bb4变成abababbbbbb，表示将数字之前的字母组合变成原来的样子
# 时间复杂度：单次是n*次数n=O(n^2)
# 空间复杂度：O(n)
def solution(string):
    if not string or len(string) <= 0:
        return ''
    i = 0
    # 一般字符串需要注意的是数字要保证多个字母组成一个数字的情况
    stack = []
    while i < len(string):
        if string[i].isdigit():
            j = i + 1
            while j < len(string) and string[j].isdigit():
                j += 1
            num = int(string[i:j])
            i = j
            if stack[-1] == ')':
                stack.pop()
                key = ''
                while stack[-1] != '(':
                    key = stack.pop() + key
                stack.pop()
            else:
                key = stack.pop()
            res = ''
            for _ in range(num):
                res += key
            stack = stack + list(res)
        else:
            stack.append(string[i])
            i += 1
    return stack

# 接雨水
# 时间复杂度：单次n*次数n=O(n^2)
# 空间复杂度：O(n)
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

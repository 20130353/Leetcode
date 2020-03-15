#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 无重复字符的最长子串.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s or len(s) <= 1:
            return len(s)

        dict = {}
        arr = []
        for inx, each in enumerate(s):
            if each not in dict.keys():
                arr.append(-1)
                dict[each] = inx
            else:
                arr.append(dict[each])
                dict[each] = inx
        A, B = 0, 0
        count = -0xffffff
        while A < len(s) - 1 and B < len(s) - 1:
            B += 1
            if arr[B] >= A:
                A = arr[B] + 1
            count = max(count, B - A + 1)
        return count


if __name__ == '__main__':
    string = 'pwwkew'
    print(Solution().lengthOfLongestSubstring(string))

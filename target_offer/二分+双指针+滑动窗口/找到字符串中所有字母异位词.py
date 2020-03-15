#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 找到字符串中所有字母异位词.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :

# 超时！
from collections import Counter


class Solution:
    def findAnagrams(self, s, t):
        if not s or len(s) <= 0 or len(t) <= 0:
            return []

        dict_t = Counter(t)
        dict_w = {}
        match = {}
        windows = ''
        left, right = 0, 0
        ans = []
        for right in range(len):
            windows += s[right]
            if s[right] in dict_w:
                dict_w[s[right]] += 1
            else:
                dict_w[s[right]] = 1
            if s[right] in t and dict_w[s[right]] >= dict_t[s[right]]:
                match[s[right]] = 1
            while sum(match.values()) == len(dict_t):
                if len(windows) == len(t):
                    ans.append(left)
                left += 1
                remove_char = windows[0]
                windows = windows[1:]
                dict_w[remove_char] -= 1
                if remove_char in t and dict_w[remove_char] < dict_t[remove_char]:
                    match[remove_char] = 0
        return ans


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))

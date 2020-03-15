#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最小覆盖子串.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :

# 两种解法：
# 1. 用map记录每个元素出现的最新位置，计算map所有元素的差距的最小值
# 2. 用滑动窗口
# 关键问题是用两个map记录出现的次数
# 对于覆盖问题，不要求位置可以直接数数量

# 第一种解法
# 存在的问题：如果用map确定是否所有元素都被包含，那么重复元素就会被忽略！
# class Solution:
#     def minWindow(self, s, t):
#         if not s or not t:
#             return 0
#
#         dict = {}
#         for each in t:
#             dict[each] = 0xfffff
#
#         min_value = 0xffffff
#         min_pos = None
#         for inx, each in enumerate(s):
#             if each in t:
#                 dict[each] = inx
#                 maxm, minm = max(dict.values()), min(dict.values())
#                 dis = maxm - minm
#                 pos = (minm, maxm)
#                 if dis < min_value:
#                     min_value = dis
#                     min_pos = pos
#         return s[min_pos[0]:min_pos[1] + 1]
#

# 第二种方法：
# 用窗口，但是还是需要用哈希表，解决的关键是用两个哈希表
# 可以用两个哈希表当作计数器解决。
# 用一个哈希表 needs 记录字符串 t 中包含的字符及出现次数，
# 用另一个哈希表 window 记录当前「窗口」中包含的字符及出现的次数，
# 如果 window 包含所有 needs 中的键，且这些键对应的值都大于等于 needs 中的值，那么就可以知道当前「窗口」符合要求了，
# 可以开始移动 left 指针了。

# 超时!
# 改成只比较去掉字母也超时！
# 改成一个总的window和总的计数
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ''

        min_length = 0xfffff
        min_value = ''
        dict_t = Counter(t)
        dict_w = {}
        left, right = 0, -1
        windows = ''
        match = {}
        while right < len(s) - 1:
            right += 1
            windows += s[right]
            if s[right] in dict_w.keys():
                dict_w[s[right]] += 1
            else:
                dict_w[s[right]] = 1
            if s[right] in t and dict_w[s[right]] >= dict_t[s[right]]:
                match[s[right]] = 1
            while sum(match.values()) == len(dict_t):
                if len(windows) < min_length:
                    min_length = len(windows)
                    min_value = windows
                left += 1
                remove_char = windows[0]
                windows = windows[1:]
                dict_w[remove_char] -= 1
                if remove_char in t and dict_w[remove_char] < dict_t[remove_char]:
                    match[remove_char] = 0
        return min_value


if __name__ == '__main__':
    S = "a"
    T = "aa"
    print(Solution().minWindow(S, T))

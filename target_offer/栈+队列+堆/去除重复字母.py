#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 去除重复字母.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

from collections import Counter
import copy
class Solution:
    def removeDuplicateLetters(self, string):
        if not string or len(string) <= 1:
            return string
        arr = list(string)
        count = Counter(arr)
        stack = []
        arr += 'a'
        ans = copy.deepcopy(arr)
        for i in range(len(arr)):
            print('----------------')
            print(arr)
            print(stack)
            while stack and arr[stack[-1]] >= arr[i]:
                inx = stack.pop()
                if count[arr[inx]] != 1:
                    ans[inx] = '#'
                    count[arr[inx]] -= 1
            stack.append(i)
        return ''.join(ans[:-1]).replace('#', '')


if __name__ == '__main__':
    string = "cbacdcbc"
    print(Solution().removeDuplicateLetters(string))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 查找和替换.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :

class Solution:
    def check(self, A, B):
        if len(A) != len(B) or len(set(A)) != len(set(B)):
            return False
        for i in range(len(A)):
            if A.index(A[i]) != B.index(B[i]):
                return False
        return True

    def findAndReplacePattern(self, words, pattern):
        ans = []
        for each in words:
            if self.check(each, pattern):
                ans.append(each)
        return ans


if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(Solution().findAndReplacePattern(words, pattern))

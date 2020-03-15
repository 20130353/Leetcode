#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 累加数.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :


class Solution:
    def isAdditiveNumber(self, string):
        if not string or len(string) < 3:
            return False
        if len(string) == 3:
            return int(string[0]) + int(string[1]) == int(string[2])
        n = len(string)
        for left in range(1, n - 2):
            for right in range(left + 1, n - 1):
                A = string[:left]
                B = string[left:right]
                if A[0] == '0' and len(A) > 1: continue
                if B[0] == '0' and len(B) > 1: continue
                new_string = string[right:]
                while new_string:
                    C = str(int(A) + int(B))
                    if new_string[:len(C)] != C:
                        break
                    new_string = new_string[len(C):]
                    A, B = B, C
                if len(new_string) <= 0: return True
        return False


if __name__ == '__main__':
    string = "00011"
    print(Solution().isAdditiveNumber(string))

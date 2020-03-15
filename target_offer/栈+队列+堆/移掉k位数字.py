#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 移掉k位数字.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

import copy


class Solution:
    def removeKdigits(self, num, k):
        if not num or k >= len(num):
            return '0'
        if k <= 0:
            return num

        stack = []
        num += '0'
        ans = copy.deepcopy(num)
        for i in range(len(num)):
            while stack and stack[-1] > int(num[i]):
                inx = ans.index(str(stack.pop()))
                ans = ans[:inx] + ans[inx + 1:]
                if len(ans) == len(num) - k:
                    return ans[:-1].lstrip('0') if ans[:-1].lstrip('0') else '0'
            stack.append(int(num[i]))


if __name__ == '__main__':
    num, k = '1129', 1
    print(Solution().removeKdigits(num, k))

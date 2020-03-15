#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 棒球的得分.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :


class Solution:
    def calPoints(self, arr):
        if not arr or len(arr) <= 0:
            return 0

        score = 0
        stack = []
        for each in arr:
            if each.lstrip('-').isdigit():
                cur_score = int(each)
            elif each == 'C':
                drop = stack.pop()
                cur_score = -drop
            elif each == 'D':
                cur_score = stack[-1] * 2
            else:
                cur_score = stack[-1] + stack[-2]
            if each != 'C': stack.append(cur_score)
            score += cur_score
        return score


if __name__ == '__main__':
    string = ["5",'C']
    print(Solution().calPoints(string))

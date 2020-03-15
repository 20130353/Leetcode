#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 验证二叉树的前序遍历.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

class Solution:
    def isValidSerialization(self, string):
        num = 1  # 表示还可以出现的#的个数
        arr = string.split(',')
        for each in arr:
            if num == 0: return False
            if each == '#':
                num -= 1
            else:
                num += 1
        return True if num == 0 else False


if __name__ == '__main__':
    string = "1,#,#,1"
    print(Solution().isValidSerialization(string))

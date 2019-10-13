#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串分割为字符.py
# @Author: smx
# @Date  : 2019/10/13
# @Desc  :

# 给定的字符:串和字符数组，看字符数组能否拼接成字符串
# 思考的方式:
# 假设只有一个元素，判断元素和字符串是否相等
# 多加一个元素，有两个元素，选择拼起来和字符串是否相等 or 字符串删除一个字符，是否能和另一个字符相等
# 这里可以用KMP提前找好相等的字符，之后按照相等的字符去找，如果没有相等的字符且字符串没有被相等（分割完），就判定不相等！

# 1.dp[i]表示从0到第i个字符是否可以用字符串拼接得到。这种方法只能适合数组元素可以多次使用。
# 2.对于复杂版，需要构建一个每个位置匹配的字符串数组标记，如果某个字符被使用到了，需要将所有之后关于这个字符的记录全部删除

# 字符串数组元素可以用多次(简单版)
# 字符串数组中的元素只能用一次（进阶版）


class KMP:
    def get_next(self, pattern):
        next = [-1, 0]
        i, leng = 2, 0
        while i < pattern.__len__():
            if pattern[i] == pattern[leng]:
                leng += 1
                next[i] = leng
                i += 1
            elif leng > 0:
                leng = next[leng]
            else:
                next[i] = 0
                i += 1
        return next

    def match(self, string, pattern):
        next = self.get_next(pattern)
        i, j = 0, 0
        pos = []
        while i < len(string):
            if string[i] == pattern[j] or j == -1:
                i += 1
                j += 1
                if j == len(pattern):
                    pos.append(i - j + 1)
                    i += 1
                    j = 0
            else:
                j = next[j]
        return pos


#
# def judge(string, pos, flag, arr):
#     if len(string) <= 0 and pos == 0:
#         return
#
#     if flag[0]:
#         return
#
#     if pos >= len(string):
#         flag[0] = True
#         return
#
#     for i in range(len(arr)):
#         if arr[i] == string[pos:pos + len(arr[i])]:
#             judge(string, pos + len(arr[i]), flag, arr)

def solution(strings, target):
    pos = [[] * len(target)]
    kmp = KMP()
    for inx, each in enumerate(strings):
        p = kmp.match(target, each)
        for i in range(len(p)):
            pos[p[i]].append(inx)

    dp = [0] * len(target)
    for i in pos[0]:
        dp[i] = 1

    for i in range(len(target)):
        for j in pos[i]:
            dp[i] = dp[i] or dp[i - pos[i][j]]
    return dp[len(target) - 1]


if __name__ == '__main__':
    string = '12345'
    arr = ['1', '2', '3', '4', '5']

    string = '12345'
    arr = ['123', '45']

    string = ''
    arr = ['123', '45']

    string = '89087'
    arr = ['123', '45']

    flag = [False]
    judge(string, 0, flag, arr)
    print(flag)

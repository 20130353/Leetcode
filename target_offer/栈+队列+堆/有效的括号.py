#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 有效的括号.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# 这样做可以保证所有的括号成双成对的，但是不能保证右括号前面的括号是左括号，所以需要改成栈的形式
class Solution:
    # def isValid(self, s):
    #     map1 = {')': 0, '}': 1, ']': 2}
    #     map2 = {'(': 0, '{': 1, '[': 2}
    #     count = [0 for i in range(3)]
    #     total_search = '(){}[]'
    #     for each in s:
    #         if each not in total_search:
    #             return False
    #         if each in map1.keys():
    #             if count[map1[each]] > 0:
    #                 count[map1[each]] -= 1
    #             else:
    #                 return False
    #         else:
    #             count[map2[each]] += 1
    #     if sum(count) > 0: return False
    #     return True

    def isValid(self, s):
        if not s or len(s) < 1:
            return True

        map = {')': '(', '}': '{', ']': '['}
        total_search = '(){}[]'
        stack = []
        for each in s:
            if each not in total_search:
                return False
            if each in map.keys():
                if stack and stack[-1] == map[each]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(each)
        if len(stack) > 0: return False
        return True


if __name__ == '__main__':
    string = '{()[]}'
    print(Solution().isValid(string))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 电话号码的组合.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

class Solution:
    def DFS(self, digits, n, digits_dict, cur_pos, cur, ans):
        if cur_pos >= n:
            if cur: ans.append(''.join(cur))
            return

        if digits_dict[digits[cur_pos]]:
            for each in digits_dict[digits[cur_pos]]:
                cur.append(each)
                self.DFS(digits, n, digits_dict, cur_pos + 1, cur, ans)
                cur.pop()
        else:
            self.DFS(digits, n, digits_dict, cur_pos + 1, cur, ans)

    def letterCombinations(self, digits):
        ans = []
        digits_dict = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                       '9': 'wxyz'}
        self.DFS(digits, digits.__len__(), digits_dict, 0, [], ans)
        return ans


if __name__ == '__main__':
    string = '1'
    print(Solution().letterCombinations(string))

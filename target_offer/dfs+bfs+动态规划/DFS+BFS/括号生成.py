#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 括号生成.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 生成n对合法括号
class Solution:
    def DFS(self, n, cur_left, cur_right, char_num, cur, ans):
        if char_num == n * 2:
            ans.append(cur)
            return
        if 0 <= cur_left < n:
            self.DFS(n, cur_left + 1, cur_right, char_num + 1, cur + '(', ans)

        if 0 <= cur_right < n and cur_left > cur_right:
            self.DFS(n, cur_left, cur_right + 1, char_num + 1, cur + ')', ans)

    def generateParenthesis(self, n):
        ans = []
        self.DFS(n, 0, 0, 0, '', ans)
        return ans


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))

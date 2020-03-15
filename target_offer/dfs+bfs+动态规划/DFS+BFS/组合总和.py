#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 组合.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

class Solution:
    # 被无限抓取使用！
    def DFS(self, arrs, n, target, cur, cur_sum, ans):
        if cur_sum == target:
            if sorted(cur) not in ans:
                ans.append(sorted(cur))
            return

        for each in arrs:
            if cur_sum + each <= target:
                cur.append(each)
                self.DFS(arrs, n, target, cur, cur_sum + each, ans)
                cur.pop()

    def combinationSum(self, arrs, target):
        ans = []
        self.DFS(arrs, len(arrs), target, [], 0, ans)
        return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))

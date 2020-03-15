#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 递增子数列.py
# @Author: smx
# @Date  : 2020/2/18
# @Desc  :


# 不需要动态规划+回溯！ 只需要提前加入即可！
# 重复元素！
# 额外的知识点：set是红黑树，map是哈希之后的红黑树，list是数组连续空间
# 查询效率是set>map>list
# 所以频繁查询是set
# class Solution:
#     def DFS(self, arrs, i, cur, ans):
#         if len(cur) >= 2 and cur not in ans:
#             ans.append(cur)
#
#         if i >= len(arrs):
#             return
#
#
#         # 我这里也相当于是入栈和出栈，但是我用复制的方式，多开了许多空间！
#         if not cur or arrs[i] >= cur[-1]:
#             self.DFS(arrs, i + 1, cp.deepcopy(cur) + [arrs[i]], ans)
#
#         self.DFS(arrs, i + 1, cp.deepcopy(cur), ans)
#
#     def findSubsequences(self, arrs):
#         ans = []
#         self.DFS(arrs, 0, [], ans)
#         return sorted(ans)

import copy as cp


class Solution:

    def DFS(self, arrs, start, cur, ans):
        if len(cur) >= 2:
            ans.append(cp.copy(cur))

        if start >= len(arrs):
            return

        dup = set()
        # 代码意思是以当前元素为开始，遍历之后所有的元素，然后递归，然后再把这个元素吐出来
        # 遍历元素的时候后，从递归返回的时候就把上一次加入的元素退出来了，这样就实现不加入某些元素。
        # 这个dup的功能是记住这一次遍历中是否有重复元素！
        # 重点是用set记住这一次遍历的元素！
        for i in range(start, len(arrs)):
            if arrs[i] in dup:
                continue
            if not cur or arrs[i] >= cur[-1]:
                cur.append(arrs[i])
                dup.add(arrs[i])
                self.DFS(arrs, i + 1, cur, ans)
                cur.pop()

    def findSubsequences(self, arrs):
        ans = []
        self.DFS(arrs, 0, [], ans)
        return ans


if __name__ == '__main__':
    arrs = [4, 6, 7, 7]
    print(Solution().findSubsequences(arrs))

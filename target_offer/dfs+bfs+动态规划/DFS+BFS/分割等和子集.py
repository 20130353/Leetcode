#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 分割等和子集.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :
class Solution:
    def DFS(self, arrs, n, target, pos, cur_sum, flag):
        if flag[0] or cur_sum > target:
            return
        if pos == n or cur_sum == target:
            flag[0] = cur_sum == target
            return

        if sum((arrs[pos:])) + cur_sum < target:
            return

        self.DFS(arrs, n, target, pos + 1, cur_sum + arrs[pos], flag)
        self.DFS(arrs, n, target, pos + 1, cur_sum, flag)

    def canPartition(self, arrs):
        if not arrs or arrs.__len__() <= 1 or sum(arrs) % 2 != 0:
            return False
        target = sum(arrs) / 2
        arrs = sorted(arrs)
        new_arrs = []
        for i in range(len(arrs) - 1, -1, -1):
            if arrs[i] > target:
                return False
            if arrs[i] != target and arrs[i] != 0:
                new_arrs.append(arrs[i])
            if arrs[i] == target:
                return True
        flag = [False]
        self.DFS(new_arrs, len(new_arrs), target, 0, 0, flag)
        return flag[0]


if __name__ == '__main__':
    arrs = [3, 3, 3, 4, 5]
    print(Solution().canPartition(arrs))

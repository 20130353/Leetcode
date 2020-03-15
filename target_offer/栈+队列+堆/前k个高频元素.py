#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 前k个高频元素.py
# @Author: smx
# @Date  : 2020/2/21
# @Desc  :

from collections import Counter
import queue as Q


class Ele:
    def __init__(self, frequence, val):
        self.fre = frequence
        self.val = val

    def __lt__(self, other):
        return self.fre > other.fre


class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        pri_queue = Q.PriorityQueue()
        for each in counter.items():
            pri_queue.put(Ele(each[1], each[0]))
        ans = []
        for i in range(k):
            ans.append(pri_queue.get().val)
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))

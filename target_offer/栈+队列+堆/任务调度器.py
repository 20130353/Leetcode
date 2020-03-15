#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 任务调度器.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :

import queue as Q
from collections import Counter


class Task(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    # True表示按照原来的顺序排序（从小到大），False表示按照逆序排序（从大到小）
    def __lt__(self, other):
        return self.priority > other.priority

    # 这两种方式是等价的
    def __gt__(self, other):
        return self.priority < other.priority


# 这道题的重点是不按照顺序，任意顺序所以就考虑按照某种顺序安排任务。
# 问题是等待时间内怎么安排！所以就按照n+1为一轮安排！
class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        print(count)
        queue = Q.PriorityQueue()
        for key, value in count.items():
            queue.put(Task(value, key))

        time = 0
        while not queue.empty():
            t = n + 1
            new_queue = Q.PriorityQueue()
            while not queue.empty():
                each = queue.get()
                print(each.priority, each.name)
                if t > 0:
                    each.priority -= 1
                    if each.priority > 0:
                        new_queue.put(each)
                    t -= 1
                else:
                    new_queue.put(each)
            queue = new_queue
            time += n + 1 if not queue.empty() else n + 1 - t
        return time


if __name__ == '__main__':
    tasks = ['A', 'A', 'B']
    n = 2
    print(Solution().leastInterval(tasks, n))

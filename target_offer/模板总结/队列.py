#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 队列.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :


class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name


from collections import Counter
import queue as Q


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

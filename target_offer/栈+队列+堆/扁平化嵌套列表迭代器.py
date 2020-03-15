#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 扁平化嵌套列表迭代器.py
# @Author: smx
# @Date  : 2020/2/13
# @Desc  :

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = []

        def queue_push(n_l):
            for item in n_l:
                if item.isInteger():
                    self.queue.append(item.getInteger())
                else:
                    queue_push(item.getList())

        queue_push(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0

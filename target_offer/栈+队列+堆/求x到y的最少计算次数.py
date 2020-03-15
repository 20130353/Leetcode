#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 求x到y的最少计算次数.py
# @Author: smx
# @Date  : 2020/2/15
# @Desc  :

class Solution():
    def min_time(self, x, y):
        queue = [x]
        ans = 0
        while queue:
            length = len(queue)
            for i in range(length):
                top = queue.pop(0)
                if top == y:
                    return ans
                queue.append(top + 1)
                queue.append(top - 1)
                queue.append(top * 2)
            ans += 1
        return ans


if __name__ == '__main__':
    x, y = map(int, input().strip().split(','))
    print(Solution().min_time(x, y))

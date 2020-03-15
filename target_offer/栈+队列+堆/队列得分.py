#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 队列得分.py
# @Author: smx
# @Date  : 2020/2/15
# @Desc  :

# AC：55%
# 重要的线索是value<=20,表示只能淘汰一次
class Solution():
    def score(self, arr):
        if not arr or len(arr) <= 0:
            return 0, 0

        n = len(arr)
        queue = []
        bonus = 0
        base = 0
        for i in range(n):
            # print(queue)
            if queue and queue[-1][0] == arr[i][0]:
                if arr[i][1] > 10 and queue[-1][1] > 10:
                    base += arr[i][1]
                    bonus += 1
                    queue.append(arr[i])
                elif arr[i][1] > 10 and queue[-1][1] <= 10:
                    base -= queue[-1][1]
                    queue.pop()
                    base += arr[i][1]
                    queue.append(arr[i])
                elif arr[i][1] <= 10 and queue[-1][1] > 10:
                    continue
                else:
                    if queue[-1][1] >= arr[i][1]:
                        continue
                    else:
                        base -= queue[-1][1]
                        queue.pop()
                        base += arr[i][1]
                        queue.append(arr[i])
            else:
                base += arr[i][1]
                queue.append(arr[i])
        total_score = base - bonus * 10
        return total_score, len(queue)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for i in range(n):
        a, b = map(int, input().strip().split(' '))
        arr.append((a, b))
    score, num = Solution().score(arr)
    print('{} {}'.format(score, num))

#
# 7
# 8 13
# 1 14
# 7 5
# 7 19
# 6 10
# 4 13
# 6 4

# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-16
# file: 滑动窗口的最大值问题
# description:

# 反思:
# 1. 窗口初始化的问题:应该从第一个元素开始找窗口的最值,只不过是当到达第一个窗口才开始保存最值
# 2. 警惕窗口的size可能小于等于0
# 3. 改进用双端队列来做
# class Solution:
#     def maxInWindows(self, num, size):
#
#         if not num or size <= 0:
#             return []
#
#         if size == 1:
#             return num
#
#         queue = []
#         #init
#         queue.append((max(num[:size]),num.index(max(num[:size]))))
#         res = []
#
#         # 判断后续的窗口最值
#         for i in range(len(num)):
#
#             # 判断queue的头元素是否还在窗口中,如果不在就一直弹出
#             while(queue and queue[0][1] <= i- size):
#                 queue.pop(0)
#
#             # 队列为空
#             if not queue:
#                 queue.append((num[i],i))
#             else:
#                 # 队列不为空
#                 if num[i] >= queue[0][0]:
#                     del queue[:]
#                     queue.append((num[i], i))
#                 else:
#                     while (queue[-1][0] <= num[i]):
#                         queue.pop()
#                     queue.append((num[i], i))
#
#             if i >= size-1:
#                 res.append(queue[0][0])
#
#         return res

from collections import deque


def windows(arr, size):
    res = []
    deq = deque()
    for i in range(len(arr)):
        while len(deq) >= 1 and i - size >= deq[0][1]:
            deq.popleft()
        while len(deq) >= 1 and deq[-1][0] <= arr[i]:
            deq.pop()
        deq.append((arr[i], i))
        print('-----------')
        print('i ', i)
        print(deq)
        if i >= size - 1:
            res.append(deq[0][0])
    return res

if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    size = 3
    ans = windows(arr, size)
    print(ans)

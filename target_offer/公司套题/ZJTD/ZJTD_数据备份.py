#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数据备份.py
# @Author: smx
# @Date  : 2019/9/15
# @Desc  :

# 超内存！

# 用计算的方式
# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = []
#     for _ in range(n):
#         a, b = map(int, input().strip().split(' '))
#         arr.append((a, b))
#
#     stack = []
#     i = 1
#     max_len = -1
#     while True:
#         if stack.__len__() == 0 and arr.__len__() == 0:
#             print('%d %d' % (i, max_len))
#             break
#         if arr.__len__() > 0 and i == arr[0][0]:
#             stack += [1] * arr[0][1]
#             arr.pop(0)
#         max_len = max(max_len, stack.__len__())
#         stack.pop(0)
#         i += 1

# 内存使用最大的时候是最后一次进的时候
# 处理时间是所有元素个数和
# case 通过20%

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    total = 0

    max_i = 0
    for _ in range(n):
        a, b = map(int, input().strip().split(' '))
        arr.append((a, b))
        total += b
        max_i = max(total - a, max_i)
    print(total + 1, max_i + 1)

# 3
# 1 1
# 2 1
# 3 1

# 3
# 1 2
# 2 3
# 3 4

# 4
# 1 3
# 2 2
# 5 1
